# alternativa 1 de jhokey

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('digite o sexo da pessoa [M/F}: ').upper()
print('fim')

# alternatuva 2 de jhokey

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('digite seu sexo [M/F}: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('sexo invalido, informe um sexo valido: ').upper()
print('sexo {} registrado com sucesso!'.format(sexo))

# alternativa guanabara

sexo = input('digite seu sexo [M/F}: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('sexo invalido, informe um sexo valido: ').upper()
print('sexo {} registrado com sucesso!'.format(sexo))
