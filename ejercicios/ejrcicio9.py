# tome una lista de nombres ingresados por el usuario y los ordene alfabéticamente.

nombres = input('ingrese lista de nombres separados por espacios: ').split();

nombres_ordenados = sorted(nombres);

print('nombres ordenados ', nombres_ordenados);