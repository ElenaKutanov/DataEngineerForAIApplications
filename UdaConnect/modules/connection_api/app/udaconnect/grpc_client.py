import grpc

from person_pb2 import Empty
from person_pb2_grpc import PersonServiceStub

"""
Used to send get all persons gRPC message to persons microservice.
"""

class GRPC_client:
    def __init__(self):
        print("Sending grpc persons retrive all...")

        channel = grpc.insecure_channel("localhost:30005")
        self.client = PersonServiceStub(channel)


    def persons_retrieve_all(self):
        request = Empty()
        print('Send GET!')
        response = self.client.Get(request)
        print('Get:', response)

        return response