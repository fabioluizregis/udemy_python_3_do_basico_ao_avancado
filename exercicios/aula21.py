# Operadores lógicos
# and (e), or (ou), not (não)
# and: todas as expressões precisam ser verdadeiras para retornar True
# or: apenas uma expressão precisa ser verdadeira para retornar True
# not: inverte o valor lógico da expressão

entrada = input('[E]ntrar, [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


print(True and True)
print(True and False)
print(False and False)
print()
print(True or True)
print(True or False)
print(False or False)
print()
print(not True)
print(not False)