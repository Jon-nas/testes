"""def valorMin(lista):
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



escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)



def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)



def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')



def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')



def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')





def entradaDados():
    coeficiente=quantidade=eval(input('Digite o valor do coeficiente: '))
    return coeficiente

def calcDelta(a, b, c):
    delta=b*b-4*a*c
    return delta

def calculaRaizes(a, b, c, delta):
    if(delta<0):
        resultado='A equação não possui raizes nos números reais'
    elif(delta ==0):
        x=-b/(2*a)
        resultado = f'A equação possua paenas a raiz: {x}'
    else:
        x1=(-b-(delta))/(2*a)
        x2=(-b+(delta))/(2*a)
        resultado=f'A questão possui as raizes: {x1}, {x2}'
        return resultado

a=entradaDados()
b=entradaDados()
c=entradaDados()

delta=calcDelta(a, b, c)

resultado=calculaRaizes(a, b, c, delta)
print(resultado)"""


#import dos pacotes necessários
"""from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')"""



"""import time

x = time.time()
print(f'Local time: {time.ctime(x)}')"""



"""while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entre com um número válido.")"""
        
        


def dividir(x, y):
    try:
        resultado = x / y
        print("A resposta é: ", resultado)
    except ZeroDivisionError:
        print("Divisão por zero")
        
dividir (3, 0)
dividir (3, 2)

import math
print(math.sqrt(36))


def foo(n):
    if n > 1:
        return n * foo(n-1)
    return n

print(foo(4))



a = 0
for i in range(30):
    if a%2==0:
        a+=1
        continue
    else:
        if a%5==0:
            break
        else:
            a+=3
            
print(a)