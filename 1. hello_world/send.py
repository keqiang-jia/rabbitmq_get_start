#!/usr/bin/env python
import pika

# 建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明队列
channel.queue_declare(queue='hello')

# 指定消息和队列的对应关系 （空字符串标识的默认交换，允许我们指定消息应发送到哪个队列，队列名称在routing_key中指定）
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()