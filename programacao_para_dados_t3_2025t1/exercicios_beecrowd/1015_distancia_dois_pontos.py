# sem OO

import math

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'{distancia:.4f}')



# com OO

# definicao das classes

"""
>>> p = Ponto(3,4)
>>> p.x
3

>>> p = Ponto(3.0,4.0)
>>> p.y
4.0

>>> p1 = Ponto(3,0)
>>> p2 = Ponto(0,4)
>>> p1.distancia(p2)
5.0
"""
class Ponto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, outro_ponto):
        return math.sqrt((outro_ponto.x - self.x)**2 + (outro_ponto.y - self.y)**2)
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()        
        
# programa principal
x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

p1 = Ponto(x1, y1)
p2 = Ponto(x2, y2)

distancia = p1.distancia(p2)

print(f'{distancia:.4f}')

