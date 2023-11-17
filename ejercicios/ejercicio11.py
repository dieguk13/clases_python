# Escribe un programa en Python que tome una lista de palabras ingresadas por el usuario y devuelva una nueva lista con las palabras en mayúsculas.

palabras = input('ingrese una lista de palabras separadas: ').split();

mayusculas = list(map(lambda palabra:palabra.upper(), palabras));
print('palabras en mayuscula: ', mayusculas);
