# 连接到RabbitMQ服务器
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 删除队列
channel.queue_delete(queue='my_queue')

# 关闭连接
connection.close()
