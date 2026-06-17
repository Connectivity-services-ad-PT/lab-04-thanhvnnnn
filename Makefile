install:
	npm install

build:
	docker build -t fit4110/notification:lab04 .

run:
	docker run --rm -p 8000:8000 --env-file .env.example fit4110/notification:lab04

mock:
	npm run mock:notification

lint:
	npm run lint:openapi

test-local:
	npm run test:local
