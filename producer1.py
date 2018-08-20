# _*_coding: utf-8 _*_
from kafka import KafkaProducer

kafka_host = '10.114.24.135'  # kafka服务器地址
kafka_port = 9092  # kafka服务器的端口

producer = KafkaProducer(bootstrap_servers=['{kafka_host}:{kafka_port}'.format(
    kafka_host=kafka_host,
    kafka_port=kafka_port
)])

# 消息
message_string = "some"

# 调用send方法，发送名字为'logtest'的topicid ，发送的消息为some
response = producer.send('logtest', message_string.encode('utf-8'))
print

response
