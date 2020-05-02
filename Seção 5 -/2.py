"""
Leia um número fornecido pelo usuário. 
Se esse número for positivo, calcule a raiz quadrada do número. 
Se o número for negativo mostre uma mensagem dizendo que o número é inválido.
"""

num1 = float(input('qual o número? '))
if num1 >= 0:
    num2 = num1 ** (1/2)
    print(f'a raiz de {num1} é {num2}')
else:
    print(f'esse número é inválido')
