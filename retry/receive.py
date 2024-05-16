from mq import MQ


def callback(msg):
    print(f" [x] Process {msg}")


MQ(host="localhost", queue_name="my_queue").consume(callback)

#
# #!/usr/bin/env python
# import pika
# import time
#
#
# def connect_with_retry():
#     try:
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#         return connection
#     except pika.exceptions.AMQPConnectionError:
#         print("Connection failed. Retrying in 5 seconds...")
#         time.sleep(5)
#         return connect_with_retry()
#
#
# connection = connect_with_retry()
# channel = connection.channel()
#
# channel.queue_declare(queue='task_queue', durable=True)
# print(' [*] Waiting for messages. To exit press CTRL+C')
#
#
# def callback(ch, method, properties, body):
#     print(f" [x] Received {body.decode()}")
#     time.sleep(body.count(b'.'))
#     print(" [x] Done")
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#
#
# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(queue='task_queue', on_message_callback=callback)
#
# while True:
#     if connection.is_closed:
#         print("Connection closed. Retrying in 5 seconds...")
#         connection = connect_with_retry()
#         channel = connection.channel()
#         channel.queue_declare(queue='task_queue', durable=True)
#         channel.basic_qos(prefetch_count=1)
#         channel.basic_consume(queue='task_queue', on_message_callback=callback)
#     try:
#         connection.process_data_events()
#     except pika.exceptions.ConnectionClosedByBroker:
#         continue
#     except pika.exceptions.AMQPError as err:
#         print(f"Caught an AMQP error: {err!r}")
#         break
