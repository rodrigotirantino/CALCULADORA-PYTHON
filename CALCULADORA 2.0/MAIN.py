import re
while True:
    operacion = input("Que operación desea realizar?. Suma, resta, division, multiplicacion: ")
    operacion = str(operacion)

    validacion_op = re.findall("suma|resta|division|multiplicacion",operacion)

    if not validacion_op:
        print("Ingrese una operación valida")
    else:
        break
    print(f"Operación seleccionada: {operacion}")
    
operacion = operacion.lower()

while True:
    try:
        num1 = int(input("Ingrese el primer número para operar: "))
        num2 = int(input("Ingrese el segundo número para operar: "))
    except ValueError:
        print("Ingrese solo números enteros.")
    else:
        break

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
