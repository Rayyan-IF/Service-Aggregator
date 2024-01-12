import json
import pika
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='brand_queue')

def get_all_brand(body):
    data = json.loads(body)
    url = "http://localhost:8002/api/sales/brand-multi-id/"
    for i in data:
        url += f"{i}%2C"
    getBrand = requests.get(url)
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