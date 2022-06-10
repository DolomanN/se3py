data = open("task5/text.txt")
list = data.read().split(",")
list = [int(x) for x in list]
print(list)
new_list = []
for i in list:
    if i % 2 != 0:
        new_list.append(i)
print(new_list)
