FROM python:3.13-slim-bookworm
RUN mkdir -p /var/log
COPY src/* /
RUN pip install -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]
