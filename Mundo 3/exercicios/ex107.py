"""Crie um módulo chamado modulos.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

import modulos
n1 = float(input('digite o preço R$: '))
print(f'aumentando 10% de {n1} temos {modulos.aumentar(n1)}')
print(f'diminuindo 10% de {n1} temos {modulos.diminuir(n1)}')
print(f'o dobro de {n1} = {modulos.dobro(n1)}')
print(f'a metade de {n1} = {modulos.metade(n1)}')
