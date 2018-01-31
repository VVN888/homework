plate = int(input()) #Введите кол-во тарелок
cleaner = int(input()) #Введите кол-во моющего средства
while plate and cleaner:
    plate -= 1
    cleaner -= 0.5
# print(plate)
# print(cleaner)
if not plate and not cleaner:
    print("Все тарелки вымыты, моющее средство закончилось")
if not plate and cleaner:
    print("Все тарелки вымыты. Осталось", cleaner, "ед. моющего средства")
if plate and not cleaner:
    print("Моющее средство закончилось. Осталось", plate, "тарелок")
