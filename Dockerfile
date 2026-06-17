FROM python:3.11-slim

WORKDIR /app

# Tạo non-root user
RUN addgroup --system appgroup && \
    adduser --system --no-create-home --ingroup appgroup appuser

# Copy requirements và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Copy environment example
COPY .env.example .env

# Chown cho non-root user
RUN chown -R appuser:appgroup /app

# Switch sang non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check using Python (no curl needed)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Run
CMD ["uvicorn", "notify_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]