# classe
class Calculadora:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a + self.b
    
    def multiplicacao(self):
        return self.a * self.b


a = int(input())
b = int(input())
calc = Calculadora(a, b)
print(f'PROD = {calc.multiplicacao()}')


