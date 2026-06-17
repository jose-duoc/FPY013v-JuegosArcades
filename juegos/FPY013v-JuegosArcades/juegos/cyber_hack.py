NOMBRE_DEL_JUEGO = "Cyber-Hack (Por: Mauricio Gálvez)"

def ejecutar_juego():

    import random
    import time

    def ejecutar_hackeo():
        print("="*40)
        print(" INICIANDO CONSOLA DE INFILTRACIÓN ")
        print("="*40)
        time.sleep(1)
        
        progreso_descarga = 0
        alerta_firewall = 0 
        herramientas = ["bruteforce", "phishing", "bypass"]
        
        print("\nObjetivo: Descargar los archivos confidenciales (100%).")
        print("¡Evita que la Alerta del Firewall llegue al 100%!")
        
        while progreso_descarga < 100 and alerta_firewall < 100:
            print(f"\n Descargado: {progreso_descarga}% |  Alerta del Firewall: {alerta_firewall}%")
            print("Selecciona tu script de hackeo:")
            print("1. Ataque Fuerza Bruta (Descarga rápida: 15-25%, Alerta media: 10-20%)")
            print("2. Inyección de Código Seguro (Descarga lenta: 5-10%, Alerta muy baja: 2-5%)")
            print("3. Reiniciar IP (No descarga, pero reduce la Alerta del Firewall: 15-30%)")
            
            entrada = input("admin@server:~# ").strip()
            
            try:
                opcion = int(entrada)
                if opcion < 1 or opcion > 3:
                    print("❌ Comando no reconocido por el sistema.")
                    continue
            except ValueError:
                print("❌ ERROR DE SINTAXIS: Introduce el número del comando.")
                continue
                
            if opcion == 1:
                descarga = random.randint(15, 25)
                riesgo = random.randint(10, 20)
                progreso_descarga += descarga
                alerta_firewall += riesgo
                print(f" Ejecutando fuerza bruta... Descargado +{descarga}%. El sistema generó +{riesgo}% de alerta.")
                
            elif opcion == 2:
                descarga = random.randint(5, 10)
                riesgo = random.randint(2, 5)
                progreso_descarga += descarga
                alerta_firewall += riesgo
                print(f" Inyectando código silencioso... Descargado +{descarga}%. El sistema generó +{riesgo}% de alerta.")
                
            elif opcion == 3:
                reduccion = random.randint(15, 30)
                alerta_firewall = max(0, alerta_firewall - reduccion)
                print(f" Limpiando registros y cambiando IP. Alerta reducida en -{reduccion}%.")
                
            time.sleep(1)
            
            if progreso_descarga < 100 and alerta_firewall < 100:
                print("\n El Firewall está escaneando la red...")
                time.sleep(1)
                
                contraataque = random.choice(["Escaneo de Puertos", "Bloqueo de Paquetes"])
                
                if contraataque == "Escaneo de Puertos":
                    daño_seguridad = random.randint(5, 15)
                    print(f" El Firewall ejecutó un {contraataque}. ¡Tu alerta sube +{daño_seguridad}%!")
                    alerta_firewall += daño_seguridad
                else:
                    daño_seguridad = random.randint(8, 12)
                    print(f" El Firewall ejecutó un {contraataque}. ¡Tu rastro aumenta +{daño_seguridad}%!")
                    alerta_firewall += daño_seguridad
                    
        
        if progreso_descarga >= 100:
            print("\n [HACKEO EXITOSO] ")
            print("Has descargado toda la base de datos sin ser detectado. ¡Eres un fantasma digital!")
        elif alerta_firewall >= 100:
            print("\n [CONEXIÓN INTERCEPTADA] ")
            print("El Firewall te localizó. Tu señal fue bloqueada y el FBI va en camino hacia tu posición.")

    
    ejecutar_hackeo()
