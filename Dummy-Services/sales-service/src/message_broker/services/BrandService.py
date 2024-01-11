import json
import pika
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='brand_queue')

def get_all_brand(body):
    pagination = json.loads(body)
    page, limit = pagination["page"], pagination["limit"]
    getBrand = requests.get(f"http://127.0.0.1:8002/api/sales/unit-brand?page={page}&limit={limit}")
    brandData = getBrand.json()["data"]
    serialized = json.dumps(brandData, default=str)
    return serialized

def on_request(ch, method, props, body):
    response = get_all_brand(body)
    ch.basic_publish(exchange='', routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                     props.correlation_id), body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='brand_queue', on_message_callback=on_request)

print("[x] Waiting for requests")
channel.start_consuming()