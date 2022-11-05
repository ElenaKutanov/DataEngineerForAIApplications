FROM elenakutanov/udaconnect-api-persons:latest

RUN mkdir -p /grpc_server
WORKDIR /grpc_server

EXPOSE 5004

COPY . /grpc_server
ENV PYTHONPATH /grpc_server:/restful:/restful/app

# RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ person.proto

CMD ["python", "/grpc_server/grpc_server.py"]