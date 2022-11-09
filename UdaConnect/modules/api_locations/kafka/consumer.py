
import logging
import json

from kafka import KafkaConsumer
from app.udaconnect.services import LocationService
from wsgi import app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api-location-kafka")


class Consumer:
  # To consume latest messages and auto-commit offsets
  consumer = KafkaConsumer('udaconnect-location',
                           group_id='udaconnect',
                           bootstrap_servers=['localhost:30005'])
  for message in consumer:
      # message value and key are raw bytes -- decode if necessary!
      # e.g., for unicode: `message.value.decode('utf-8')`
      print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
      payload = json.loads(message.decode('ascii'))
      with app.app_context():
        LocationService.create(payload)


if __name__ == "__main__":
  Consumer()