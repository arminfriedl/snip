FROM python:3.8-alpine

RUN apk update && apk add su-exec \
  && pip3 install pipenv

COPY . /app
WORKDIR /app

ENV FLASK_APP=snip
ENV FLASK_ENV=production

RUN pipenv install

EXPOSE 5000
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
