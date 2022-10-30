FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY locations_api/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002

COPY ./persons_api/ .
COPY ./models/ ./app/udaconnect/
CMD ["flask", "run", "--host", "0.0.0.0"]