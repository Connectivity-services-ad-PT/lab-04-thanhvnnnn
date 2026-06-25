# syntax=docker/dockerfile:1.7

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SERVICE_NAME=notification
ENV SERVICE_VERSION=0.4.0
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8000

WORKDIR /app

RUN addgroup --system appgroup \
    && adduser --system --no-create-home --ingroup appgroup appuser

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY .env.example .env

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3).read()" || exit 1

CMD ["sh", "-c", "uvicorn notify_app.main:app --app-dir src --host ${APP_HOST} --port ${APP_PORT}"]
