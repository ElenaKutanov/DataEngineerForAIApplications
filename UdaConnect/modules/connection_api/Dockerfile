FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY connection_api/requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5003

COPY ./connection_api/ .
COPY ./models/ ./app/udaconnect/
COPY ./schemas/ ./app/udaconnect/
COPY ./protobufs/person_pb2.py ./app/udaconnect/
COPY ./protobufs/person_pb2_grpc.py ./app/udaconnect/

CMD ["flask", "run", "--host", "0.0.0.0"]