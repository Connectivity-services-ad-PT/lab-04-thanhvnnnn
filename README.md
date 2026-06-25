# FIT4110 Lab 04 - Team Notify Docker Packaging

Service: **Notification Service** (`team-notify`)

Role in the Smart Campus Operations Platform: receive alert events from Core
Business and queue multi-channel notifications. For Lab 04, delivery is mocked;
no real email, SMS, Telegram or push token is stored in this repository.

## Lab 04 Scope

This repository demonstrates that the Notification service can be packaged and
tested as a single Docker container.

- FastAPI service with `GET /health`.
- Protected Notification endpoints using `Authorization: Bearer local-dev-token`.
- ProblemDetails-style error responses for auth and validation failures.
- OpenAPI contract in `contracts/notify.openapi.yaml`.
- Dockerfile with non-root runtime user and container healthcheck.
- `.dockerignore` and `.env.example`.
- Newman tests for functional, auth, negative and boundary cases.

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Public container health check |
| POST | `/notifications` | Queue an alert notification |
| GET | `/notifications` | List notification records |
| GET | `/notifications/{notification_id}` | Read notification detail |
| POST | `/notifications/{notification_id}/retry` | Queue a retry |
| GET | `/templates/{template_code}` | Read template metadata |
| GET | `/core-alerts/{alert_id}` | Mock Core Business alert for consumer smoke tests |

## Quick Start

Install Node dependencies for OpenAPI/Newman checks:

```bash
npm install
```

Build and run the container:

```bash
docker build -t fit4110/team-notify:lab04 .
docker run --rm --name fit4110-notify-lab04 -p 8000:8000 --env-file .env.example fit4110/team-notify:lab04
```

In another terminal:

```bash
curl http://localhost:8000/health
npm run test:local
```

Newman reports are written to:

```text
reports/newman-lab04-local.xml
reports/newman-lab04-local.html
```

## Suggested Image Tag

```bash
docker tag fit4110/team-notify:lab04 ghcr.io/connectivity-services-ad-pt/team-notify:v0.1.0-team-notify
```

Push the registry image only after signing in to the registry with the correct
class or GitHub Container Registry credentials.
