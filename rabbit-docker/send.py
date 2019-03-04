import pika
import time
import random

conection = None
while True:
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters("rabbit", 5672))
    except pika.exceptions.ConnectionClosed:
        time.sleep(4.2)
    else:
        break

channel = connection.channel()
channel.queue_declare(queue='random')
while True:
    time.sleep(random.uniform(1, 5))
    data = "{}".format(random.randint(1, 100))
    print("sent {}".format(data))
    channel.basic_publish(exchange='',
     routing_key='random',
     body=data.encode()
    )
