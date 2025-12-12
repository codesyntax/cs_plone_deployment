FROM python:3.11.10-slim-bullseye
RUN mkdir -p /var/log
COPY src/* /
RUN pip install -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]