# Run Local - Lab 04 Team Notify

These steps let another student clone the repository, build the Docker image and
rerun the same tests.

## 1. Install test dependencies

```bash
npm install
```

## 2. Build the Docker image

```bash
docker build -t fit4110/team-notify:lab04 .
```

## 3. Run the container

```bash
docker run --rm \
  --name fit4110-notify-lab04 \
  -p 8000:8000 \
  --env-file .env.example \
  fit4110/team-notify:lab04
```

Expected health response:

```json
{
  "status": "ok",
  "service": "notification",
  "version": "0.4.0",
  "dependencies": {
    "queue": "mock-ready",
    "sender": "mock-ready"
  }
}
```

## 4. Run Newman against the container

```bash
npm run test:local
```

Reports:

```text
reports/newman-lab04-local.xml
reports/newman-lab04-local.html
```

## 5. Stop the container

The command in step 3 uses `--rm`, so `Ctrl+C` is enough. If the container is
still running:

```bash
docker stop fit4110-notify-lab04
```
