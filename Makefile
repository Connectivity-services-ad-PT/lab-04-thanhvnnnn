.PHONY: help install build run stop test test-docker clean lint validate mock health

# Colors for output
GREEN := \033[0;32m
RED := \033[0;31m
NC := \033[0m

help:
	@echo "$(GREEN)Available commands:$(NC)"
	@echo "  make install      - Install Python dependencies"
	@echo "  make build        - Build Docker image"
	@echo "  make run          - Run Docker container"
	@echo "  make stop         - Stop Docker container"
	@echo "  make test         - Run tests locally"
	@echo "  make test-docker  - Run tests on Docker container"
	@echo "  make clean        - Clean up artifacts"
	@echo "  make lint         - Run linter checks"
	@echo "  make validate     - Validate OpenAPI contract"
	@echo "  make health       - Check service health"

install:
	@echo "$(GREEN)Installing Python dependencies...$(NC)"
	python -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	@echo "$(GREEN)Installing Node dependencies...$(NC)"
	npm install
	@echo "$(GREEN)Done! Activate venv with: source .venv/bin/activate$(NC)"

build:
	@echo "$(GREEN)Building Docker image...$(NC)"
	docker build -t fit4110/team-notify:lab04 .
	docker tag fit4110/team-notify:lab04 ghcr.io/fit4110/team-notify:v0.1.0-team-notify
	@echo "$(GREEN)Image built successfully!$(NC)"

run:
	@echo "$(GREEN)Running Docker container...$(NC)"
	docker run --rm \
		--name fit4110-notify-lab04 \
		-p 8000:8000 \
		--env-file .env.example \
		fit4110/team-notify:lab04

run-detached:
	@echo "$(GREEN)Running Docker container in background...$(NC)"
	docker run -d \
		--name fit4110-notify-lab04 \
		-p 8000:8000 \
		--env-file .env.example \
		fit4110/team-notify:lab04
	@echo "$(GREEN)Container started! Wait 5 seconds for health check...$(NC)"
	sleep 5

stop:
	@echo "$(GREEN)Stopping Docker container...$(NC)"
	docker stop fit4110-notify-lab04 2>/dev/null || true
	docker rm fit4110-notify-lab04 2>/dev/null || true

test:
	@echo "$(GREEN)Running local tests...$(NC)"
	source .venv/bin/activate && pytest tests/ -v --cov=src/notify_app --cov-report=html

test-docker: run-detached
	@echo "$(GREEN)Running Postman/Newman tests on Docker container...$(NC)"
	sleep 3
	npm run test:docker
	@echo "$(GREEN)Tests completed! Stopping container...$(NC)"
	make stop

clean:
	@echo "$(GREEN)Cleaning up...$(NC)"
	rm -rf .venv/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf reports/newman/*.html
	rm -rf reports/newman/*.xml
	docker rmi fit4110/team-notify:lab04 2>/dev/null || true
	@echo "$(GREEN)Cleanup complete!$(NC)"

lint:
	@echo "$(GREEN)Running linter...$(NC)"
	source .venv/bin/activate && flake8 src/ --max-line-length=120 --ignore=E203,W503
	source .venv/bin/activate && black src/ --check --line-length 120

format:
	@echo "$(GREEN)Formatting code...$(NC)"
	source .venv/bin/activate && black src/ --line-length 120

validate:
	@echo "$(GREEN)Validating OpenAPI contract...$(NC)"
	npm run validate:contract

mock:
	@echo "$(GREEN)Starting mock server...$(NC)"
	npm run mock:server

health:
	@echo "$(GREEN)Checking service health...$(NC)"
	curl -f http://localhost:8000/health || echo "$(RED)Service not healthy!$(NC)"

logs:
	@echo "$(GREEN)Showing container logs...$(NC)"
	docker logs fit4110-notify-lab04 -f

shell:
	@echo "$(GREEN)Opening shell in container...$(NC)"
	docker exec -it fit4110-notify-lab04 /bin/bash

stats:
	@echo "$(GREEN)Getting service metrics...$(NC)"
	curl http://localhost:8000/metrics | python -m json.tool