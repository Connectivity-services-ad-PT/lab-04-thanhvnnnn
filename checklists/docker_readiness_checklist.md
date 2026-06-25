# Docker Readiness Checklist - Lab 04 Team Notify

## Dockerfile

- [x] Uses a small Python base image.
- [x] Defines `WORKDIR`.
- [x] Copies dependencies before source code for better Docker cache usage.
- [x] Exposes port `8000`.
- [x] Defines `CMD`.
- [x] Defines `HEALTHCHECK`.
- [x] Runs with a non-root user.
- [x] Does not contain real secrets.

## Runtime

- [x] Container maps host port `8000` to service port `8000`.
- [x] `/health` returns HTTP `200`.
- [x] Runtime configuration comes from `.env.example`.
- [x] Business endpoints require `Authorization: Bearer local-dev-token`.

## Testing

- [x] Newman collection targets the Notification service.
- [x] Newman report paths are configured in `reports/`.
- [x] Functional tests are included.
- [x] Auth tests are included.
- [x] Negative validation tests are included.
- [x] Boundary test for max message length is included.

## Evidence

- [x] Docker image evidence saved.
- [x] Container run evidence saved.
- [x] `GET /health` evidence saved.
- [x] Newman HTML/XML report generated.
- [ ] Registry image tag pushed.
