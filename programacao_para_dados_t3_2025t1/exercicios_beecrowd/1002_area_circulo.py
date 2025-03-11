# jeito simples sem orientação a objetos

raio = float(input())
area = 3.14159 * raio * raio
print(f'A={area:.4f}')


# ======== 
# com orientação a objetos
# ========

# classe
class Circle():
    
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio * self.raio

# programa principal    
raio = float(input())
circle = Circle(raio)
area = circle.area()
print(f'A={area:.4f}')