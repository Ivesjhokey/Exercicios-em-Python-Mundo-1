cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    n1 = int(input('qual valor voce quer sacar?: '))
    while n1 >= 50:
        cedula50 += 1
        n1 = n1 - 50
    while n1 >= 20:
        cedula20 += 1
        n1 = n1 - 20
    while n1 >= 10:
        cedula10 += 1
        n1 = n1 - 10
    while n1 >= 1:
        cedula1 += 1
        n1 = n1 - 1
    if n1 == 0:
        break
print(f'para sacar o valor desejado foram nescessarias {cedula50} cedulas de 50,'
      f' {cedula20} cedulas de 20, {cedula10} cedulas de 10, {cedula1} cedulas de 1')
