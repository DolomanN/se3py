# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in list: 
    if i not in new_list:
        new_list.append(i) 
print (new_list)
