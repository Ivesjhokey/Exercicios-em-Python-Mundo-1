"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""


from utilidadesCeV import moeda

n1 = int(input('digite um valor: '))
print(moeda.resumo(n1, 10, 10))
