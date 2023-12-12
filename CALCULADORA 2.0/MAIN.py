
operacion = input("Que operación desea realizar: ")
num1 = int(input("Ingrese el primer numero para operar: "))
num2 = int(input("Ingrese el segundo numero para operar: "))

operacion = operacion.lower()

from SUMA import Suma
from RESTA import Resta
from MULTIPLICACION import Multiplicacion
from DIVISION import Division

if operacion == "suma":
    Suma(num1,num2)
    
elif operacion == "resta":
    Resta(num1,num2)
    
elif operacion == "multiplicacion":
    Multiplicacion(num1,num2)
    
elif operacion == "division":
    Division(num1,num2)
    
else:
     print("Operacion invalida")