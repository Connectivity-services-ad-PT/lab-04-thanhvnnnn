# FIT4110 Lab 04 - Docker Packaging cho Notification Service

## 1. Service của nhóm

- Service: **Notification Service** (`team-notify`)
- Vai trò: nhận alert từ Core Business và tạo thông báo đa kênh
- Cơ chế tích hợp: Queue async, lab mô phỏng bằng REST contract và test bằng Postman/Newman

## 2. Mục tiêu Lab 04

Lab này chứng minh service Notification chạy ổn định trong Docker container:

- Có `Dockerfile`.
- App chạy bằng user non-root.
- Có `HEALTHCHECK` gọi `GET /health`.
- Cấu hình qua `.env.example`.
- Có Postman/Newman test lại service trong container.
- Lỗi trả Problem Details.
- Không commit secret thật.

## 3. Endpoint chính

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/notifications` | Tạo notification từ alert |
| GET | `/notifications` | Liệt kê notification |
| GET | `/notifications/{notification_id}` | Xem chi tiết |
| POST | `/notifications/{notification_id}/retry` | Retry gửi lại |
| GET | `/templates/{template_code}` | Xem template |

## 4. Chạy bằng Docker

```bash
cp .env.example .env
docker build -t fit4110/notification:lab04 .
docker run --rm -p 8000:8000 --env-file .env fit4110/notification:lab04
```

Health:

```bash
curl http://localhost:8000/health
```

## 5. Chạy kiểm thử

```bash
npm install
npm run test:local
```

Report nằm trong `reports/`.

## 6. Minh chứng cần nộp

- `docker image ls` hoặc log build image.
- `docker ps` cho container đang chạy.
- `GET /health` trả 200.
- Newman report pass.
- Screenshot request/response happy path và lỗi.
