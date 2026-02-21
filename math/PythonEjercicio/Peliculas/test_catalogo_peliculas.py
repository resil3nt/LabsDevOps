from Pelicula import Pelicula

opcion = None
while opcion != 4:
    print('Opciones; ')
    print('1. Agregar Peliculas')
    print('2. Listar Peliculas')
    print('3. Eliminar Peliculas')
    print('Exit')

    opcion = input('Escribe tu opcion (1-4): ')

    if opcion == 1:
        nombre_pelicula = input('Proporciona el nombre de la Peli:')
        pelicula = pelicula(nombre_pelicula)
        cp.agregar_pelicula(pelicula)
    elif opcion == 2:
        cp.listar_peliculas()
    elif opcion == 3:
        cp.eliminar_peliculas()
else:
    print('Terminando Programa')