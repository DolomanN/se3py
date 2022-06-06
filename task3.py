#Составить список простых множителей натурального числа N
number = input ("введите число: ")
def Factor(n):
    list = []
    d = 2
    while d * d <= int(n):
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
    return list
print (Factor(int(number)))