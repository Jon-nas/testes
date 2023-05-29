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