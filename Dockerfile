# ── Stage 1: Build & Test ─────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN pytest test_app.py -v

# ── Stage 2: Production Image ─────────────────────────────────────────────────
FROM python:3.11-slim AS production

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Non-root user
RUN useradd -m -u 1001 -s /bin/bash appuser

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir flask==3.0.0 gunicorn==21.2.0

COPY --from=builder /app/app.py .

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "app:app"]
