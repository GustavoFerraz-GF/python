#oposto = float(input("Comprimento do cateto oposto: "))
#adjacente = float(input("comprimento do cateto adjacente: "))
#hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
#print("A hipotenusa vai medir {:.2f}.".format(hipotenusa))

import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print(("A hipotenusa vai medir {:.2f}.".format(hi)))