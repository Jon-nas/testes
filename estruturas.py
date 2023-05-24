#resolução
a = 10
b = 20

if(a>b):
    maior = a
else:
    maior = b
print(f'O maior número é: {maior}')


#resolução2
maior = a
if(b>maior):
    maior = b
print(f'O maior número é: {maior}')


if(a%2==0):
    a = "par"
else:
    a = "Impar"
print(f"O valor de a é: {a}")


nota = 8.5

if (nota>=7.0):
    aluno = 'aprovado'
elif (nota<=5.0):
    aluno = 'recuperação'
else:
    aluno = 'reprovado'
print(f'O estudante está: {aluno}')



valorUnidade = 10
desconto10 = 0.1
desconto20 = 0.2
quantidade = eval(input('Digite a quantidade que vai comprar: '))
if (quantidade <= 10 ):
    valor = valorUnidade*quantidade
elif(quantidade <= 20):
    valor = valorUnidade*quantidade*(1-desconto10)
else:
    valor = valorUnidade*quantidade*(1-desconto20)
print(f'O valor final da compra é: {valor}')



lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0
for i in range(n):
    if(lista[i]%2==0):
        soma = soma + lista[i]
print(f'A soma dos elementos pares é: {soma}')


#outra resposta
lista = [10, 2, 5, 7, 6, 3]
soma = 0
for num in lista:
    if(num%2==0):
        soma = soma + num
print(f'O somatório dos elementos pares é: {soma}')


for item in range(2, 9, 3):
    print(item)



nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra)




nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)