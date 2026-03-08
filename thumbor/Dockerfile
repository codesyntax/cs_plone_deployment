# Downgrade to 3.12 to prevent Thumbor runtime crashes and syntax warnings
FROM python:3.12-slim

# Install git so uv can clone the repository directly from GitHub
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN mkdir -p /app

ENV UV_SYSTEM_PYTHON=1

# Install directly from GitHub to get the latest complete code
RUN uv pip install --no-cache \
    "git+https://github.com/bluedynamics/zodb-pgjsonb-thumborblobloader.git" \
    "thumbor>=7.0"

COPY thumbor.conf /etc/thumbor.conf

EXPOSE 8888

CMD ["thumbor", "--conf=/etc/thumbor.conf"]
