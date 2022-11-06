FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 5003

COPY . .
ENV PYTHONPATH /restful

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5003"]