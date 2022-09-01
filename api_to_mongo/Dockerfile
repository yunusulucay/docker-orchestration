FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip3 install requests
RUN pip3 install pymongo
#RUN apt-get install wget -y
#RUN apt install -y software-properties-common gnupg apt-transport-https ca-certificates
#RUN apt install -y mongodb
#RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
#RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt-get clean -y
RUN mkdir -p /tmp/script
COPY get_api_to_mongodb.py /tmp/script/
CMD ["python3","/tmp/script/get_api_to_mongodb.py" ]
