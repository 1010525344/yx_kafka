from kafka import KafkaConsumer
import json
import  re
consumer = KafkaConsumer('logtest',
                         bootstrap_servers=['10.114.24.135:9092'])

for message in consumer:
       print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset,
                                            bytes.decode(message.value)))

       # str = message.value
       str = bytes.decode( message.value)
       q='qw'
       result = q in str
       print(result)