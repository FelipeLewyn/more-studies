"""
Faça um progama que peça ao usuário para digitar um número inteiro,
Informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro. 
"""
numero = input('Digite um numero inteiro: ')

numero_inteiro = int (numero) 

verificacao_impar_par = (numero_inteiro) % 2 

if verificacao_impar_par == 0:
    print('Esse número e par')

else:
    print('Este numero e impar')

"""
Faça um progama que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input('Que horas são? ')
int_hora = int(hora)

if int_hora == 0 or int_hora < 11:
    print('Bom dia')

elif int_hora == 12 or int_hora < 17:
    print('Boa tarde')

elif int_hora == 18 or int_hora < 23:
    print('Boa noite')
"""
Faça um progama que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 "Seu nome e muito grande".
"""
nome = input('Digite seu primeiro nome: ')
numero_de_letras = len(nome)

if numero_de_letras <= 4:
    print('Seu nome é curto')

elif numero_de_letras == 5 or numero_de_letras == 6:
    print('Seu nome é normal')

elif numero_de_letras > 6:
    print('Seu nome é muito grande')