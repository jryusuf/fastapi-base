from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def example_function(x, y):
    result = x + y
    print("The result is:", result)
    return result


def unused_function():
    pass
