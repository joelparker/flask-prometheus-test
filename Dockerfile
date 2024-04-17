# syntax=docker/dockerfile:1
FROM python:3.9-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY *.py .

EXPOSE 3000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3000"]