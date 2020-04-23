SHELL := /bin/bash
PWD := $(shell pwd)
CLIENTS?=1
GIT_REMOTE = github.com/7574-sistemas-distribuidos/docker-compose-init

default: build

all:

deps:
	go mod tidy
	go mod vendor

build: deps
	GOOS=linux go build -o bin/client github.com/7574-sistemas-distribuidos/docker-compose-init/client
.PHONY: build

docker-image:
	docker build -f ./server/Dockerfile -t "server:latest" .
	docker build -f ./client/Dockerfile -t "client:latest" .
.PHONY: docker-image

docker-compose-up: docker-image
	python3 scale_client.py clients=$(CLIENTS)
	docker-compose -f docker-compose-dev-tmp.yaml up -d --build
.PHONY: docker-compose-up

docker-compose-down:
	docker-compose -f docker-compose-dev-tmp.yaml stop -t 1
	docker-compose -f docker-compose-dev-tmp.yaml down
.PHONY: docker-compose-down

docker-compose-logs:
	docker-compose -f docker-compose-dev-tmp.yaml logs -f
.PHONY: docker-compose-logs

test:
	sudo ./server/healthcheck.sh
.PHONY: test

cleanup:
	rm docker-compose-dev-tmp.yaml
.PHONY: cleanup

inject-config:
	./inject_config.sh
.PHONY: inject-config
