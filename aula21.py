"""
Formataçao basica de string  
s - string
d - int
f - float 
 <número de digitos>f
 x ou X - Hexadecimal 
 (Caractere) (><^) (quantidade)
 > - Esquerda 
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou -
 Ex.: 0>-100, .1f
 Conversion flags - !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{-10101.03909434900:0=+10.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')