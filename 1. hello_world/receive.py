#!/usr/bin/env python
import pika, sys, os

def main():
    # 建立连接
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 声明队列
    channel.queue_declare(queue='hello')

    # 回调函数
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # 指定队列对应的回调函数
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)