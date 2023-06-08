lista = ['cachorro', 'hamster', ['pato', 'galinha', 'porco'], 'gato']
print(lista[3][2])

def foo(a):

   return a + a + a

b = 1

foo(b)

foo(b)

foo(b)

print(b)

a = 0
for i in range(30):

    if a%2 == 0:
        a += 1
        continue
    else:
        if a%5 == 0:
            break
        else:
            a += 3
print(a)

import math
print(math.sqrt(36))

x = [2, 9, 1, 5]
i = 1
j = 2
i, x[i] = j*2 - x[j] **2, 0
print(x)

def f(n):
    if n < 3:
        return n-1
    else:
        return f(n-2) + f(n-1)
print (f(10))



numero1 = int(input('Informe o número de Processos: '))
numero2 = int(input('Informe o número de Juízes: '))
try:
    resultado = numero1 / numero2
    print("Há ",resultado, " processos a serem julgados por cada Juiz")
except ZeroDivisionError:
    print("Não é possível divisão por zero")
    
    
def foo(n):
    if n > 1:
        return n * foo(n - 1)
    return n
    
print(foo(4))
