primeiro_valor = input ('digite um valor: ')
segundo_valor = input ('digite um segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor}' , 'é maior que' , f'{segundo_valor}')

elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor}' , 'é igual ao' , f'{segundo_valor}')

else :
    print(f'{primeiro_valor}' , ' é menor que ' , f'{segundo_valor}')