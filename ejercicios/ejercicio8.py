#Escribe un programa en Python que tome una lista de números ingresados por el usuario y muestre la suma de los números pares.

numeros = input('ingrese lista de numeros separados por espacios: ').split();

numeros = map(int, numeros);

suma_pares = sum(num for num in numeros if num % 2 == 0);

print('la suma de los numeros pares es: ', suma_pares);