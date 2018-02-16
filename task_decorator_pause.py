import time


def pause(f):
    time.sleep(2)
    return f   #(*args, **kwargs)

@pause   # 1-й вар-т реализации декоратора
def func():
    pass
print('Фунция выполняется с задержкой 2 секунды!')
# func = pause(func)   # 2-й вар-т реализации декоратора
# print('Фунция выполняется с задержкой 2 секунды!')
