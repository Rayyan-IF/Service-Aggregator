import sys
import json
import pika
sys.path.append("../../../")
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.configs.database import get_database
from src.core.entities.common.UnitColourEntity import MtrColour

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='colour_queue')

def get_all_colour(db:Session):
    query_init = select(MtrColour)
    query_final = db.scalars(query_init).all()
    result = []
    for colour in query_final:
        data_outcome = {
            "colour_id": colour.colour_id,
            "brand_id": colour.brand_id,
            "colour_code": colour.colour_code,
            "colour_commercial_name": colour.colour_commercial_name,
            "colour_police_name": colour.colour_police_name,
            "is_active": colour.is_active,
        }
        result.append(data_outcome)
    serialized = json.dumps(result)
    return serialized

def on_request(ch, method, props, body):
    with get_database() as db:
        response = get_all_colour(db)
    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id), body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='colour_queue', on_message_callback=on_request)

print("[x] Waiting for requests")
channel.start_consuming()