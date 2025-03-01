FROM python:3.12-alpine

WORKDIR /consumer2

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "celery", "-A", "app", "worker", "-Q", "multiplyQueue", "--loglevel=info", "--concurrency=1", "--logfile=/consumer2/logs/consumer2.log"]
