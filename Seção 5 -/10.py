"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre 
seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura):
Homens: (72.7 * h) – 58
Mulheres: (62.1 * h) – 44.7
"""

h = float(input('Digite sua altura em metros: '))
s = input('Você é do sexo feminino ou masculino? ')
if s == 'masculino' :
	peso = (72.7 * h) - 58
if s == 'feminino' :
	peso = (62.1 * h) - 44.7
print(f'Seu peso ideal é de {peso:.2f}kg')
