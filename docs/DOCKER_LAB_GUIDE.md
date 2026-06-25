# Docker Lab Guide - Team Notify

## Why Docker?

Docker packages the Notification API, dependencies, runtime settings and start
command into one image so another machine can run the same service.

## Image and Container

```bash
docker build -t fit4110/team-notify:lab04 .
docker run --rm --name fit4110-notify-lab04 -p 8000:8000 --env-file .env.example fit4110/team-notify:lab04
```

## Dockerfile Checklist

The Dockerfile in this repo includes:

- Python 3.11 slim base image.
- Dependency install from `requirements.txt`.
- Source code copied into `/app/src`.
- Runtime config from `.env.example`.
- Non-root `appuser`.
- `EXPOSE 8000`.
- Healthcheck that calls `GET /health`.
- Uvicorn command for `notify_app.main:app`.

## Healthcheck

The container should report healthy only when the API is ready:

```Dockerfile
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3).read()" || exit 1
```

Manual check:

```bash
curl http://localhost:8000/health
docker inspect fit4110-notify-lab04
```

## Secrets

Do not commit real provider credentials. Lab 04 uses only:

```text
AUTH_TOKEN=local-dev-token
NOTIFY_MOCK_MODE=true
```

Real Telegram, SMS, email or push tokens must be supplied outside Git.
