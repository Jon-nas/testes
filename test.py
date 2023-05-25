print ('Olá, mundo!')

x = 5
print (x, type(x))

#print(dir(int))  ou help(int)

a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)


x = 10
print(x)



def multiplicador(numero):
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {a}")
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")



def multiplicador(numero):
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")



def multiplicador(numero):
        global a # todas as referências à variável a são para a global
        a = 2      # a global será alterado
        print(f"Dentro da função,  variável  vale: {a}")
        return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável b vale: {b}")
print(f"Fora da função, a variável a vale: {a}")



def func():
    x = 1
    print(x)

x = 10
func()
print(x)


print(type(1_000_000))

print(type(50.0))
x = 50.0
y = 50,0
print(x)
print(y)

print(type(2+3+1))
print(type(2+3+1.0)) #apenas um opeando float torna o resultado float

print (2**3)
print (type(2**3))
print (type(2.0**3))

x = 5/2
print(x) #Diferentemente de outras linguagens, como C, a divisão de dois números inteiros não necessariamente tem resultado inteiro

#Para obter o quociente inteiro e resto, quando dois inteiros são divididos, é necessário utilizar os operadores // e %, respectivamente. Ao dividir 21 por 2, temos quociente 10 e resto 1

print(2 < 3) #tipo bool
print(2 > 3)
print(not(2 < 3)) 



def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)