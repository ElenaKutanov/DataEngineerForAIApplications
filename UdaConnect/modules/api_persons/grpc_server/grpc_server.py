import time
import logging
import grpc

from concurrent import futures
from person_pb2 import PersonMessage, PersonMessageList
from person_pb2_grpc import PersonServiceServicer, add_PersonServiceServicer_to_server
#from app.udaconnect.services import PersonService


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("udaconnect-api-persons")


class PersonServicer(PersonServiceServicer):
    def Get(self, request, context):
        logger.info('Received a message! GET')
        print('Received a message! GET')
        #all_persons = PersonService.retrieve_all()

        result = PersonMessageList()


        # for person in all_persons:
        #     grpc_person = PersonMessage (
        #         id = person.id,
        #         first_name = person.first_name,
        #         last_name = person.last_name,
        #         company_name = person.company_name
        #     )

        #     result.persons.append(grpc_person)

        logger.info(result)
        print('Response:', result)

        return result


class GRPC_server:
    def __init__(self):
        # Initialize gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        add_PersonServiceServicer_to_server(PersonServicer(), server)

        logger.info('Server starting on port 5004...')
        print('Server starting on port 5004...')
        server.add_insecure_port("[::]:5004")
        server.start()
        server.wait_for_termination()

if __name__ == "__main__":
    logger.info('Run gRPC server!')
    print('Run gRPC server!')
    GRPC_server()