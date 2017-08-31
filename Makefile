DOCKER=docker

TAG=mobilityhouse/grafana-bot

image:
	${DOCKER} build . -t ${TAG}

shell:
	${DOCKER} run --rm -it  \
		-v ${PWD}/data/secret:/tmp/secret \
		-v ${PWD}/data/setup.yaml:/tmp/setup.yaml \
		-v ${PWD}/src:/bench \
		${TAG} \
		/bin/bash

build:
	${DOCKER} run --rm -it  \
		-v ${PWD}/data/secret:/tmp/secret \
		-v ${PWD}/data/setup.yaml:/tmp/setup.yaml \
		-v ${PWD}/src:/bench \
		${TAG} \
		python config.py

convert:
	${DOCKER} run --rm -it  \
		-v ${PWD}/src:/bench \
		-v ${PWD}/data/reference.json:/tmp/reference.json \
		-v ${PWD}/in:/tmp/in \
		-v ${PWD}/out:/tmp/out \
		${TAG} \
		python convert.py

.PHONY: build convert image
