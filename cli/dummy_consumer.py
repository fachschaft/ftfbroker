import configloader as c
from ftfbroker.consumer import GeneralConsumer
from ftfbroker.topic import TOPIC_AUTOMATE_STOCK

if __name__ == '__main__':
    consumer = GeneralConsumer(
        topics=[TOPIC_AUTOMATE_STOCK],
        kafka_server=c.KAFKA_SERVER,
        kafka_user=c.KAFKA_USER,
        kafka_password=c.KAFKA_PASSWORD,
        start_point='earliest',
    )

    for message in consumer.consume():
        print(message)
