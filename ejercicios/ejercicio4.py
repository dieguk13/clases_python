#Escribe un programa en Python que lea un archivo de texto y cuente la cantidad de palabras que contiene.

try:
    with open('texto1.txt', 'r') as archivo:
        contenido = archivo.read();
        palabras=contenido.split();
    print('la cantida de palabras es: ', len(palabras) )
    
except FileNotFoundError:
    print('el archivo no existe');