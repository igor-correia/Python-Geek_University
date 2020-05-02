"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. 
Do contrário, imprima o número ao quadrado.
"""

num1 = float(input('qual o número? '))
if num1 >= 0:
    num2 = num1 ** (1/2)
    print(f'a raiz de {num1} é {num2}')
else:
    num2 = num1 ** 2
    print(f'{num1} ao quadrado é {num2}')
