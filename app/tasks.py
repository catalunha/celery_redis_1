import time

from celery import Celery

# from celery.schedules import crontab
app = Celery(
    main="tasks",
    broker="redis://localhost:6379/0",
)

app.conf.beat_schedule = {
    "add-print-in-5-seconds": {
        "task": "tasks.print_hello",
        "schedule": 30,
    }
}


@app.task
def hello_redis(name):
    print("start")
    time.sleep(5)
    for i in range(100000):
        print(i)
    message = f"Redis: Olá, ${name}"
    print("end")
    return message


@app.task
def print_hello():
    print("Hello schedule...")
