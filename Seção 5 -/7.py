"""
Faça um programa que receba dois números e mostre qual deles é o maior,
se por acaso eles forem iguais, imprima a mensagem números iguais
"""

num1 = input('qual o primeiro número? ')
num2 = input('qual o segundo número? ')
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print(f'{num1} e {num2} são iguais')
