FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /timeslotAPI
WORKDIR /timeslotAPI
ADD . /timeslotAPI/
RUN pip install -r requirements.txt