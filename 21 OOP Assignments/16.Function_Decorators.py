def log_function_call(func):
    def wrapper():
        print("Function called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello from Ali")
say_hello()