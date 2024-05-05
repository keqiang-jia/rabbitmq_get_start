#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明交换机，类型为direct
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 指定一条消息的路由键，发送到指定交换机
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
    
print(f" [x] Sent {severity}:{message}")
connection.close()