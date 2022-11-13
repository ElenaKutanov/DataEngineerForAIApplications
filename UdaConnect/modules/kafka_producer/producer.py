import logging
import json

from kafka import KafkaProducer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-kafka-producer")

class Server:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['udaconnect-kafka-brocker:5008'],
                      api_version=(0,11,5),
                      value_serializer=lambda x: dumps(x).encode('utf-8'))

    def send_location(self, person_id, creation_time):

        message = { "person_id": person_id,
                    "latitude": "-122.2908829999999938",
                    "longitude": "37.5536299999999983",
                    "creation_time": creation_time }
        self.producer.send('udaconnect-location', json.dumps(message))
        logger.info(f'KafkaProducer message sent: {message}')
        self.producer.flush()


if __name__ == "__main__":
    server = Server()
    logger.info(f'KafkaProducer run!')
    for _ in range(10):
        server.send_location(5, '2020-08-15 10:37:06.000000')
