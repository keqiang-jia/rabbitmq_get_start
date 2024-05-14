import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_queue')

channel.basic_publish(exchange='', routing_key='my_queue', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
