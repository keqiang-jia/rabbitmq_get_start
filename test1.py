import pika
import threading


class OperationLog:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        self.consume_thread = threading.Thread(target=self.monitor)
        self.consume_thread.daemon = True
        self.consume_thread.start()

    def _add_to_db(self, ch, method, properties, body):
        message = body.decode()
        print(f"Adding to database: {message}")

    def send(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
        print(f"Sent message: {message}")

    def monitor(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self._add_to_db, auto_ack=True)
        self.channel.start_consuming()


OperationLog('my_queue').send('Hello World')
