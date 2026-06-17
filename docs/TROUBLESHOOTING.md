# Troubleshooting - Lab 04 Notification

## 1. Port 8000 đang bị chiếm

```bash
docker ps
```

Dừng container cũ hoặc đổi `APP_PORT` trong `.env`.

## 2. Gọi nghiệp vụ bị 401

Thêm header:

```text
Authorization: Bearer local-dev-token
```

## 3. Docker build lỗi package

Chạy lại:

```bash
docker build --no-cache -t fit4110/notification:lab04 .
```

## 4. Newman không tìm thấy collection

Kiểm tra file:

```text
postman/collections/FIT4110_lab04_notification_docker.postman_collection.json
```

## 5. `/health` chạy nhưng `/notifications` lỗi

Kiểm tra payload có đủ `alert_id`, `target`, `channels`, `priority`, `title`, `message` không.
