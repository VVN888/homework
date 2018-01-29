x1 = int(input()) # координата х точки А
y1 = int(input()) # координата у точки В
x2 = int(input()) # координата х точки В
y2 = int(input()) # координата у точки В
x3 = int(input()) # координата х точки С
y3 = int(input()) # координата у точки С
ab = (((x2-x1)**2)+((y2-y1)**2))**(1/2) # сторона AB
ac = (((x3-x1)**2)+((y3-y1)**2))**(1/2) # сторона AC
bc = (((x3-x2)**2)+((y3-y2)**2))**(1/2) # сторона AC
# print(ab)
# print(ac)
# print(bc)
if ab >ac and ab> bc:
    n1 = ab**2
    n2 = ac**2 + bc**2
#    print('АВ - гипотенуза')
if ac >ab and ac> bc:
    n1 = ac**2
    n2 = ab**2 + bc**2
#    print('АС - гипотенуза')
if bc >ab and bc> ac:
    n1 = bc**2
    n2 = ab**2 + ac**2
#    print('ВС - гипотенуза')
if n1 == n2:
    print('yes')
else:
    print('no')
