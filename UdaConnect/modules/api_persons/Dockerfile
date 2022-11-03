FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY api_persons/requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5003 5004

COPY ./api_persons/ .

RUN python -m grpc_tools.protoc -I./grpc_server/ --python_out=./grpc_server/ --grpc_python_out=./grpc_server/ person.proto