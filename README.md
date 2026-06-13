#  Proyecto Arcade FPY013V - Python & GitHub

¡Bienvenido al proyecto final colaborativo de la clase! El objetivo de esta actividad es construir un **Arcade de Juegos de Texto** interactivo en Python utilizando un entorno de desarrollo real con Git y GitHub.

El archivo principal `main.py` funciona como el "motor" del Arcade. Está programado para escanear de forma automática la carpeta `juegos/`, detectar sus entregas de código e integrarlas dinámicamente al menú principal.

---

##  REGLA DE ORO DEL PROYECTO
> **PROHIBIDO MODIFICAR EL ARCHIVO `main.py`.** > Para que tu juego aparezca en el menú, solo debes crear tu propio archivo dentro de la carpeta `juegos/`. Si modificas el archivo central `main.py`, tu entrega será rechazada debido a los conflictos de código que ocasionarás con tus compañeros.

---

##  Instrucciones Paso a Paso para Estudiantes

Sigue estos pasos en orden para clonar el proyecto, programar tu minijuego y enviar tu tarea correctamente:

### Paso 1: Clonar el repositorio y preparar tu entorno
Abre tu terminal o Git Bash y ejecuta los siguientes comandos:
```bash
# 1. Clona este repositorio en tu computadora
git clone <URL_DE_ESTE_REPOSITORIO>

# 2. Entra a la carpeta del proyecto
cd mi_arcade_colaborativo

# 3. Crea una rama propia con tu nombre para no trabajar directamente en 'main'
git checkout -b feature-juego-tuNombre

### Paso 2: Crear tu archivo de juego
Dirígete a la carpeta llamada juegos/.
Crea un archivo nuevo en formato Python.
El nombre del archivo debe ser tu primer nombre y apellido en minúsculas, separados por un guión bajo (Ejemplo: juan_perez.py).
### Paso 3: Codificar respetando la estructura obligatoria
Para que el menú de main.py reconozca tu juego sin errores, tu archivo DEBE incluir obligatoriamente dos elementos con estos nombres exactos:
Una variable de texto llamada NOMBRE_DEL_JUEGO.
Una función principal llamada ejecutar_juego().
Plantilla base para tu archivo (Copia y modifica esto):
Python
# Archivo: juegos/tu_nombre_tu_apellido.py

# 1. El nombre que aparecerá listado en el menú del Arcade
NOMBRE_DEL_JUEGO = "Adivina el Número (Por: Tu Nombre)"

# 2. La función principal que arrancará tu minijuego al seleccionarlo
def ejecutar_juego():
    import random
    
    print(" ¡Bienvenido a mi minijuego de azar! ")
    opcion = input("Elige (1) Cara o (2) Cruz: ")
    resultado = random.choice(["1", "2"])
    
    if opcion == resultado:
        print(" ¡Felicidades, ganaste!")
    else:
        print(" Suerte para la próxima.")
