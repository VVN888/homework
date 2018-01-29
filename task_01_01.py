y = int(input('y: ')) # ввод года
y1 = y / 100 # кратность 100-м
y2 = y / 400 # кратность 400-м
y3 = y / 4   # кратность 4-м
# print(y1)
# print(y2)
# print(y3)
if (int(y1) == float(y1) and int(y2) != float(y2)) or (int(y3) != float(y3)):
    print('no')
else:
    print('yes')
