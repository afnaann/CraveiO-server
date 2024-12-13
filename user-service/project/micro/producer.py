import json
import pika


def cart_initialize(method, body):
    # Connection parameters
    params = pika.URLParameters('amqps://mykxtdyr:iKVsLZI606pzmAl79e5527IB46YlGo27@puffin.rmq2.cloudamqp.com/mykxtdyr')
    
    try:
        # Establish connection
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        
        # Declare exchange (durable)
        channel.exchange_declare(exchange='cart_exchange', exchange_type='direct', durable=True)
        
        # Set message properties with durability
        properties = pika.BasicProperties(type=method, delivery_mode=2)  # delivery_mode=2 makes the message persistent
        # Publish message
        channel.basic_publish(exchange='cart_exchange', routing_key='main', body=json.dumps(body), properties=properties)
        print(f"Message published: {body}")
    except pika.exceptions.AMQPError as e:
        print(f"Failed to publish message: {e}")
    finally:
        if 'connection' in locals():
            connection.close()

