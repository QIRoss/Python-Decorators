import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start} seconds")
    return wrapper

@measure_time
def hello():
    print("Hello, world!")

hello()