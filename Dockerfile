FROM python:3.8-alpine

RUN apk update && apk add su-exec \
  && pip3 install pipenv

RUN mkdir -p /data

COPY . /app
WORKDIR /app

RUN pipenv install
RUN pipenv install gunicorn

ENV SNIP_DATABASE="sqlite"
ENV SNIP_DATABASE_URI="sqlite:////data/snip.db"
ENV SNIP_FLASK_HOST="0.0.0.0"

EXPOSE 5000
CMD ["pipenv", "run", "gunicorn", "-b0.0.0.0:5000", "snip:app"]
