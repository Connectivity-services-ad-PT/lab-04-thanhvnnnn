# Docker Readiness Checklist - Lab 04 Notification

- [x] Có `Dockerfile`.
- [x] Có `.dockerignore`.
- [x] Có `.env.example`, không commit secret thật.
- [x] Container chạy bằng user non-root.
- [x] Có `HEALTHCHECK` gọi `/health`.
- [x] `GET /health` không cần token.
- [x] Endpoint nghiệp vụ cần bearer token.
- [x] Có Problem Details cho lỗi 401/404/409/422.
- [x] Có Postman/Newman collection.
- [ ] Đã build image trên máy cá nhân.
- [ ] Đã chạy container và chụp `docker ps`.
- [ ] Đã chạy `npm run test:local` và lưu report thật.
