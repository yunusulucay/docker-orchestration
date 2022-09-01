FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip3 install requests
RUN pip3 install pymongo
RUN apt-get install libpq-dev python3-dev -y
RUN pip3 install psycopg2
RUN mkdir -p /tmp/script
COPY manipulate.py /tmp/script
CMD [ "python3","/tmp/script/manipulate.py" ]