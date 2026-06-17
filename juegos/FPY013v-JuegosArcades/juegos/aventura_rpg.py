NOMBRE_DEL_JUEGO = "Aventura RPG (Por: Mauricio Gálvez)"

def ejecutar_juego():
    import random, time
    
    def monstruoAleatorio(nivel_actual):
        monstruos = [
            ["Goblin Verde", 30, 45],
            ["Orco Enojado", 55, 75],
            ["Dragón Joven", 80, 110],
        ]
        
        seleccionado = random.choice(monstruos)

        nombre = seleccionado[0]
        multiplicador_vida = 1 + (nivel_actual - 1) * 0.3 
        vida_base = random.randint(seleccionado[1], seleccionado[2])
        vida_final = int(vida_base * multiplicador_vida)
        return nombre, vida_final
    
    def elegir_clase():
        print("="*40)
        print("\n--- SELECCIÓN DE CLASE ---")
        time.sleep(1)
        while True:
            clase = input("Elige tu clase (Guerrero / Mago / Arquero): ").strip().lower()
            
            if clase == "guerrero":
                print("¡Has elegido al Guerrero! Gran vitalidad y ataques físicos estables.")
                return "Guerrero", 90
            elif clase == "mago":
                print("¡Has elegido al Mago! Menos vida, pero con magia devastadora e inestable.")
                return "Mago", 55
            elif clase == "arquero":
                print("¡Has elegido al Arquero! Vida equilibrada y tiros de alta precisión o gran riesgo.")
                return "Arquero", 70
            else:
                print(" Clase no válida. Escribe 'Guerrero', 'Mago' o 'Arquero'.")
                
    def iniciar_combate():
        print("\n" + "="*40)
        print("\n" + ("="*6) + "  BIENVENIDO A LA AVENTURA  " + ("="*6))
        print("\n" + "="*40)
        
        clase_jugador, vida_jugador = elegir_clase()
        vida_maxima = vida_jugador
        nivel = 1

        jugando = True

        while jugando and vida_jugador > 0:
            nombre_monstruo, vida_monstruo = monstruoAleatorio(nivel)
            print("\n" + "="*40)
            print("\n" + ("="*6) + f"¡Avanzas al nivel {nivel}!" + ("="*6))
            print(f"¡Un {nombre_monstruo} (Nivel {nivel}) aparece con {vida_monstruo} de vida!")
            print("\n" + "="*40)
            time.sleep(1)
            #Turno jugador
            while vida_jugador > 0 and vida_monstruo > 0:
                print("\n" + "="*40)
                print(f"Tu Vida: {vida_jugador}/{vida_maxima} ({clase_jugador}) | Vida de {nombre_monstruo}: {vida_monstruo}")
                print("Elige tu ataque:")
                if clase_jugador == "Guerrero":
                    print("1. Espadazo (Daño seguro: 12-18)")
                    print("2. Escudazo (Daño bajo: 5-8, pero te cura 5 HP)")
                elif clase_jugador == "Mago":
                    print("1. Rayo Eléctrico (Daño medio: 10-22)")
                    print("2. Explosión Arcana (Daño caótico: 2-35)")
                elif clase_jugador == "Arquero":
                    print("1. Tiro Rápido (Flecha segura: 10-16)")
                    print("2. Disparo a la Cabeza (50% de probabilidad: 0 o 35 de daño)")
                print("3. Poción de Curación (Recupera 15-25 HP)")

                entrada = input("> ").strip()

                try:
                    eleccion = int(entrada)
                    if eleccion < 1 or eleccion > 3:
                        print(" Opción no válida. Elige un número entre 1 y 3.")
                        continue
                except ValueError:
                    print(" Entrada inválida. Por favor, escribe un número.")
                    continue
                    
                if eleccion == 1:
                    if clase_jugador == "Guerrero":
                        daño = random.randint(12, 18)
                        print(f"¡Tu Espadazo le quita {daño} de vida al {nombre_monstruo}!")
                        time.sleep(1)
                    elif clase_jugador == "Mago":
                        daño = random.randint(10, 22)
                        print(f"¡Tu Rayo Eléctrico electrocuta al {nombre_monstruo} por {daño} de daño!")
                        time.sleep(1)
                    else: # Arquero
                        daño = random.randint(10, 16)
                        print(f"¡Tu Tiro Rápido impacta en el blanco haciendo {daño} de daño!")
                        time.sleep(1)
                
                    vida_monstruo -= daño
            
                elif eleccion == 2:
                    if clase_jugador == "Guerrero":
                        daño = random.randint(5, 8)
                        vida_jugador += 5
                        print(f"¡Golpeas con el escudo! Haces {daño} de daño y recuperas 5 HP por tu defensa.")
                        time.sleep(1)
                        vida_monstruo -= daño
                    elif clase_jugador == "Mago":
                        daño = random.randint(2, 35)
                        print(f"La Explosión Arcana impacta haciendo {daño} de daño.")
                        time.sleep(1)
                        vida_monstruo -= daño
                    else:#arquero
                        punteria = random.choice(["acierto", "fallo"])
                        if punteria == "acierto":
                            daño = 35
                            print(f"¡BRUTAL! Tensas el arco, apuntas y metes un flechazo en los ojos del {nombre_monstruo} por {daño} de daño!")
                            time.sleep(1)
                            vida_monstruo -= daño
                        else:
                            print("¡Fallo! El enemigo esquivó tu flecha en el último segundo. 0 de daño.")
                    
                elif eleccion == 3:
                    curacion = random.randint(15, 25)
                    vida_jugador = min(vida_maxima, vida_jugador + curacion)
                    print(f"Te tomas una poción. ¡Recuperas {curacion} de vida!")
                    time.sleep(1)
                    
                if vida_monstruo <= 0:
                    print(f"¡Felicidades! Has derrotado al {nombre_monstruo}!")
                    nivel += 1

                    recompensa_vida = 20
                    vida_jugador = min(vida_maxima, vida_jugador + recompensa_vida)
                    print(f"Recibes {recompensa_vida} de vida como recompensa por tu victoria.")
                    time.sleep(1)

                    continuar = input("¿Quieres continuar al siguiente nivel? (si/no): ").strip().lower()
                    if continuar == "no":
                        print("¡Gracias por jugar! Hasta la próxima aventura.")
                        jugando = False
                    continue
                #Turno monstruo
                print(f"\n Turno del {nombre_monstruo}...")
                multiplicador_daño = 1 + (nivel - 1) * 0.15 
                time.sleep(1)

                if nombre_monstruo == "Goblin Verde":
                    ataque = random.choice(["Puñalada", "Lanzar Piedra"])
                    print(f"¡El {nombre_monstruo} se prepara para atacar con {ataque}!")
                    time.sleep(1)
                    if ataque == "Puñalada":
                        daño_base = random.randint(10, 15)
                        print(f"¡El {nombre_monstruo} te ataca con una Puñalada causando {daño_base} de daño!")
                    else:
                        daño_base = random.randint(5, 9)
                        print(f"¡El {nombre_monstruo} te lanza una piedra causando {daño_base} de daño!")
                elif nombre_monstruo == "Orco Enojado":
                    ataque = random.choice(["Golpe con Maza", "Grito de Guerra"])
                    print(f"¡El {nombre_monstruo} se prepara para atacar con {ataque}!")
                    time.sleep(1)
                    if ataque == "Golpe con Maza":
                        daño_base = random.randint(12, 20)
                        print(f"¡El {nombre_monstruo} te golpea con su maza causando {daño_base} de daño!")
                    else:
                        daño_base = random.randint(6, 10)
                        print(f"¡El {nombre_monstruo} te lanza un grito de guerra que te causa {daño_base} de daño psicológico!")
                else: #dragon
                    ataque = random.choice(["Llamarada", "Garra Afilada"])
                    print(f"¡El {nombre_monstruo} se prepara para atacar con {ataque}!")
                    time.sleep(1)
                    if ataque == "Llamarada":
                        daño_base = random.randint(18, 28)
                        print(f"¡El {nombre_monstruo} te lanza una llamarada causando {daño_base} de daño!")
                    else:
                        daño_base = random.randint(10, 16)
                        print(f"¡El {nombre_monstruo} te ataca con su garra afilada causando {daño_base} de daño!")
                time.sleep(1)
                daño_monstruo = int(daño_base * multiplicador_daño)
                vida_jugador -= daño_monstruo

            if vida_jugador <= 0:
                    
                print("¡Has sido derrotado! Mejor suerte la próxima vez.")

    iniciar_combate()