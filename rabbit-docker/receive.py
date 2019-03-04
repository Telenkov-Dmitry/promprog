import pika
import time

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

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback, queue='random')
channel.start_consuming()
