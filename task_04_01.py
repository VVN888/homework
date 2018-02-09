with open('data.txt') as f:
    data_txt = f.read()
    data_txt = data_txt.split(' ')

n = int(input())
p = int(input())
lst1 = []
lst2 = []

for i in range(len(data_txt)):
    data_txt[i] = int(data_txt[i])
    if (data_txt[i]) // n == (data_txt[i]) / n:   # 1-й вариант проверки
#    if (data_txt[i]) / n == int((data_txt[i]) / n):   # 2-й вариант проверки
        lst1.append(str(data_txt[i]))
    lst2.append(str(data_txt[i]**p))

with open('out-1.txt','w') as f_new1:
    f_new1.write(" ".join(lst1))
with open('out-2.txt','w') as f_new2:
    f_new2.write(" ".join(lst2))

# print(data_txt)
# print(lst1)
# print(lst2)
