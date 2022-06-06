def nod(a, b):
  while b:
    a, b = b, a % b
  return a
def nok(n,m):
    return (n/nod(n,m))*m  
print(int(nok(4,6)))

