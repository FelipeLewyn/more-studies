#Operadores logicos
# and (e) or (ou) not (não)
# and - Todas condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' false 
# Também existe tipo Nome que não valor 
# usado para representar um não valor

entrada = input ('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'

if entrada == 'E' or entrada =='e' and senha_digitada == senha_permitida :
    print('Entrar')
else:
    print('Sair')
   
print('\n')

# Avaliação de curto circuito
# O operador  or faz o que o if faz so que em uma unica linha
senha = input('senha: ') or 'sem senha'
print(senha)
