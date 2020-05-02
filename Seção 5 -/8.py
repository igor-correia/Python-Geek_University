"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas 
e exiba na tela a média dessas notas. Uma nota válida deve ser obrigatoriamente 
entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve 
ser informado ao usuário e o programa termina.
"""

nota1 = float(input('qual a primeira nota? '))
nota2 = float(input('qual a segunda nota? '))
if nota1 >=0 and nota1 <=10:
    if nota2 >=0 and nota2 <=10:
    	media = (nota1 + nota2) / 2
    	print(f'a média das notas é: {media}')
	else:
    	print(f'{nota2} é uma nota inválida')
else:
    print(f'{nota1} é uma nota inválida')
