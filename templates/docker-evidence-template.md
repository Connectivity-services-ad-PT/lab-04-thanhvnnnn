# Docker Evidence - Lab 04 Notification

## 1. Build image

- Command:

```bash
docker build -t fit4110/notification:lab04 .
```

- Screenshot/log: `reports/docker-build.png`

## 2. Run container

```bash
docker run --rm -p 8000:8000 --env-file .env fit4110/notification:lab04
```

- Screenshot: `reports/docker-ps.png`

## 3. Health check

```bash
curl http://localhost:8000/health
```

- Screenshot: `reports/health-local.png`

## 4. Newman

```bash
npm run test:local
```

- Report: `reports/newman-lab04-local.html`
