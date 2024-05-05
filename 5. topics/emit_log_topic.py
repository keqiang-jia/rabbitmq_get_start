#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明交换机，类型为topic
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 指定一条消息的路由键，发送到指定交换机
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)

print(f" [x] Sent {routing_key}:{message}")
connection.close()