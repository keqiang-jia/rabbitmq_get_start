from mq import MQ

MQ(host="localhost", queue_name="my_queue").publish("Hello World")


# #!/usr/bin/env python
# import pika
# import sys
# import time
#
#
# def on_connection_blocked(method_frame):
#     # 连接被阻止时的处理逻辑
#     print("Connection blocked. Retrying in 5 seconds...")
#     time.sleep(5)
#     connect()
#
#
# def on_connection_unblocked(method_frame):
#     # 连接恢复正常时的处理逻辑
#     print("Connection unblocked!")
#
#
# def connect():
#     try:
#         connection = pika.BlockingConnection(
#             pika.ConnectionParameters(host='localhost'))
#         connection.add_on_connection_blocked_callback(on_connection_blocked)
#         connection.add_on_connection_unblocked_callback(on_connection_unblocked)
#         return connection
#     except pika.exceptions.AMQPConnectionError:
#         print("Connection failed. Retrying in 5 seconds...")
#         time.sleep(5)
#         return connect()
#
#
# connection = connect()
# channel = connection.channel()
#
# channel.queue_declare(queue='task_queue', durable=True)
#
# message = ' '.join(sys.argv[1:]) or "Hello World!"
# channel.basic_publish(
#     exchange='',
#     routing_key='task_queue',
#     body=message,
#     properties=pika.BasicProperties(
#         delivery_mode=pika.DeliveryMode.Persistent
#     ))
# print(f" [x] Sent {message}")
# connection.close()
