# RUN LOCAL - Lab 04 Notification

## Cách chạy nhanh

```bash
cp .env.example .env
npm install
docker build -t fit4110/notification:lab04 .
docker run --rm -p 8000:8000 --env-file .env fit4110/notification:lab04
```

Kiểm tra health:

```bash
curl http://localhost:8000/health
```

Chạy Newman:

```bash
npm run test:local
```

## Token demo

Các endpoint nghiệp vụ dùng header:

```text
Authorization: Bearer local-dev-token
```
