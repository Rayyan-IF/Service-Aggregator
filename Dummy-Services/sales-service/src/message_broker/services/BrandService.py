import sys
import json
import pika
sys.path.append("../../../")
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.configs.database import get_database
from src.core.entities.master.BrandEntity import MtrBrand

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='brand_queue')

def get_all_brand(db:Session):
    query_init = select(MtrBrand)
    query_final = db.scalars(query_init).all()
    result=[]
    for brand in query_final:
        data_outcome = {
            "brand_id": brand.brand_id,
            "brand_code": brand.brand_code,
            "brand_name": brand.brand_name,
            "brand_must_pdi": brand.brand_must_pdi,
            "brand_abbreviation": brand.brand_abbreviation,
            "brand_must_withdrawal": brand.brand_must_withdrawal,
            "supplier_id": brand.supplier_id,
            "warehouse_id": brand.warehouse_id,
            "atpm_unit": brand.atpm_unit,
            "atpm_finance": brand.atpm_finance,
            "atpm_workshop": brand.atpm_workshop,
            "atpm_sparepart": brand.atpm_sparepart,
            "is_active": brand.is_active,
        }
        result.append(data_outcome)
    serialized = json.dumps(result)
    return serialized

def on_request(ch, method, props, body):
    with get_database() as db:
        response = get_all_brand(db)
    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id), body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='brand_queue', on_message_callback=on_request)

print("[x] Waiting for requests")
channel.start_consuming()