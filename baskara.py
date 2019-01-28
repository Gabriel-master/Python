# # # # # # # # # # # # # #
# @author Gabriel Martins #
# Data: 28/01/2019        #
# Linguagem: Python       #
# # # # # # # # # # # # # #

import math

a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))

d = (b**2)-(4*a*c)

if d < 0:
    print("O delta não possui raiz negativa")
    exit()
else:
    d = math.sqrt(d)
    x1 = (-b + d)/(2 * a)
    x2 = (-b - d)/(2 * a)
print("X' = ",x1, "\n X'' = ",x2)



        
        
