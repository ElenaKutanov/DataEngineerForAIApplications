import time
from concurrent import futures

from flask import Flask
import logging

import grpc

import sys
sys.path.insert(0, "..")
sys.path.insert(0, "...")

from person_pb2 import PersonMessage, PersonMessageList
from person_pb2_grpc import PersonServiceServicer, add_PersonServiceServicer_to_server

from app.udaconnect.services import PersonService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-persons-api")
app = Flask(__name__)


class PersonServicer(PersonServiceServicer):
    def Get(self, request, context):
        logger.info('Received a message! GET')
        all_persons = PersonService.retrieve_all()

        result = PersonMessageList()

        for person in all_persons:
            grpc_person = PersonMessage (
                id = person.id,
                first_name = person.first_name,
                last_name = person.last_name,
                company_name = person.company_name
            )

            result.persons.append(grpc_person)

        logger.info(result)

        return result


class GRPC_server:
    def __init__(self):
        # Initialize gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        add_PersonServiceServicer_to_server(PersonServicer(), server)


        logger.info("Server starting on port 30005...")
        server.add_insecure_port("[::]:30005")
        server.start()
        # Keep thread alive
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == "__main__":
    logger.info('Run gRPC server!')
    app.run(host='localhost', debug=True)
    GRPC_server()