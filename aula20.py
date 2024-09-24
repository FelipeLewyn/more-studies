"""
Interpolação básica de stringa
s - string
d e 1 - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Felipe'
preco = 100.012244365436
variavel = '%s,o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))