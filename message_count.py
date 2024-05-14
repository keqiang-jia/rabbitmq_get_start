import pika

# 连接到RabbitMQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个队列
channel.queue_declare(queue='my_queue')

# 获取消息数量
method_frame = channel.queue_declare(queue='my_queue')
print("消息数量：", method_frame.method.message_count)

connection.close()
