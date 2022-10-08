FROM alpine:latest
LABEL maintainer="Elena Kutanov"

WORKDIR /opt

COPY . /opt

RUN apk add cmd:pip
RUN pip freeze > requirements.txt

EXPOSE 3111

RUN apk add cmd:python3
RUN python3 init_db.py
CMD ["python3", "app.py"]