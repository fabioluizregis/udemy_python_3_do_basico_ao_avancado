a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={:.2f}'.format(a, b, c)  # Pega os valores na ordem que aparecem no format

print(formato)

formato2 = 'a={1} b={0} c={2:.2f}'.format(a, b, c) # Pega os valores pelo índice

print(formato2)