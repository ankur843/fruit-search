FROM python:3.7-slim-stretch 

RUN apt-get update && apt-get install -y git python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip3 install --upgrade -r requirements.txt

COPY app app/

COPY Map Map/

COPY Map/run.sh/ run.sh 

WORKDIR Map

RUN ["chmod","+x","run.sh"]

EXPOSE 5000

EXPOSE 8080

RUN pwd

RUN ls -ltr

CMD ["sh","./run.sh"]

