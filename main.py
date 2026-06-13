import os
import importlib

def cargar_juegos_estudiantes():
    """Busca y acopla automáticamente los archivos de cada estudiante."""
    juegos_registrados = {}
    carpeta = "juegos"
    
    # Crear la carpeta automáticamente si no existe al iniciar
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        # Crear un archivo vacío __init__.py necesario para Python
        with open(os.path.join(carpeta, "__init__.py"), "w") as f:
            f.write("")

    # Leer todos los archivos .py de la carpeta 'juegos' 
    archivos = [f[:-3] for f in os.listdir(carpeta) if f.endswith('.py') and f != '__init__.py']
    
    for archivo in archivos:
        try:
            # Importar el archivo del estudiante dinámicamente
            modulo = importlib.import_module(f"{carpeta}.{archivo}")
            
            # Verificar que el estudiante haya creado la función requerida 'ejecutar_juego'
            if hasattr(modulo, "ejecutar_juego"):
                # Si el estudiante definió un nombre para su juego, lo usamos; si no, usamos su nombre de archivo
                nombre_pantalla = getattr(modulo, "NOMBRE_DEL_JUEGO", archivo.capitalize())
                juegos_registrados[nombre_pantalla] = modulo.ejecutar_juego
        except Exception as e:
            print(f" No se pudo cargar el archivo '{archivo}.py': {e}")
            
    return juegos_registrados

def ejecutar_arcade():
    while True:
        print("\n" + "═" * 45)
        print("   ARCADE FPY013V - ABIERTO - PROYECTO COLABORATIVO  ")
        print("═" * 45)
        
        diccionario_juegos = cargar_juegos_estudiantes()
        lista_nombres = list(diccionario_juegos.keys())
        
        if not lista_nombres:
            print(" [!] No hay juegos disponibles en la carpeta 'juegos'.")
            print("     Los estudiantes deben subir sus archivos .py allí.")
        else:
            # Mostrar los juegos de los alumnos dinámicamente
            for indice, nombre in enumerate(lista_nombres, start=1):
                print(f"  [{indice}] - Jugar a: {nombre}")
                
        opcion_salir = len(lista_nombres) + 1
        print(f"  [{opcion_salir}] - Salir del programa")
        print("═" * 45)
        
        try:
            seleccion = int(input("Selecciona una opción: "))
            
            if seleccion == opcion_salir:
                print("\n¡Gracias por jugar! Cerrando el Arcade...")
                break
            elif 1 <= seleccion <= len(lista_nombres):
                nombre_elegido = lista_nombres[seleccion - 1]
                funcion_del_alumno = diccionario_juegos[nombre_elegido]
                
                print(f"\n Lanzando: {nombre_elegido}...\n" + "-"*40)
                # Ejecuta el código del estudiante
                funcion_del_alumno()
                print("-"*40)
                
                input("\nPresiona Enter para regresar al menú principal...")
            else:
                print(" Opción fuera de rango. Intenta de nuevo.")
        except ValueError:
            print(" Entrada inválida. Por favor, escribe un número.")

if __name__ == "__main__":
    ejecutar_arcade()
