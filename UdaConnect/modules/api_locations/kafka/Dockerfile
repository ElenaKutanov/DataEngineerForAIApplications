FROM elenakutanov/udaconnect-api-locations:latest

RUN mkdir -p /kafka
WORKDIR /kafka

EXPOSE 5005

COPY . /kafka
ENV PYTHONPATH /kafka:/restful:/restful/app

CMD ["sleep", "3600"]