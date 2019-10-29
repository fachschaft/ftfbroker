from typing import Any

import configloader as c
from ftfbroker.producer import (
    AutomateStockProducer, GeneralProducer, RocketchatMensaProducer
)
from ftfbroker.protobuf.ftf.automate_stock_pb2 import (
    AutomateStock, AutomateStockV1
)


def send_with_generic_producer_instance(args: Any) -> None:
    prod = GeneralProducer(**args)

    # Prepare payload
    payload = AutomateStockV1(distance_cm=42.)
    envelop = AutomateStock(payload_v1=payload)

    prod.send(envelop, key="11")

    prod.flush()
    prod.close()


def send_with_generic_producer_static(args: Any) -> None:
    GeneralProducer.init_module(**args)

    # Prepare payload
    payload = AutomateStockV1(distance_cm=43.)
    envelop = AutomateStock(payload_v1=payload)

    GeneralProducer.send_(envelop, key="12")

    GeneralProducer.flush_()


def send_with_special_producer_instance(args: Any) -> None:
    prod = AutomateStockProducer(**args)

    payload = AutomateStockV1(distance_cm=44.)

    prod.sendV1("13", payload)

    prod.flush()
    prod.close()


def send_with_special_producer_static(args: Any) -> None:
    # GeneralProducer.init_module() would also be possible
    AutomateStockProducer.init_module(**args)

    payload = AutomateStockV1(distance_cm=44.)

    AutomateStockProducer.sendV1_("14", payload)
    AutomateStockProducer.flush_()


def send_rocketchat_mensa_example(args: Any) -> None:
    # GeneralProducer.init_module() would also be possible
    RocketchatMensaProducer.init_module(**args)

    payload = [
        ('11:30', ['Person A', 'Person B']),
        ('12:00', ['Person C'])
    ]

    RocketchatMensaProducer.sendV1_(payload)
    RocketchatMensaProducer.flush_()


if __name__ == '__main__':
    args = {
        'kafka_server': c.KAFKA_SERVER,
        'kafka_user': c.KAFKA_USER,
        'kafka_password': c.KAFKA_PASSWORD,
    }
    func = [
        send_with_generic_producer_instance,
        send_with_generic_producer_static,
        send_with_special_producer_instance,
        send_with_special_producer_static,
        send_rocketchat_mensa_example,
    ]

    for i, f in enumerate(func):
        print(f'{i+1}: {f.__name__}')

    index = int(input("Choose a function:"))

    func[index - 1](args)
