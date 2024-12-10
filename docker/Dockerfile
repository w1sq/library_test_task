FROM python:3.12-slim

WORKDIR /app

COPY src/ /app/src/
COPY data/ /app/data/

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "-u", "main.py"]