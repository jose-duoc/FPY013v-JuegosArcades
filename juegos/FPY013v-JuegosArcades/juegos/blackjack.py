NOMBRE_DEL_JUEGO = "BlackJack (Por: Mauricio Gálvez)"

def ejecutar_juego():


    def calcular_puntaje(lista_cartas):
        total = 0
        cant_ases = 0
        
        for carta in lista_cartas:
            if carta == "J" or carta == "Q" or carta == "K":
                total = total + 10
            elif carta == "A":
                total = total + 11
                cant_ases = cant_ases + 1
            else:
                total = total + int(carta)
        while total > 21 and cant_ases > 0:
            total = total - 10
            cant_ases = cant_ases - 1
        return total

    import random, time

    def jugar_21():
        print("="*40)
        print(" INICIANDO JUEGO DE BLACKJACK ")
        print("="*40)
        time.sleep(1)

        baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4

        mis_cartas = []
        cartas_casa = []

        #repartir 2
        for i in range (2):
            carta1 = random.choice(baraja)
            mis_cartas.append(carta1)
            baraja.remove(carta1)

            carta2 = random.choice(baraja)
            cartas_casa.append(carta2)
            baraja.remove(carta2)

        jugando = True

        while jugando:
            mi_puntaje = calcular_puntaje(mis_cartas)
            print(f"\n Tus cartas: {mis_cartas} | Puntaje: {mi_puntaje}")
            print(f" Carta visible de la casa: {cartas_casa[0]}")  

            if mi_puntaje > 21:
                print("Te pasaste de 21. Perdiste.")
                return
            print("\n¿Qué deseas hacer?")
            print("1. Pedir otra carta")
            print("2. Plantarse")

            entrada = input("> ").strip()

            try:
                opcion = int(entrada)
                if opcion < 1 or opcion > 2:
                    print("Opción no válida. Escribe '1' para pedir carta o '2' para plantarte.")
                    continue
            except ValueError:
                print("ERROR DE SINTAXIS: Introduce '1' para pedir carta o '2' para plantarte.")
                continue   

            if opcion == 1:
                nueva_carta = random.choice(baraja)
                mis_cartas.append(nueva_carta)
                baraja.remove(nueva_carta)
                print(f"Pediste una carta: {nueva_carta}")
                time.sleep(1)
            elif opcion == 2:
                print("Te has plantado. Es el turno de la casa.")
                time.sleep(1)
                jugando = False
        
        # turno casa
        puntaje_casa = calcular_puntaje(cartas_casa)

        print(f"\n Cartas de la casa: {cartas_casa} | Puntaje: {puntaje_casa}")
        time.sleep(1)

        while puntaje_casa < 17:
            carta_nueva_casa = random.choice(baraja)
            cartas_casa.append(carta_nueva_casa)
            baraja.remove(carta_nueva_casa)
            
            puntaje_casa = calcular_puntaje(cartas_casa)

            print(f"La casa pide una carta: {carta_nueva_casa} | Nuevo puntaje: {puntaje_casa}")
            time.sleep(1)

        print(f"\n Cartas finales de la casa: {cartas_casa} | Puntaje final: {puntaje_casa}")
        time.sleep(1)
        print("\nCalculando resultado...")
        time.sleep(2)                           
        print(f"\n Tu puntaje: {mi_puntaje} | Puntaje de la casa: {puntaje_casa}")

        if puntaje_casa > 21:
            print("La casa se pasó de 21. ¡Ganaste!")           
        elif mi_puntaje > puntaje_casa:
            print("¡Ganaste! Tu puntaje es mayor que el de la casa.")   
        elif mi_puntaje < puntaje_casa:
            print("Perdiste. El puntaje de la casa es mayor que el tuyo.")  
        else:
            print("Empate. El puntaje de la casa y el tuyo son iguales.")
        print("="*40)

    jugar_21()
    

