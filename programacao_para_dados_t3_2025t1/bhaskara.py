class Bhaskara:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f'{self.a}x2 + {self.b}x + {self.c} = 0'
    
    def calcula_delta(self):
        return self.b**2 - 4 * self.a * self.c
    
    def verifica_delta(self):
        if self.calcula_delta() < 0:
            return False
        else:
            return True
    
    def calcula_raizes(self):
        delta = self.calcula_delta()
        if self.verifica_delta():
            x1 = (-self.b + delta**0.5) / (2 * self.a)
            x2 = (-self.b - delta**0.5) / (2 * self.a)
            return [x1, x2]
        else:
            return []
        
calc = Bhaskara(1, -6 , 9)
calc.calcula_raizes()