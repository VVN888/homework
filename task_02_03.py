# lst = [14, 8, 3, 1, 89, 2, 45] # 1-й набор
# lst = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45] # 2-й набор
def average(lst):
    return round(float(sum(lst)) / len(lst), 3)
# print(average(lst)) # для вывода на экран
