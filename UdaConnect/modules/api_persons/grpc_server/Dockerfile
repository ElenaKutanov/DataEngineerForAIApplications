FROM elenakutanov/udaconnect-api-persons:latest

EXPOSE 5004

COPY . .
ENV PYTHONPATH /grpc_server:/restful/app

# RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ person.proto

CMD ["python", "./grpc_server.py"]