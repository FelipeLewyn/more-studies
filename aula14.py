# if / elif      / else
# se / se nao se / se nao

entrada = input('você quer "entrar" ou "sair"? ')

if entrada == "entrar": # o if pode viver sozinho
    print('você entrou no sistema')

# bloco if tudo que vai ser executado pela condição deve estar aqui
elif entrada == "sair": # pode ser colocado varias vezes
    print('você saiu do sistema')

# bloco elif tudo que vai ser executado pela condição deve estar aqui
else : # sempre o ultimo na ser colocado 
    print('você não digitou nem entrar e nem sair')

# bloco else tudo que vai ser executado pela condição deve estar aqui

print('\n')
print('fora dos blocos')