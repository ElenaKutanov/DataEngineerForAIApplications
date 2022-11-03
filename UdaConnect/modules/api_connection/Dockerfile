FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY api_connection/requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5002

COPY ./api_connection/ .

RUN python -m grpc_tools.protoc -I./app/grpc_client/ --python_out=./app/grpc_client/ --grpc_python_out=./app/grpc_client/ person.proto

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5002"]