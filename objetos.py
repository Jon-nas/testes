"""class pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
        
    def set_nome(self, nome):
        self.nome=nome
        
    def set_ender(self, ender):
        self.ender=ender
        
    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
pessoa1 = pessoa("Mary", "rua 01234")
pessoa2 = pessoa("Peter", "rua 56789")

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')




class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def imprimir(self):
        print(self.nome, "Tem ", self.idade, "ano(s)")
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade
        
p = pessoa("Ana", 25)
p.imprimir()




class profissional(pessoa):  #Herança
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super() .imprimir()
        print('\t e trabalha com ', self.profissao)
    
p = profissional("Ana", 25, "Balconista")  #Polimorfismo
p.imprimir()




class salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus
        
def salarioAnual(self):
    return (self.base*12)+self.bonus

class empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salarioAgregado = salario        #Agregação
    def salarioTotal(self):
        return self.salarioAgregado.salarioAnual()
    
salario = salario(10000, 700)
emp = empregado('Musashi', 46, salario)
print(emp.salarioTotal())



#Methode de class e estática
from datetime import date
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def anoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    
    @staticmethod
    def maiorIdade(idade):
        return idade >= 18
    
pessoa1 = pessoa('Mary', 26)
pessoa2 = pessoa.anoNascimento('Ana', 2006)

print(pessoa1.idade)
print(pessoa2.idade)

print(pessoa.maiorIdade(17))




#Construtores e self
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
def main():
    c1 = Conta(1,1,"Peter",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")
    

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__": 
    main()
    
    
    

class A():
    def f(self):
        print("foo")


def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__": 
    main()
    
    
    
    
#Métodos
def __depositar__(self,valor):
     self.saldo += valor
     
class Conta:
    def __init__(self, numero, cpf,           nomeTitular, saldo):
         self.numero = numero
         self.cpf = cpf
         self.nomeTitular = nomeTitular
         self.saldo = saldo
    def depositar(self, valor):
         self.saldo += valor
    def sacar(self, valor):
         self.saldo -= valor
         
    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")     

def main():
    c1 = Conta(1,1,"Peter",0)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__": 
    main()
    
    
    
    
#Métodos com retorno
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")     
        
def main():
    c1 = Conta(1,1,"Peter",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")
    

if __name__ == "__main__": 
    main()

    
    
    
    
#Referência entre objetos na memória
class Conta:
    def __init__(self, numero, cpf,    nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
        return True
    def gerarextrato(self):
        print(f"numero:{self.numero}\n     cpf:{self.cpf}\nsaldo:{self.saldo}")
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")
        
conta1 = Conta(1, 123,'Peter',0)
conta2 = Conta(3, 456,'Mary',0)
conta1.depositar(1000)
conta1.transfereValor(conta2,500)
print(conta1.saldo)
print(conta2.saldo)"""
        


class carro(object):
    def faleComigo(self):
        print('Sou um carro')
        
class fusca(carro):
    def faleComUmFusca(self):
        print('Sou um fusca')
        
x = carro()
y = fusca()

x.faleComigo()
y.faleComigo()


#Exercícios
veiculos = ['avião', 'carro', 'navio', 'ônibus']
veiculos_Upercase = [veiculos.upper() for veiculos in veiculos] #Minha resposta
print(veiculos_Upercase)

f_maiuscula = lambda x: str.upper(x)  #Resposta correta
nomesMaiusculos = list(map(f_maiuscula, veiculos))
print(f'nomes maiusculos = {nomesMaiusculos}')



lista = [0, 1, 1, 2, 3, 5, 8 , 13, 21, 34]
listaPar = [item for item in lista if item % 2 == 0]  #Minha resposta
print(listaPar)

fTesteParidade = lambda x: x % 2 == 0  #Resposta correta
print(f'teste de fTesteParidade(5) = {fTesteParidade(5)}')
pares = list(filter(fTesteParidade, lista))
print(f'lista de números pares = {pares}')



lista_números = [9.56783, 7.57568, 3.00914, 6.2321] 
lista_precisao = [2, 2, 3, 3]
listaArredondada = [round(item, precisao) for item, precisao in zip(lista_números, lista_precisao)]  #Minha resposta
print(listaArredondada)

arreondamento = lambda x, y: round(x, y) #Resposta correta
resultado = list(map(arreondamento, lista_números, lista_precisao))
print(resultado)



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = sum([item for item in numeros])  #Minha resposta
print(soma)

from functools import reduce  #Resposta correta
f_soma = lambda x, y: x + y
resultado = reduce(f_soma, numeros)
print(resultado)


#inicie a execução de uma thread, cloque ela para esperar 2 segundos e informe o inicio e o final da exução da thread.

import threading  #Minha resposta
import time

def fThread():
    print('Inicio da thread')
    time.sleep(2)
    print('Fim da thread')
    
thread = threading.Thread(target=fThread)
thread.start()
thread.join()

from time import sleep   #Resposta correta
from threading import Thread
def tarefa(tempo_espera, mensagem):
    print(f'\nInicializando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')
thread = Thread(target=tarefa, args=(2, 'Thread em execução'))
thread.start()
print('\nAguardando pela execução da thread...')
thread.join()
print('A execução foi concluida!')




# inicie a execução de duas threads, cloque a primeira e a segunda thread para esperar,
# respectivamente 3 e 2 segundos, informe o inicio e o final da exução da thread.
import threading  #Minha resposta
import time

def fThread1():
    print('Inicio da thread 1.')
    time.sleep(3)
    print('Fim da thread 1!')
    
def fThread2():
    print('Inicio da thread 2.')
    time.sleep(2)
    print('Fim da thread 2!')
    
fThread1 = threading.Thread(target=fThread1)
fThread2 = threading.Thread(target=fThread2)

fThread1.start()
fThread2.start()


from time import sleep   #Resposta correta
from threading import Thread
def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciandoa a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')
    
t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join()
t2.join()
print('A execuçaão foi concluida')




#inicie a execução de duas threads, a primeira deve calcular o cubo de um número,
# a segunda thread deve calcular o quadrado de um número. Coloque a primeira e a segunda thread
# para esperar respectivamente 3 e 2 segundos, informe a ordem da exução das threads.
import threading  #Minha resposta
import time

def cube(num):
    time.sleep(3)
    print(f"O cubo de {num} é {num**3}")

def square(num):
    time.sleep(2)
    print(f"O quadrado de {num} é {num**2}")

t1 = threading.Thread(target=cube, args=(3,))
t2 = threading.Thread(target=square, args=(4,))

t1.start()
t2.start()

t1.join()
t2.join()


from time import sleep   #Resposta correta
from threading import Thread
def calcular_cubo(num, tempo_espera):
    print(f'\nCubo: {num * num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_cubo')
    
def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num * num}')
    sleep(tempo_espera)
    print('Conclusão da função calcular_quadrado')
    
tr1 = Thread(target=calcular_quadrado, args=(5, 3))
tr2 = Thread(target=calcular_cubo, args=(5, 2))
tr1.start()
tr2.start()
tr1.join()
tr2.join()
print('A execução foi concluida!')