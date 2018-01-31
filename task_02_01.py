# s = (49094) # 1-й набор
# s = (Я бы изменил мир, но бог не дает исходники) # 2-й набор
# s = (Сел в озере березов лес) # 3-й набор
# s = input() # для ввода с клавиатуры
def is_palindrome(s):
    s = s.replace(' ', '')
    if s.lower() == s.lower()[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome
# print(bool(is_palindrome(s))) # для вывода на экран
