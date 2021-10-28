class Categoria:

    def __init__(self):
        self.categorias = []

    def leer_archivo(self):
        """Este método lee el archivo de categorias.txt y asigna el
        contenido del mismo al atrubuto categorias.
        """
        pass

    def guardar_en_archivo(self):
        """Este método guarda el contenido del atributo categorias
        en el archivo categorias.txt.
        """
        pass

    def agregar_categoria(self):
        nueva_categoria = input("Ingresá la nueva categoría: ")
        self.categorias.append(nueva_categoria)

    def eliminar_categoria(self):
        """Este método pide al usuario que ingrese una categoría y la
        elimina de la lista categorias atributo de esta clase.
        Previamente verifica que el usuario haya ingresado una opción
        correcta.
        """
        pass

categoria_de_libros = Categoria()
menu = """
########## MENU ##########
--------------------------
1. Agregar nueva categoría
2. Eliminar una categoría
3. Listar categorías
4. Guardar y salir
"""
opciones = ["1", "2", "3", "4"]
opcion_escogida = ""
while opcion_escogida != "4":
    print(menu)
    opcion_escogida = input("Ingresar la opción deseada: ")
    if opcion_escogida not in opciones:
        print("¡Ingrese una opción correcta!")
    elif opcion_escogida == "1":
        categoria_de_libros.agregar_categoria()
    elif opcion_escogida == "2":
        categoria_de_libros.eliminar_categoria()
    elif opcion_escogida == "3":
        print(categoria_de_libros.categorias)
    else:
        print("Guardando...")
        categoria_de_libros.guardar_en_archivo()
        print("¡Chau!")
