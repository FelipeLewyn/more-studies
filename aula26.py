"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
condicao = False
passou_no_if = None

if condicao:
   passou_no_if = True
   print('faça algo')

else:
   print('Não faça algo')

if passou_no_if is None:
   print('Não faça algo')

else:
    print('passou no if')