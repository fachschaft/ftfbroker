from typing import Any

import configloader as c
from ftfbroker.consumer import GeneralConsumer
from ftfbroker import topic

def listen_all_ftf_topics(args: Any) -> None:
    consumer = GeneralConsumer(
        **args,
        topic_pattern="^ftf_.*",
    )

    for key, message in consumer.consume():
        print('Key:', key, '\nMessage:', message)


def listen_single_ftf_topic(args: Any) -> None:
    topics = [
        topic.TOPIC_AUTOMATE_STOCK,
        topic.TOPIC_ROCKETCHAT_MENSA,
    ]

    for i, t in enumerate(topics):
        print(f'{i+1}: {t}')

    index = int(input("Choose a topic:"))

    consumer = GeneralConsumer(
        **args,
        topics=[topics[index-1]],
    )

    for key, message in consumer.consume():
        print('Key:', key, '\nMessage:', message)


if __name__ == '__main__':
    args = {
        'kafka_server': c.KAFKA_SERVER,
        'kafka_user': c.KAFKA_USER,
        'kafka_password': c.KAFKA_PASSWORD,
    }
    func = [
        listen_all_ftf_topics,
        listen_single_ftf_topic,
    ]

    for i, f in enumerate(func):
        print(f'{i+1}: {f.__name__}')

    index = int(input("Choose a function:"))

    func[index - 1](args)
