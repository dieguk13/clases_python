# Escribe un programa en Python que tome dos listas de números ingresadas por el usuario y devuelva una nueva lista que contenga los números comunes a ambas listas.

lista1 = input('ingrese los numeros separados por espacios: ').split();

lista2 = input('ingrese los numeros separados por espacios: ').split();

lista1 = list(map(int, lista1)); 
lista2 = list(map(int, lista2)); 

comunes= [];

for numero in lista1:
    if numero in lista2:
        comunes.append(numero);
        
print('numeros comunes: ', comunes) 