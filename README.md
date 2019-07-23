## Docker Small WebApp

[![Docker Pulls](https://img.shields.io/docker/pulls/renaudhager/python-training-webapp.svg)](https://hub.docker.com/r/renaudhager/python-training-webapp)

# Description
Small python, inspired by Docker training application. (https://github.com/docker-training/webapp)

## Build
To build this image, run the following command:
```
make build
```

## Run
To run this Docker image, run the following command:
```
docker run -d \
  -p 5000:5000 \
  renaudhager/python-training-webapp:latest
```
