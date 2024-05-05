#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout') # 声明交换机logs，类型为fanout

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# 发送消息到logs交换机，因为是fanout类型的交换机，routing_key没意义，于是为空
channel.basic_publish(exchange='logs', routing_key='', body=message) 
print(f" [x] Sent {message}")
connection.close()