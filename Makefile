DOCKER=docker

TAG=mobilityhouse/grafana-bot

image:
	${DOCKER} build . -t ${TAG}

shell:
	${DOCKER} run --rm -it  \
		-v ${PWD}/data/secret:/tmp/secret \
		-v ${PWD}/src:/bench \
		${TAG} \
		/bin/bash

build:
	${DOCKER} run --rm -it  \
		-v ${PWD}/src:/bench \
		${TAG} \
		python config.py

.PHONY: image shell
