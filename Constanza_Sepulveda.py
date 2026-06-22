import time
import random
import os

#Variable del nombre del juego
NOMBRE_DEL_JUEGO = "Neon Thread"
#Esta funcion arrancara nuestro minijuego
def ejecutar_juego():
    # Esta funcion sirve para hacer una limpia a la pantalla segun el sistema 
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    limpiar_pantalla()
    print("="*60)
    print(" 🧵 BIENVENIDO A NEON THREAD 🧵 ")
    print("="*60)
    print(" REGLAS:")
    print(" 1. Una barrera con un hueco caerá en la pantalla.")
    print(" 2. Un hilo de luz se moverá  de manera horizontalmente.")
    print(" 3. Tu objetivo es presionar ENTER en el momento exacto")
    print("    en que el hilo apunte directamente en el hueco de la barrera.")
    print("="*60)
    
    input("\nPresiona ENTER para iniciar la sincronización...")

    #Comenzamos con la configuracion del juego
    largo_pista = 30
    ancho_hueco = 6
    #Definimos la posicion del hueco de manera aleatoria
    hueco_inicio = random.randint(2, largo_pista - ancho_hueco - 2)
    hueco_fin = hueco_inicio + ancho_hueco
    #Construimos la barrera visualmente para el juego
    #Ejemplo: ██████████ *HUECO* ████████████
    barrera_izquierda = "█" * hueco_inicio
    barrera_derecha = "█" * (largo_pista - hueco_fin)
    espacio_hueco = " " * ancho_hueco
    pista_barrera = barrera_izquierda + espacio_hueco + barrera_derecha
    #Variables del movimiento
    posicion_hilo = 0
    direccion = 1  # 1 derecha, -1 izquierda
    puntuacion = 0
    
    print("\n¡PREPÁRATE!")
    time.sleep(1)

    while True:
        limpiar_pantalla()
        
        print(f"🎯 PUNTUACIÓN: {puntuacion}")
        print("\n--- BARRERA ---")
        print(pista_barrera)
        print("--------------------------")
        
        #Dibujamos la linea del hilo en la posicion actual
        pista_hilo = [" "] * largo_pista
        if posicion_hilo < largo_pista - 3:
            pista_hilo[posicion_hilo] = ">"
            pista_hilo[posicion_hilo+1] = ">"
            pista_hilo[posicion_hilo+2] = ">"
        else:
            pista_hilo[posicion_hilo] = ">"
            
        print("".join(pista_hilo))
        print("--------------------------")
        
        accion = input("\n[Presiona ENTER para avanzar el hilo / Escribe 'C' para CALIBRAR en el ojal]: ").strip().upper()
        
        if accion == 'C':
            if hueco_inicio <= posicion_hilo <= hueco_fin - 3:
                puntuacion += 100
                print("\n¡HILO ENCESTADO EN EL HUECO!")
                print(f"Pasaste limpiamente por las barreras. +100 puntos.")
                input("\nPresiona ENTER para la siguiente ronda...")
                
                #Siguiente ronda:Se cambiara el hueco de lugar para subirle la dificultad
                hueco_inicio = random.randint(2, largo_pista - ancho_hueco - 2)
                hueco_fin = hueco_inicio + ancho_hueco
                barrera_izquierda = "█" * hueco_inicio
                barrera_derecha = "█" * (largo_pista - hueco_fin)
                pista_barrera = barrera_izquierda + espacio_hueco + barrera_derecha
                posicion_hilo = 0
                direccion = 1
                continue
            else:
                print("\n¡HILO ROTO!")
                print(f"Chocaste contra la barrera")
                print(f"Puntuación final: {puntuacion} puntos")
                print("="*60)
                input("\nPresiona ENTER para salir al menú principal del Arcade...")
                break

        #Movimiento del hilo de lado a lado
        posicion_hilo += direccion   
        #El rebote en los bordes
        if posicion_hilo >= largo_pista - 3 or posicion_hilo <= 0:
            direccion *= -1