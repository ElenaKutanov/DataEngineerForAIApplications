FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY ./requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5004

COPY . .

# RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ person.proto

CMD ["python", "./grpc_server.py"]