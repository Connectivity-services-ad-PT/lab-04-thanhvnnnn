.PHONY: help install validate build run run-detached stop test-docker clean health logs

IMAGE_NAME := fit4110/team-notify:lab04
CONTAINER_NAME := fit4110-notify-lab04

help:
	@echo "Available commands:"
	@echo "  make install       Install Node dependencies"
	@echo "  make validate      Lint the OpenAPI contract"
	@echo "  make build         Build the Docker image"
	@echo "  make run           Run the Docker container"
	@echo "  make test-docker   Run Newman against the Docker container"
	@echo "  make stop          Stop the Docker container"
	@echo "  make health        Call GET /health"

install:
	npm install

validate:
	npm run validate:contract

build:
	docker build -t $(IMAGE_NAME) .
	docker tag $(IMAGE_NAME) ghcr.io/connectivity-services-ad-pt/team-notify:v0.1.0-team-notify

run:
	docker run --rm \
		--name $(CONTAINER_NAME) \
		-p 8000:8000 \
		--env-file .env.example \
		$(IMAGE_NAME)

run-detached:
	docker run -d --rm \
		--name $(CONTAINER_NAME) \
		-p 8000:8000 \
		--env-file .env.example \
		$(IMAGE_NAME)

test-docker: run-detached
	npx wait-on http://localhost:8000/health --timeout 30000
	npm run test:local
	$(MAKE) stop

stop:
	docker stop $(CONTAINER_NAME) 2>/dev/null || true

health:
	curl -f http://localhost:8000/health

logs:
	docker logs $(CONTAINER_NAME) -f

clean:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker rmi $(IMAGE_NAME) 2>/dev/null || true
