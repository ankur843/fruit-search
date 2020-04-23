FROM python:3.7-slim-stretch 

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip3 install --upgrade -r requirements.txt

COPY app app/

COPY Map Map/

WORKDIR Map

EXPOSE 5000

EXPOSE 8080

CMD ["sh", "./run.sh"]
