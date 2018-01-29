x1 = int(input()) # координата х точки А
y1 = int(input()) # координата у точки В
x2 = int(input()) # координата х точки В
y2 = int(input()) # координата у точки В
x3 = int(input()) # координата х точки С
y3 = int(input()) # координата у точки С
ab2 = ((x2-x1)**2)+((y2-y1)**2) # сторона AB в квадрате
ac2 = ((x3-x1)**2)+((y3-y1)**2) # сторона AC в квадрате
bc2 = ((x3-x2)**2)+((y3-y2)**2) # сторона AC в квадрате
# print(ab2)
# print(ac2)
# print(bc2)
if ab2 > ac2 and ab2 > bc2:
    n1 = ab2
    n2 = ac2 + bc2
#    print('АВ - гипотенуза')
if ac2 > ab2 and ac2 > bc2:
    n1 = ac2
    n2 = ab2 + bc2
#    print('АС - гипотенуза')
if bc2 > ab2 and bc2 > ac2:
    n1 = bc2
    n2 = ab2 + ac2
#    print('ВС - гипотенуза')
if n1 == n2:
    print('yes')
else:
    print('no')
