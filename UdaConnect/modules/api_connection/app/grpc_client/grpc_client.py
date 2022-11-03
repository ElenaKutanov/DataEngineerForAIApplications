import logging

import grpc

from app.grpc_client.person_pb2 import Empty
from app.grpc_client.person_pb2_grpc import PersonServiceStub

"""
Used to send get all persons gRPC message to persons microservice.
"""

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api-connection")

class GRPC_client:
    def __init__(self):
        print("Sending grpc persons retrive all...")

        channel = grpc.insecure_channel("localhost:5004")
        self.client = PersonServiceStub(channel)


    def persons_retrieve_all(self):
        request = Empty()
        print('Send GET!')
        response = self.client.Get(request)
        print('Get:', response)

        return response

if __name__ == "__main__":
    logger.info('Run gRPC client!')
    print('Run gRPC client!')
    client = GRPC_client()
    print('Send retrive all persons!')
    client.persons_retrieve_all()