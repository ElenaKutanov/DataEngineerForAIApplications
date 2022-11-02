FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY persons_api/requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5002

COPY ./persons_api/ .
COPY ./models/model_person.py ./app/udaconnect/
COPY ./schemas/schema_person.py ./app/udaconnect/
COPY ./protobufs/person_pb2.py ./app/udaconnect/
COPY ./protobufs/person_pb2_grpc.py ./app/udaconnect/