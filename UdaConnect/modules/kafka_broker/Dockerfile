FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5008

COPY . .

RUN cd bin
RUN export PATH=$KAFKA_HOME/bin:$PATH