FROM elenakutanov/udaconnect-api-persons:latest

RUN mkdir -p /grpc_server
WORKDIR /grpc_server

EXPOSE 5004

COPY . /grpc_server
ENV PYTHONPATH /grpc_server:/restful:/restful/app

RUN python -m grpc_tools.protoc -I/grpc_server/ --python_out=/grpc_server/ --grpc_python_out=/grpc_server/ /grpc_server/person.proto

CMD ["python", "/grpc_server/grpc_server.py"]