# classe
class Calculadora:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a + self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def media_ponderada(self, p1, p2):
        return (self.a*p1 + self.b*p2) / (p1 + p2)


a = float(input())
b = float(input())
print(f'MEDIA = {Calculadora(a,b).media_ponderada(3.5,7.5):.5f}')