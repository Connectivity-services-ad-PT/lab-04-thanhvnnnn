# Docker Lab Guide - Notification Service

## 1. Build image

```bash
docker build -t fit4110/notification:lab04 .
```

## 2. Run container

```bash
cp .env.example .env
docker run --rm -p 8000:8000 --env-file .env fit4110/notification:lab04
```

## 3. Health check

```bash
curl http://localhost:8000/health
```

Expected:

```json
{
  "status": "ok",
  "service": "notification",
  "version": "1.0.0",
  "dependencies": { "queue": "ready", "sender": "ready" }
}
```

## 4. Newman test

```bash
npm install
npm run test:local
```

## 5. Evidence

Lưu ảnh/log vào `reports/`:

- `docker-build.png`
- `docker-ps.png`
- `health-local.png`
- `newman-lab04-local.html`
- `container-logs.txt`
