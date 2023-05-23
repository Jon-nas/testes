a = ['10']
b = ['20']
c = ['30']

r = a+b+c
print(f'r={r}')

r1 = a*2+b*3+c*4
print(f'r1={r1}')



a = 1
b = 2
# troca de variáveis usando variável auxiliar ‘temp’
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla
a, b = b, a
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")