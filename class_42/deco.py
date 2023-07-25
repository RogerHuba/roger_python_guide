from functools import wraps
from time import sleep

def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Yo mamma says "{orig_val}"'
    return wrapper


def sophisticated_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'It is with a great honor that I hear you say "{orig_val}"'
    return wrapper

def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


@procrastinate
@yo_mamma_decorator
@sophisticated_decorator
def just_sayin(txt):
    return txt


if __name__ == "__main__":
    print(just_sayin('I love star wars!'))
