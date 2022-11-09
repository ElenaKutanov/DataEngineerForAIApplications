FROM python:3.9-alpine

RUN mkdir -p /restful
WORKDIR /restful

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

COPY ./requirements.txt /restful/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r /restful/requirements.txt

EXPOSE 5001

COPY . /restful
ENV PYTHONPATH /restful

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]