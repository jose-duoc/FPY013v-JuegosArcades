import random

NOMBRE_DEL_JUEGO = "Adivina el Número (Por: Antonia Del Solar)"

def ejecutar_juego():

    partidas_ganadas = 0
    partidas_jugadas = 0

    while True:

        print("\n" + "=" * 40)
        print("      ¡BIENVENIDO A ADIVINA EL NÚMERO!")
        print("=" * 40)

        numero_secreto = random.randint(1, 40)
        intentos = 5

        while intentos > 0:

            print("\n--- NUEVO INTENTO ---")

            try:
                numero = int(input("Ingresa un número entre 1 y 40: "))

                if numero == numero_secreto:
                    print("\n¡Correcto! Has ganado.")
                    partidas_ganadas += 1
                    partidas_jugadas += 1
                    break

                elif numero < numero_secreto:
                    print("El número es mayor.")

                else:
                    print("El número es menor.")

                intentos -= 1
                print(f"Intentos restantes: {intentos}")

            except ValueError:
                print("Debes ingresar un número válido.")

        if intentos == 0:
            partidas_jugadas += 1
            print(f"\nHas perdido. El número era {numero_secreto}")

        print("\n--- MENÚ ---")
        print("1. Jugar otra partida")
        print("2. Ver estadísticas")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            continue

        elif opcion == "2":
            print("\nEstadísticas")
            print(f"Partidas jugadas: {partidas_jugadas}")
            print(f"Partidas ganadas: {partidas_ganadas}")

            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            print("\nSaliendo del juego...")
            print(
                f"Estadísticas finales: Jugadas {partidas_jugadas} | Ganadas {partidas_ganadas}"
            )
            break

        else:
            print("Opción inválida. Volviendo al menú principal.")
            break