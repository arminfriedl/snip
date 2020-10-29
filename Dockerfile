FROM python:3.8-alpine

RUN apk update && apk add su-exec \
  && pip3 install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install

ENV FLASK_APP=snip
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
