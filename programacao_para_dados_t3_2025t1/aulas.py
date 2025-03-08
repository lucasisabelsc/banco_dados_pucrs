# Primeira Classe
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f'{self.name} recebe R$ {self.salary:.2f}'
    
    def proporcional(self, days):
        aux = self.salary / 30 * days
        return f'{aux:.2f}'




    
# Usando a classe
joao = Employee('João', 1000)
print(joao.name)
print(str(joao))
print(joao.proporcional(25))





###
#
#   Inspecionando objetos
#
###

type(joao)
id(joao)
help(joao)
dir(joao)
isinstance(joao, Employee)




###
#
#   Exercício 1001 - BeeCrowds
#
#   Leia 2 valores inteiros e armazena-los nas variáveis a e b. Efetue a soma
#   de a e b, atribuindo o seu resultado na variável soma. Imprima a variável
#   soma.
#
###


# Sem Orientação a Objetos

a = int(input())
b = int(input())
soma = a + b
print(f'VALOR A PAGAR: R$ {soma:.2f}')


# Com Orientação a Objetos
# A classe tem dois atributos, a e b
# O método soma() tem dois parâmetros, a e b
# O método imprime() tem um parâmetro, soma

# Definindo a Classe
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b
    
    def __str__(self):
        return f'{self.a} + {self.b} = {self.soma()}'
    
# Programa Principal
a = int(input())
b = int(input())
calc = Calculadora(a, b)
x = calc.soma()
print(f'Valor da Soma {x:.2f}')
str(calc)


