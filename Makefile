DOCKER=docker

TAG=mobilityhouse/grafana-bot

image:
	${DOCKER} build . -t ${TAG}

shell:
	${DOCKER} run --rm -it  \
		-v ${PWD}/data:/data \
		-v ${PWD}/src:/bench \
		${TAG} \
		/bin/bash

apply:
	${DOCKER} run --rm -it  \
		-v ${PWD}/data:/data \
		-v ${PWD}/out:/tmp/out \
		-v ${PWD}/src:/bench \
		${TAG} \
		python config.py

convert:
	${DOCKER} run --rm -it  \
		-v ${PWD}/src:/bench \
		-v ${PWD}/data:/data \
		-v ${PWD}/in:/tmp/in \
		-v ${PWD}/out:/tmp/out \
		${TAG} \
		python convert.py

.PHONY: apply convert image
