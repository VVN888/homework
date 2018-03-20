#import time
from time import sleep


def pause(sec_sleep):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep(sec_sleep)
            #print('Фунция выполняется с задержкой 2 секунды!')
            return func(*args, **kwargs)
            #print('Фунция выполняется с задержкой 2 секунды! - 2')
        return wrapper
    return decorator
