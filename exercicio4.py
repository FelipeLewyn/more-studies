"""
Exercício
Peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não)
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome: {nome}')
    print(f'Seu nome invertido: {nome[::-1]}')
    print(f'Seu nome não tem a b c: {'a b c' not in nome}' )
    print(f'Seu nome contém: {len(nome)} letras')
    print(f'A primeira letra do seu nome e: {nome[0]}')
    print(f'A última letra do seu nome: {nome[::-10]}')
else:
    print('Desculpe, você deixou um ou todos os campos vazios.')