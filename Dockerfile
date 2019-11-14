FROM python:3.7-alpine
MAINTAINER Ben Vandersteen "benjaminfvandersteen@gmail.com"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "/app/app.py" ]
