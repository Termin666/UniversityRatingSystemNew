import json
import os

import pika

from ..educator_rating.models import EducatorReport
from .convertions import bundle_report


def send_educator_report_to_broker(report: EducatorReport):
    data = bundle_report(report)

    with pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv('RABBITMQ_HOST')
            )
    ) as connection:
        channel = connection.channel()

        channel.basic_publish(
            exchange=os.getenv('RABBITMQ_EXCHANGE'),
            routing_key=os.getenv('RABBITMQ_ROUTING_KEY'),
            body=json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8')
        )
