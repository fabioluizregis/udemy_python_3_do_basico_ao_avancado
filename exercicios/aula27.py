"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da string
"""

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[-4])

print(variavel[4:])
print(variavel[4:8])

print(len(variavel))
print(variavel[0:len(variavel):1]) # 1 quer dizer de quantos em quantos caracteres imprimir
print(variavel[0:len(variavel):2])

print(variavel[::-1])
print(variavel[-1:-10:-1])