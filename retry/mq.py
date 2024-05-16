import time

import pika


class MQ:
    def __init__(self, host, queue_name):
        self.host = host
        self.queue_name = queue_name
        self.connection = None
        self.channel = None

        self._connect_with_retry()

    def _connect_with_retry(self):
        while True:
            try:
                parameters = pika.ConnectionParameters(self.host)
                self.connection = pika.BlockingConnection(parameters)
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue=self.queue_name, durable=True)
                print(' [*] Waiting for messages. To exit press CTRL+C')
                break
            except pika.exceptions.AMQPConnectionError:
                print("Connection to RabbitMQ failed. Retrying in 5 seconds...")
                time.sleep(5)

    def _close(self):
        self.connection.close()

    def publish(self, message):
        try:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue_name,
                                       body=message,
                                       properties=pika.BasicProperties(
                                           delivery_mode=pika.DeliveryMode.Persistent
                                       ))

            print(f" [x] Sent {message}")
        except pika.exceptions.AMQPConnectionError:
            print("Publish failed: Connection to RabbitMQ lost. Retrying in 5 seconds...")
            self._connect_with_retry()
            self.publish(message)

    def consume(self, callback):
        def _callback(ch, method, properties, body):
            msg = body.decode()
            print(f" [x] Received {msg}")
            time.sleep(body.count(b'.'))
            callback(msg)
            print(" [x] Done")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=_callback)

        while True:
            if self.connection.is_closed:
                print("Connection to RabbitMQ closed. Retrying in 5 seconds...")
                self._connect_with_retry()
                self.channel.basic_qos(prefetch_count=1)
                self.channel.basic_consume(queue=self.queue_name, on_message_callback=_callback)
            try:
                self.connection.process_data_events()
            except pika.exceptions.ConnectionClosedByBroker:
                continue
            except pika.exceptions.AMQPError as err:
                print(f"Caught an AMQP error: {err!r}")
                break
