"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: 
o número digitado ao quadrado e a raiz quadrada do numero digitado
"""
num1 = float(input('qual o número? '))
if num1 >= 0:
    num2 = num1 ** (1/2)
    print(f'a raiz de {num1} é {num2}')
    num3 = num1 ** 2
    print(f'{num1} ao quadrado é {num3}')

