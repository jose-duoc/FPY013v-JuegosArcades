import random

NOMBRE_DEL_JUEGO = "Carrera de Autos"

def avanzar_auto():
    return random.randint(1, 6)

def mostrar_pista(nombre, posicion, meta):
    pista = "-" * posicion + "A" + "-" * (meta - posicion)
    print(nombre + ": " + pista)

def obstaculo(posicion):
    """20% de probabilidad de obstáculo"""
    if random.randint(1, 100) <= 20:
        retroceso = random.randint(2, 4)
        print("🛞 ¡Obstáculo en la pista! Retrocedes", retroceso, "espacios")
        posicion -= retroceso
        if posicion < 0:
            posicion = 0
    return posicion

def ejecutar_juego():

    print("\n" + "=" * 45)
    print("BIENVENIDO A CARRERA DE AUTOS")
    print("=" * 45)

    nombre_jugador = input("Ingresa tu nombre: ")

    partidas = 0
    victorias_jugador = 0
    victorias_pc = 0

    while True:

        print("\n1. Iniciar carrera")
        print("2. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "2":
            print("\nSaliendo del juego...")
            print("Carreras jugadas:", partidas)
            print(nombre_jugador, ":", victorias_jugador, "| IA:", victorias_pc)
            break

        if opcion != "1":
            print("Opcion invalida")
            continue

        meta = 30
        posicion_jugador = 0
        posicion_pc = 0
        nitros = 3

        print("\nComienza la carrera")

        while posicion_jugador < meta and posicion_pc < meta:

            input("\nPresiona ENTER para avanzar")

            print("\nNitros disponibles:", nitros)
            print("1. Avance normal")
            print("2. Usar Nitro")

            opcion_nitro = input("Elige una opcion: ")

            # 🚗 JUGADOR
            if opcion_nitro == "2" and nitros > 0:
                nitros -= 1

                if random.randint(1, 100) <= 70:
                    avance_jugador = random.randint(5, 10)
                    print("⚡ Nitro activado")
                else:
                    avance_jugador = 0
                    print("💥 El Nitro fallo")
            else:
                avance_jugador = avanzar_auto()

            # 🛞 obstáculo jugador
            posicion_jugador += avance_jugador
            posicion_jugador = obstaculo(posicion_jugador)

            # 🤖 IA
            avance_pc = avanzar_auto()
            posicion_pc += avance_pc

            # 🛞 obstáculo IA
            posicion_pc = obstaculo(posicion_pc)

            if posicion_jugador > meta:
                posicion_jugador = meta

            if posicion_pc > meta:
                posicion_pc = meta

            print("\nTu avanzaste", avance_jugador, "espacios")
            print("La IA avanzo", avance_pc, "espacios")

            mostrar_pista(nombre_jugador, posicion_jugador, meta)
            mostrar_pista("IA", posicion_pc, meta)

        partidas += 1

        if posicion_jugador >= meta and posicion_pc >= meta:
            print("\nEmpate")
        elif posicion_jugador >= meta:
            print("\nGanaste la carrera")
            victorias_jugador += 1
        else:
            print("\nLa IA gano la carrera")
            victorias_pc += 1

        print("\nEstadisticas")
        print("Carreras jugadas:", partidas)
        print(nombre_jugador, ":", victorias_jugador, "| IA:", victorias_pc)
        print("-" * 45)

if __name__ == "__main__":
    ejecutar_juego()