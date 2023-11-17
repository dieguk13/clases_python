#Escribe un programa en Python que tome una lista de números ingresados por el usuario y los escriba en un archivo de texto, uno por línea.

numeros= input('ingrese lista de numeros separados por espacios: ').split()

with open('texto_5.txt', 'w') as archivo:
    for numero in numeros:
        archivo.write(numero + '\n');
        
print('los numeros ya han sido guardados');