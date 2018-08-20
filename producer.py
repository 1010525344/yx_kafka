# -*- coding: utf8 -*-
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['10.114.24.134:9092','10.114.24.135:9092','10.114.24.136:9092'])  # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]

for i in range(3):
    msg = "msg"
    producer.send('logtest', bytes(msg, encoding='utf-8'))

