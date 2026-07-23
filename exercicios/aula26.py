"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos a imprimir>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou =
Ex.: 0>-1--,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')

print(f'{1000.230987329047:.1f}')
print(f'{1000.230987329047:,.1f}')
print(f'{1000.230987329047:+,.1f}')
print(f'{-1000.230987329047:+,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')