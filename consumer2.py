from pykafka import KafkaClient

client = KafkaClient(hosts="10.114.24.134:9092")
#print client.topics
topic = client.topics['test']
consumer = topic.get_simple_consumer(consumer_group='test',  consumer_id='test')

for message in consumer:
        print message.offset, message.value

        str = message.value
        q = 'qw'
        result = q in str
        if result == True:
            with open('D:\consumer_mes.txt', 'w') as f:
                f.write(str)
#auto_commit_enable=True,