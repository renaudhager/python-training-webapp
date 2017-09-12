NAME = renaudhager/python-training-webapp

GIT_TAG := $(shell git describe --abbrev=0 --tags --exact-match)

all: build tag_latest

build:
	docker build --tag="$(NAME):$(GIT_TAG)" .

tag_latest:
	docker tag $(NAME):$(GIT_TAG) $(NAME):latest

push:
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASSWORD)
	docker push "$(NAME):$(GIT_TAG)"
	docker push "$(NAME):latest"
