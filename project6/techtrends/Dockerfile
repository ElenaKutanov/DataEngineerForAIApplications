FROM alpine:latest
LABEL maintainer="Elena Kutanov"

WORKDIR /opt/techtrends

COPY ./project6/techtrends ./
RUN apk add cmd:dir
RUN dir -s

RUN apk add cmd:python3
RUN apk add cmd:pip
RUN pip install -r requirements.txt

EXPOSE 3111

RUN apk add cmd:python3
RUN python3 init_db.py
CMD ["python3", "app.py"]
