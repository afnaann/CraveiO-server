import pika
import json
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from micro.models import CustomUser,Roles



params = pika.URLParameters('amqps://mykxtdyr:iKVsLZI606pzmAl79e5527IB46YlGo27@puffin.rmq2.cloudamqp.com/mykxtdyr')

def user_role_callback(ch, method, properties, body):
    data = json.loads(body.decode())
    user = CustomUser.objects.get(id=data['user_id'])
    print(user)
    if data['role'] in Roles:
        user.role = data['role']
        user.save()
    else:
        print('this is not user role')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
try:
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    
    channel.exchange_declare(exchange='role_exchange', exchange_type='direct', durable=True)
    
    channel.queue_declare(queue='main', durable=True)
    channel.queue_bind(exchange='role_exchange', queue='main', routing_key='main')
    

    channel.basic_consume(queue='main', on_message_callback=user_role_callback, auto_ack=False)
    print('Waiting for messages...')
    
    channel.start_consuming()
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    if 'channel' in locals():
        channel.close()
    if 'connection' in locals():
        connection.close()
