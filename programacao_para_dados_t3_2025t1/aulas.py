# =============================================================================
#   AULA 02
# =============================================================================


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




# =============================================================================
#   AULA 03
# =============================================================================


###
#
#   Acessibilidade de Atributos em Python
#   
#   O sinal de sublinhado _ antes de um item indica que ele é privado.
#   A sinalização indica que em uma manutenção futura o item pode ser
#   alterado ou removido.
#
###

class Bhaskara:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f'{self.a}x2 + {self.b}x + {self.c} = 0'
    
    def _calcula_delta(self):
        # método privado
        return self.b**2 - 4 * self.a * self.c
    
    def _verifica_delta(self):
        # método privado
        if self.calcula_delta() < 0:
            return False
        else:
            return True
    
    def calcula_raizes(self):
        delta = self._calcula_delta()
        if self._verifica_delta():
            x1 = (-self.b + delta**0.5) / (2 * self.a)
            x2 = (-self.b - delta**0.5) / (2 * self.a)
            return [x1, x2]
        else:
            return []
        
        
###
#
#   Sobrecarga de métodos
#   
#   Um método pode ser definido com um mesmo nome, porém com parâmetros
#   diferentes.
#   A sobrecarga auxilia a reduzir a complexidade de uma interface e o 
#   quantidade de nomes de métodos para memorizar
#
###

class Cashier:
    def __init__(self):
        self.total = 0
    
    def add(self, value, times = 1):
        # este método está em sobrecarga
        # pode receber 1 parâmetro ou 2
        self.total += value * times
        
cashier01 = Cashier()
cashier01.add(10)            # com apenas um parâmetro
cashier01.add(10, 2)         # com dois parâmetros

print(cashier01.total)


###
#
#   Sobrecarga de métodos com nomes iguais porém tipos de parametros diferentes
#   Em determinados momentos, quero usar int, ou list, ou float, etc
#
###

class Cashier:
    def __init__(self):
        self.total = 0
    
    def add(self, value, times = 1):
        # este método está em sobrecarga
        # pode receber 1 parâmetro ou 2
        
        # verifica se o parâmetro value é uma lista
        if isinstance(value, list):
            self.total += sum(value) * times
        else:
            self.total += value * times
        return self.total
            
cashier02 = Cashier()
cashier02.add(10)            # com apenas um parâmetro
cashier02.add(10, 2)         # com dois parâmetros
cashier02.add([10, 20, 30])  # com uma lista


###
#
#   Operador Polimórfico
#   
#   Um operador pode ser usado com diferentes tipos de parâmetros. Por exemplo,
#   o operador + pode ser usado com inteiros, strings, listas, etc
#
###


###
#
#   Classe abstrata
#
#   Classe que serve para determinar o comportamento (atributos e métodos) esperados
#   por suas subclasses. Apresenta uma implementação incompleta.
#   Utiliza o conceito de HERANÇA em que uma subclasse herda a definição da sua
#   super classe. Permite ampliar uma implementação existente sem alterar a 
#   implementação original.
#
#
#   Vantagens do Polimorfismo
#
#   Classes novas oferecem comportamento compatível com classes antigas, desde que 
#   se mantenham a mesma interface.
#   Simplifica a evolução de sistemas que têm por base um tipo
#   que é derivado durante a evolução do sistema.   
#
###


import math

# primeiro, desenvolvemos o círculo
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2

c1 = Circle(1.0)
c1.area()

# outro programador, em outro dia, desenvolve o triangulo
# porém acaba usando outro nome para o método da área
class Triangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return  self.a * self.b / 2

t1 = Triangle(3, 4)
t1.get_area()

# em outro momento, gostaríamos de calcular as áreas de círculos e triangulos

shapes = [Circle(1.0), Triangle(3, 4)]

for shape in shapes:
    print(shape.area())
    
# porém dá erro, porque o triangulo usa um nome diferente do círculo
# para o método da área

# então, usamos a sobrecarga do método área

class Triangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b / 2
    
# agora, usaremos a classe abstrata para garantir que todas as próximas formas
# utilizarão a sobrecarga do método area

class Shape:
    def area(self):
        pass
    
    


# =============================================================================
#   AULA 04
# =============================================================================


###
#
#   Qualidade de Software
# 
#   A orientaão a objetos nos auxilia a aumentar a qualidade dos nossos programas
#   
#   Cinco Perspectivas de Qualidade:
#   - Transcedental: a qualidade é um ideal, que sempre precisa ser melhorada
#   - Manufatura: favorece o produtor e a entrega do produto (mais fácil e rápido)
#   - Produto: qualidade interna. Perfeccionismo em fazer o produto perfeito.
#   - Usuário: atende as tarefas do usuário
#   - Valor: o que pode ser feit no orçamento e prazo
# 
#   ISO 25000: Qualidade de Software
#   - Funtional suitability
#   - Reliability
#   - Performance Efficiency
#   - Operability
#   - Security
#   - Compatibility
#   - Maintainability
#   - Portability
#
#   Módulos e Pacotes
#   - Módulo: um arquivo Python
#   - Pacote: uma pasta com módulos
#
###


# criei o arquivo (módulo) fibonacci.py
import fibonacci as fib
fib.fibonacci(4)


###
#
#   Protocolos e operadores
#   Um protocolo pode ser entendido como uma lista de métodos
#
#   Como utilizar um protocolo
#   Considere uma função que espera que um objeto apresente um método específico
#   A maneira mais simples de garantir a presença de um método em um objeto, 
#   seria inficar uma classe para o tipo do objeto. Porém, em alguns casos,
#   um mesmo método pode aparecer em diferentes classes. A função necessita
#   que o método esteja presente no objeto, porém a classe não é importante.
#
###


#   Exemplo Duck Typing

#   Crio uma classe Duck
class Duck:
    def talk(self):
        print("Quack")

#   Crio uma funçãp que espera que o objeto contenha o método talk        
def make_talk(e: Duck):     #   Sugiro que o objeto seja classe Duck
    e.talk()
    
#   Crio uma classe Dog
class Dog:
    def talk(self):
        print("Woof")    

class Mute:
    def walk(self):
        pass

#   Crio os objetos    
duck = Duck()
dog = Dog()
mute = Mute()

#   Funciona conforme o esperado para o Duck
make_talk(duck)

#   Mesmo o objeto não tendo a classe recomendada, ele tem o método talk
#   e funciona normalmente
make_talk(dog)

#   Porém, se eu chamo um objeto que não tem o método talk, o programa dá erro
#   e trava

make_talk(mute)

#   Para evitar esses erros e travamentos do programa, usam-se os protocolos

#   Exemplo Protocolos

from typing import Protocol

class Talker(Protocol):
    def talk(self):
        pass

def make_talk(e: Talker):
    e.talk()

duck = Duck()
dog = Dog()

duck = make_talk(duck)
dog = make_talk(dog)


###
#
#   Métodos Especiais
#   Métodos que iniciam com "__"
#   
#   __init__: construtor
#   __str__: representa o objeto
#   __len__: retorna o tamanho
#   __add__: retorna a soma dos objetos
#   __eq__: define como trabalhamos a igualdade entre os objetos
#
###


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, outro_ponto):
        return Ponto(self.x + outro_ponto.x, self.y + outro_ponto.y)
    
    def __eq__(self, outro_ponto):
        return self.x == outro_ponto.x and self.y == outro_ponto.y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
p1 = Ponto(1,1)
p2 = Ponto(2,2)
p3 = p1 + p2
p4 = Ponto(3,3)
p5 = Ponto(1,1)
print(p3)
print(p3==p4)
print(p3==p5)



###
#
#   Tratamento de erros e excepções
#
#   Erros: erros que impedem a execução do programa
#   Exceções: erros que podem ocorrer durante a execução do programa
#   
#   Comando raise
#   O comando raise sinaliza que uma exceção ocorreu
#   A execução do programa é interrompida
#   
#   Exceções predefinidas
#   - ValueError
#   - TypeError
#   - ZeroDivisionError
#   - IndexError
#
###


#   Verificar condições de entrada

def media(p,t):
    if p < 0.0 or p > 10.0:
        raise ValueError("A nota da prova deve estar entre 0.0 e 10.0")
    if t < 0.0 or t > 10.0:
        raise ValueError("A nota do trabalho deve estar entre 0.0 e 10.0")
    return (2.0*p+t) / 3

media (7.0,7.0)
media (7.0,70)

### 
# 
#   Dinâmica
# 
#   Escreva uma classe Ponto que verifica se a comparação é sempre realizada 
#   com outro objeto da classe Ponto. Indique uma exceção do tipo TypeError 
#   caso o tipo seja 
#
###

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, outro_ponto):
        if isinstance(outro_ponto, Ponto):
            return Ponto(self.x + outro_ponto.x, self.y + outro_ponto.y)
        else:
            raise TypeError("A soma deve ser feita com outro objeto da classe Ponto")
    
    def __eq__(self, outro_ponto):
        if isinstance(outro_ponto, Ponto):
            return self.x == outro_ponto.x and self.y == outro_ponto.y
        else:
            raise TypeError("A comparação deve ser feita com outro objeto da classe Ponto")
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
p1 = Ponto(1,1)
p2 = Ponto(2,2)
p3 = 3
p4 = p1 + p2
p5 = p1 + p3


###
#
#   try/except
#
###

try:
    n1 = 7
    n2 = 7
    m = media(n1,n2)
    print(m)
except ValueError:
    print('Opa! Erro!')
    
try:
    n1 = 7
    n2 = 70
    m = media(n1,n2)
    print(m)
except ValueError:
    print('Opa, tivemos um erro!')
    

### Continuando dinamica do Ponto

try:
    p1 = Ponto(1,1)
    p2 = "hello"
    if p1 == p2:
        print('Iguais')
except TypeError:
    print('Ocorreu um erro durante a execução')
    


###
#
#   Dinâmica: exemplo de pacote
#   Exemplo de Pacote: Índice de Inteligibilidade de Flesch
#
###




# =============================================================================
#   AULA 05
# =============================================================================


### Criando seu próprio repositório

### 
# 
# Gerador de números aleatórios
# Escreva um programa em Python que simule a jogada de dois 
# dados de seis faces.
# O programa deve apresentar todos os lançamentos.
# O programa deve indicar quantas vezes os dados lançados
# formaram 12 pontos
#
###

# Jeito simples e fácil de resolver
import random

i = 0
while i < 10:
    primeiro_dado = random.randrange(1,7)
    segundo_dado = random.randrange(1,7)
    print(primeiro_dado, segundo_dado)
    if primeiro_dado + segundo_dado == 12:
        print('12 pontos')
    i += 1

# Agora, utilizando POO

d1 = random.Random()
d2 = random.Random()

jogadas = []
duplo_seis = 0

for i in range(10):
    primeiro_dado = d1.randrange(1,7)
    segundo_dado = d2.randrange(1,7)
    jogadas.append((primeiro_dado, segundo_dado))
    # print(primeiro_dado, segundo_dado)
    if primeiro_dado + segundo_dado == 12:
        duplo_seis += 1
        print('12 pontos')
    i += 1

print(jogadas)
print(duplo_seis)


### 
# 
#   Estatísticas de sinalização
#   Escreva um programa em Python que leia um arquivo com 
#   registro de obras de sinalização.
#   O programa deve apresentar a obra com a implantação mais
#   antiga.
#   O programa deve apresentar registros que não apresentam
#   latitude e longitude.
#
###

f = open('sinalizacao.csv')

dados = []

obra_mais_antiga = ''

for linha in f:
    print(linha.strip().split(';'))
    print(linha.strip().split(';')[4])
    if obra_mais_antiga == '' or obra_mais_antiga > linha.strip().split(';')[4]:
        obra_mais_antiga = linha.strip().split(';')[4]
    dados.append(linha.strip().split(';'))

print(obra_mais_antiga)
