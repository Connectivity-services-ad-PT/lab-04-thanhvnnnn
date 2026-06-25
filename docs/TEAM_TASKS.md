# Team Tasks - Lab 04 Team Notify

Service: Notification

## Completed Items

- [x] Replace the IoT sample contract with `contracts/notify.openapi.yaml`.
- [x] Provide `GET /health`.
- [x] Protect business endpoints with a sample bearer token.
- [x] Return ProblemDetails-style JSON for auth and validation errors.
- [x] Build a Dockerfile for the Notification API.
- [x] Use `.dockerignore`.
- [x] Provide `.env.example` without real secrets.
- [x] Provide `RUN_LOCAL.md`.
- [x] Run the container as a non-root user.
- [x] Add a Docker `HEALTHCHECK`.
- [x] Add Postman/Newman tests for functional, auth, negative and boundary cases.
- [x] Configure GitHub Actions to build the container and run Newman.

## Notification Notes

- Mock channels are enough for Lab 04.
- Do not commit real email, SMS, Telegram or push provider tokens.
- Suggested image tag: `ghcr.io/connectivity-services-ad-pt/team-notify:v0.1.0-team-notify`.
