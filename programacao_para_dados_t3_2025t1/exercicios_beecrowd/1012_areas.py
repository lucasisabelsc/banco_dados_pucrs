###
#   Com Orientacão a Objetos
###


class Shape:
    def area():
        pass
    
    
class Circle(Shape):
    
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14159 * self.raio * self.raio
    
    
class Triangle(Shape):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return ( self.base * self.altura ) / 2


class Trapezoid(Shape):
    
    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ( self.base_maior + self.base_menor ) * self.altura / 2


class Rectangle(Shape):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    

class Square(Shape):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    
# programa principal

a, b, c = [float(x) for x in input().split()]

triangulo = Triangle(a, c)

print(f"TRIANGULO: {triangulo.area():.3f}")