FROM python:3.9-alpine

WORKDIR .

RUN apk add --no-cache gcc bash openjdk8

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5007

COPY . .