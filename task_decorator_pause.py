import time


def pause(f):
    time.sleep(2)
    return str(f)   #(*args, **kwargs), добавил тип str

@pause   # 1-й вар-т реализации декоратора
def func(*args, **kwargs):
    pass
print('Фунция выполняется с задержкой 2 секунды!')
# func = pause(func)   # 2-й вар-т реализации декоратора
#print('Фунция выполняется с задержкой 2 секунды!')
