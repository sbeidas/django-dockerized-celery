from config.celery import app

@app.task(bind=True)
def add(self,x, y):
    return x + y
