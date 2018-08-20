# _*_coding: utf-8 _*_
from pykafka import KafkaClient

#Kafka的IP和端口
client = KafkaClient(hosts="10.114.24.134:9092")
#print client.topics
#把所有topic中的名为test的topic取出来赋值
topic = client.topics['test']
#print topic
#同步生产消息，kafka自带的api
producer = topic.get_producer()

#发送消息
message = "223344qw667788912"
producer.produce(message)
print message
#收尾
producer.stop()
