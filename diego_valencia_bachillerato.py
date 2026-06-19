# Archivo: juegos/diego_valencia_bachillerato.py
import random
import time  # Importamos el módulo de tiempo

NOMBRE_DEL_JUEGO = "Bachillerato Contra Reloj (Por: Diego Valencia)"

def ejecutar_juego():
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'V']
    
    categorias = [
        'Nombre', 'Apellido', 'País', 'Ciudad', 
        'Color', 'Animal', 'Fruta', 'Verdura'
    ]
    
    letra_elegida = random.choice(letras)
    puntaje = 0
    puntaje_maximo = len(categorias) * 10
    tiempo_limite = 10  # Segundos que tiene el jugador para responder
    
    print(f"\n--- ¡BACHILLERATO CONTRA RELOJ! ---")
    print(f"La letra elegida es la: {letra_elegida}")
    print(f"¡Cuidado! Solo tienes {tiempo_limite} segundos por categoría.")
    print("-----------------------------------")
    
    for cat in categorias:
        # 1. Iniciamos el "cronómetro"
        tiempo_inicio = time.time() 
        
        # 2. El usuario escribe su respuesta
        respuesta = input(f"Escribe un/a {cat} con '{letra_elegida}': ").strip().upper()
        
        # 3. Detenemos el "cronómetro" y calculamos cuánto tardó
        tiempo_fin = time.time() 
        tiempo_tomado = tiempo_fin - tiempo_inicio
        
        # 4. Validamos el tiempo y la respuesta
        if tiempo_tomado > tiempo_limite:
            # Si tardó más del límite, formateamos los decimales a 1 (.1f)
            print(f"  ¡Tiempo agotado! Tardaste {tiempo_tomado:.1f} segundos. 0 puntos.\n")
            
        elif respuesta and respuesta.startswith(letra_elegida):
            print(f"  ¡Válido! Respondiste en {tiempo_tomado:.1f} seg. +10 puntos.\n")
            puntaje += 10
            
        else:
            print(f"  Error. No empieza con '{letra_elegida}' o está en blanco.\n")
            
    print("-----------------------------------")
    print(f"Juego terminado.")
    print(f"Tu puntaje final es: {puntaje} de {puntaje_maximo} puntos posibles.")
    print("-----------------------------------\n")