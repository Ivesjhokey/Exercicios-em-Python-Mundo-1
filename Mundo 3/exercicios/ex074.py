from random import randint
for c in range(0, 1):
    n1 = randint(1, 5)
    n2 = randint(1, 5)
    n3 = randint(1, 5)
    n4 = randint(1, 5)
    n5 = randint(1, 5)
tupla = (n1, n2, n3, n4, n5)
print(tupla)
print(f'o menor valor é {min(tupla)} e o maior é {max(tupla)}')
