from catalogo import Pelicula, CatalogoPeliculas
import os
import time

def mostrar_menu():
    print("\n--- Menú del Catálogo de Películas ---")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo")
    print("4. Salir")

# Saludo inicial
print("🎬 ¡Bienvenida/o al administrador de tu propio catálogo de películas!")
print("Con este programa podés guardar, ver o borrar tus pelis favoritas. 😊\n")

nombre_catalogo = input("📁 Ingresá el nombre del catálogo: ")
catalogo = CatalogoPeliculas(nombre_catalogo)

# Verificamos si el archivo ya existe
if not os.path.exists(catalogo.ruta_archivo):
    print(f"📂 Se creó un nuevo catálogo llamado '{nombre_catalogo}.txt'.")
else:
    print(f"📁 El catálogo '{nombre_catalogo}.txt' ya existe.")

while True:
    mostrar_menu()
    opcion = input("Elegí una opción (1-4): ")

    if opcion == '1':
        nombre_pelicula = input("🎞️ Ingresá el nombre de la película: ")
        pelicula = Pelicula(nombre_pelicula)
        catalogo.agregar(pelicula)

    elif opcion == '2':
        catalogo.listar()

    elif opcion == '3':
        confirmar = input("¿Estás segura/o de querer eliminar el catálogo? (s/n): ")
        if confirmar.lower() == 's':
            catalogo.eliminar()

    elif opcion == '4':
        print("Saliendo", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
        print("\n👋 ¡Nos vemos! Gracias por usar el programa.")
        break

    else:
        print("⚠️ Opción no válida. Intentá de nuevo.")