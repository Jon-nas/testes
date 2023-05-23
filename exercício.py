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



num = 10   # Entrada e saída de dados
print(num)

nome = input('Entre com seu nome: ')
print(nome)

numero = eval(input('Entre com um inteiro: '))
numero = numero + 2
print(numero)

peso = eval(input('Entre com o seu peso: '))
altura = eval(input('Entre com sua altura: '))
imc = peso/(altura**2)
print('IMC = ', imc)

def foo(a):
    return a+a+a

b = 1

foo(b)
foo(b)
foo(b)

print(b)