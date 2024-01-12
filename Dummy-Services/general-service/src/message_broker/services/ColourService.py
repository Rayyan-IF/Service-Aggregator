import json
import pika
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='colour_queue')

def get_all_colour(body):
    pagination = json.loads(body)
    page, limit = pagination["page"], pagination["limit"]
    getColour = requests.get(f"http://localhost:8001/api/sales/unit-colour?page={page}&limit={limit}")
    colourData = getColour.json()["data"]
    serialized = json.dumps(colourData, default=str)
    return serialized

def on_request(ch, method, props, body):
    response = get_all_colour(body)
    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id), body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='colour_queue', on_message_callback=on_request)

print("[x] Waiting for requests")
channel.start_consuming()