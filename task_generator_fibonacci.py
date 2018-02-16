# n = int(input())   # ввод кол-ва чисел
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a
# print(*fibonacci(n))   # вывод на экран
