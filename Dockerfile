# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# ensure to not install recommended deps
RUN apt-get update && \
    apt-get install \
    python3-dev python3-pip libpq-dev locales-all build-essential \
    libev-dev libblas-dev liblapack-dev gfortran libxml2-dev libxslt1-dev \
    -y --no-install-recommends

# set locale
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# write stdout/stderr without buffering
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/
WORKDIR /app

# wheel makes life easy
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install wheel
RUN python3 -m pip install -r requirements.txt

# copy code from repo to app directory
COPY . /app/
ENTRYPOINT [ "/app/run.sh" ]
