FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

COPY . /app

RUN ["chmod", "+x", "./etc/wait-for-it.sh"]
CMD bash ./etc/entrypoint.dev.sh