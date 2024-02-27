
class Gg:
    def __init__(self, nombre, apellido, edad):
     self.nombre = nombre
     self.apellido= apellido
     self.edad= edad
    
    def mostrar_detalle(self):
        print(f'Gg: {self.nombre} {self.apellido} {self.edad}')
        
persona1= Gg('Juan', 'Perez', 30)
persona1.mostrar_detalle()
print(persona1.edad)

