from app import consumer2

@consumer2.task
def multiply(x, y):
    return x * y
