IMAGE_NAME = renaudhager/python-training-webapp

ifndef IMAGE_VERSION
    IMAGE_VERSION := $(shell git describe --abbrev=0 --tags --exact-match)
endif


all: build tag_latest

build:
	docker build --tag="$(IMAGE_NAME):$(IMAGE_VERSION)" .

tag_latest:
	docker tag $(IMAGE_NAME):$(IMAGE_VERSION) $(IMAGE_NAME):latest

push:
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASSWORD)
	docker push "$(IMAGE_NAME):$(IMAGE_VERSION)"
	docker push "$(IMAGE_NAME):latest"
