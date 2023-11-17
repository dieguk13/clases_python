# Crear un módulo en Python llamado "operaciones_matematicas" que contenga funciones para realizar diferentes operaciones matemáticas básicas. El módulo debe ser utilizado en un programa principal donde se invoquen las funciones para realizar cálculos(suma, resta, multiplicación, división).

import operaciones_matematicas

numero1 = int(input('ingrese el numero 1: '));
numero2 = int(input('ingrese el numero 2: '));

print('Suma: ', operaciones_matematicas.suma(numero1, numero2));
print('Resta: ', operaciones_matematicas.resta(numero1, numero2));
print('Multiplicacion: ', operaciones_matematicas.multiplicacion(numero1, numero2));
print('Division: ', operaciones_matematicas.division(numero1, numero2));
print('Division con Exepcion: ', operaciones_matematicas(numero1, numero2));