def Division (num1,num2):
    try:
        print(int(num1) / int(num2))
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except ValueError:
        print("Ingrese digitos validos: ")
