import threading
from time import sleep

import pika, sys, os


def main(queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):
        print(f"进程ID：{os.getpid()}，线程ID：{threading.get_ident()}")
        print(f" [x] Received {body}")

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        threading.Thread(target=main, args=('hello1',)).start()
        threading.Thread(target=main, args=('hello2',)).start()
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
