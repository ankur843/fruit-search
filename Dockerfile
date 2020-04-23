FROM python:3.7-slim-stretch 

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --upgrade -r requirements.txt

COPY Map Map/

WORKDIR Map

EXPOSE 8080

CMD ["python", "server2.py"]
