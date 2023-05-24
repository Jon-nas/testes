def valorMin(lista):
    minimo = lista [0]
    for element in lista:
        if (element < minimo):
            minimo = element
    return minimo

lista = [2, 10, 3, 1, 4, 5]
menor = valorMin(lista)
print('O menor elemento da lista é: [{}]'. format(menor))



def par(n):
    r = (n%2==0)
    return r

def somaPar (lst):
    soma = 0
    for num in lst:
        if (par(num)):
            soma = soma + num
    return soma
        
lista = [10, 2, 5, 7, 6, 3]
soma = somaPar(lista)
print(f'A soma dos elementos pares da lista é: {soma}')



numero = 5
def fatorialIterativo(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f
print(f'O fatorial de {numero} é: {fatorialIterativo(numero)}')

#resposta2
def fatorialRecusivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorialRecusivo(n-1)
print(f'O fatorial de {numero} é: {fatorialRecusivo(numero)}')



numero = 7
def primo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%i==0):
            return False
        i=i-1
    return True

def resultado1(numero, resultado):
    mensagem = f'O número {numero} não é primo'
    if(resultado):
        mensagem = f'O número {numero} é primo'
    return mensagem

resultado = primo(numero)
msg = resultado1(numero, resultado)
print(msg)