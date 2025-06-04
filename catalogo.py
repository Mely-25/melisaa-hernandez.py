import os

# Clase Pelicula
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # atributo privado

    def get_nombre(self):
        return self.__nombre

# Clase Catálogo
class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w") as archivo:
                pass  # Crea el archivo si no existe
            print(f"📁 Se creó un nuevo catálogo: {self.ruta_archivo}")
        else:
            print(f"📁 Catálogo encontrado: {self.ruta_archivo}")

    def agregar(self, pelicula):
        with open(self.ruta_archivo, "a") as archivo:
            archivo.write(pelicula.get_nombre() + "\n")
        print(f"✅ Película '{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        print("\n📃 Lista de películas:")
        try:
            with open(self.ruta_archivo, "r") as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    for p in peliculas:
                        print("🎬", p.strip())
                else:
                    print("⚠️ El catálogo está vacío.")
        except FileNotFoundError:
            print("❌ El archivo no existe.")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("🗑️ el catalogo fue eliminado con éxito.")
        else:
            print("❌ El catálogo no existe para eliminar.")