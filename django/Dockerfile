FROM python:3.11.5-slim-bullseye

# PIP_DISABLE_PIP_VERSION_CHECK turns off an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# PYTHONDONTWRITEBYTECODE means Python will not try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED ensures Docker does not buffer our console output
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code