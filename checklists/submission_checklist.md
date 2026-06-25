# Submission Checklist - Lab 04 Team Notify

- [x] `Dockerfile`
- [x] `.dockerignore`
- [x] `.env.example`
- [x] `RUN_LOCAL.md`
- [x] Notification OpenAPI contract: `contracts/notify.openapi.yaml`
- [x] Postman collection: `postman/collections/team_notify.postman_collection.json`
- [x] Postman local environment: `postman/environments/team_notify_local.postman_environment.json`
- [x] Newman XML/HTML report path configured in `reports/`
- [x] GitHub Actions workflow builds the image and runs Newman
- [x] Container has `GET /health`
- [x] Container runs as a non-root user
- [x] Functional, auth, negative and boundary tests are included
- [x] ProblemDetails responses are used for auth and validation errors
- [x] Docker build/run/health evidence saved in `reports/lab04-docker-evidence.md`
- [x] Newman XML/HTML reports generated in `reports/`
- [ ] Registry image has been pushed with tag `v0.1.0-team-notify`
