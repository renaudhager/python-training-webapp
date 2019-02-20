FROM ubuntu:14.04
RUN apt-get update -y && \
  apt-get install -y curl dnsutils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip
COPY ./webapp/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
COPY ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]
