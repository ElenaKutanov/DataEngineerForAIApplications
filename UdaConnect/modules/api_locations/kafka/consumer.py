import logging
import json

from kafka import KafkaConsumer
from app.udaconnect.services import LocationService
from wsgi import app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api-location-kafka")


class Consumer:
  #To consume latest messages and auto-commit offsets
  consumer = KafkaConsumer('udaconnect-location',
                            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                            bootstrap_servers=['udaconnect-kafka-broker:5008'])

  for message in consumer:
      payload = message.value
      logger.info(f"Message: {message.topic}, {payload}")

      with app.app_context():
        LocationService.create(payload)


if __name__ == "__main__":
  Consumer()