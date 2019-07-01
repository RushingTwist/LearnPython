import time
from functools import wraps


def log(func):
    @wraps(func)
    def function(*args, **kw):
        print('call %s' %func.__name__)
        return func(*args, **kw)

    function.level = level
    return function

@log
def timethis():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


timethis()
