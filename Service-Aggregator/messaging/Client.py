import pika
import uuid

class Colours(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, auto_ack=True, on_message_callback=self.on_response)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
           self.response = body.decode()

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='', routing_key='colour_queue', properties=pika.BasicProperties(
                                   reply_to=self.callback_queue, correlation_id=self.corr_id), body='')
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)

class Brands(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, auto_ack=True, on_message_callback=self.on_response)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
           self.response = body.decode()

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='', routing_key='brand_queue', properties=pika.BasicProperties(
                                   reply_to=self.callback_queue, correlation_id=self.corr_id), body='')
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)