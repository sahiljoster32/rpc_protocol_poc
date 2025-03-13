from app import consumer1

@consumer1.task
def add(x, y):
    return x + y
