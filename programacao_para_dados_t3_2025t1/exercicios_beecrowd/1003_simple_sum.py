# Read two integer values, in this case, the variables A and B. After this, 
# calculate the sum between them and assign it to the variable SOMA. 
# Write the value of this variable.

# Input
# The input file contains 2 integer numbers.

# Output
# Print the message "SOMA" with all the capital letters, with a blank space 
# before and after the equal signal followed by the corresponding value to the 
# sum of A and B. Like all the problems, don't forget to print the end of line, 
# otherwise you will receive "Presentation Error"

# sem OO

A = int(input())
B = int(input())
SOMA = A + B
print(f'SOMA = {SOMA}')


# com OO

# classe
class Calculadora:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a + self.b


# programa principal
A = int(input())
B = int(input())
calc = Calculadora(A, B)
print(f'SOMA = {calc.soma()}')