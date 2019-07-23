IMAGE_NAME = renaudhager/python-training-webapp

ifndef VERSION
    VERSION := $(shell git describe --abbrev=0 --tags --exact-match)
endif

.PHONY: all
all: build tag

.PHONY: build
build:
	docker build --tag="$(IMAGE_NAME):$(VERSION)" .

.PHONY: tag_latest
tag:
	docker tag "$(IMAGE_NAME):$(VERSION)" "$(IMAGE_NAME):latest"

.PHONY: push
push:
	docker push "$(IMAGE_NAME):$(VERSION)"
	docker push "$(IMAGE_NAME):latest"
