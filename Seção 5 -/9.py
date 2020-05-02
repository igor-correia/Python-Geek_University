"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido,
caso contrário imprima: Empréstimo concedido.
"""

salario = float(input('Digite seu salário: '))
prestacao = float(input('Digite o valor da prestação: '))
limite = salario * 0.2
if prestacao > limite:
	print('Empréstimo não concedido')
else:
	print('Empréstimo concedido')
