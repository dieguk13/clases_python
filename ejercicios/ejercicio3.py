#Crea una clase llamada "Estudiante" que tenga atributos de nombre, edad y lista de notas. La clase debe tener un método para calcular el promedio de las notas del estudiante.

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre;
        self.edad = edad;
        self.notas = notas;
        
    def calcular_promedio(self):
        #recorrer notas sumarlas y dividirlas por el total
        suma = 0;
        #las lineas 13, 14, 15 la forma larga de calcular
        #for nota in self.notas:
        #   suma = suma + nota;
        # print('el promedio es: ',  suma / len(self.notas));
        
        print('el promedio es: ',  sum(self.notas)/len(self.notas));
        
# crear objeto estudiante

estudiante = Estudiante('Juan ', 20, [3, 5, 4])
estudiante.calcular_promedio();
            