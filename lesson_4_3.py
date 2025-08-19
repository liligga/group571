# декораторы

def printer(function):
    def wrapper(*args, **kwargs):
        print(f"До вызова функции {function.__name__}")
        result = function(*args, **kwargs)
        print(f"После вызова функции {function.__name__}")
        return result

    return wrapper


@printer
def hello_world():
    print("Hello World")


@printer
def add_numbers(a, b):
    return a + b


hello_world()
result = add_numbers(1, b=2)
print(result)
