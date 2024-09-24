"""
Introdoção ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro tentar executar
"""

numero_str = input(
    'Vou dobrar o número que você digitar: ')

try:
    numero_float = float (numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('isso não é um número')

# if numero_str.isdigit():
#   numero_float = float (numero_str)
#   print(f'O dobro de {numero_str} é {numero_foat * 2})
# else:
#  print('isso não é um número')
