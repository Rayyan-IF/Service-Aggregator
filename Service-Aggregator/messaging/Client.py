import pika
import uuid

class Rpc(object):
    def __init__(self, queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, auto_ack=True, on_message_callback=self.on_response)
        self.queue_name = queue_name

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
           self.response = body.decode()

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, properties=pika.BasicProperties(
                                   reply_to=self.callback_queue, correlation_id=self.corr_id), body='')
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)