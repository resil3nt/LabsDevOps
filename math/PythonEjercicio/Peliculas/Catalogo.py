class Catalogo:
    ruta_archivo= 'peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')


    @classmethod
    def listar_peliculas(cls)
