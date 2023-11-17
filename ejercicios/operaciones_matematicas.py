def suma(num1, num2):
    return num1 + num2;

def resta(num1, num2):
    return num1 - num2;

def multiplicacion(num1, num2):
    return num1 * num2;

def division(num1, num2):
    if num1 != num2:
        return num1 / num2;
    else:
        return 'Error no se puede dividir entre cero';
    
def divisionException(num1, num2):
    try:
        return num1/num2;
    except ZeroDivisionError:
        return'Error: no se puede dividir entre cero'