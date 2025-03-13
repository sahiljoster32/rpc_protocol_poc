FROM python:3.12-alpine

WORKDIR /consumer1

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python" , "-m", "celery", "-A", "app", "worker", "-Q", "addQueue", "--loglevel=info", "--concurrency=1", "--logfile=logs/consumer1.log"]
