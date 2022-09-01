FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install libpq-dev python3-dev -y
RUN pip3 install psycopg2
RUN pip3 install dash
RUN pip3 install pandas
RUN mkdir -p /tmp/script
COPY deploy.py /tmp/script
CMD [ "python3","/tmp/script/deploy.py" ]