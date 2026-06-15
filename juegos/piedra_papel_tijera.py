# juegos/piedra_papel_tijera.py
import random

# Constante para que el menú del Arcade muestre un nombre bonito en el HTML
NOMBRE_DEL_JUEGO = "Piedra, Papel o Tijera"

def validar_opcion(opcion):
    """Verifica si la opción ingresada por el usuario es válida."""
    opciones_validas = ["1", "2", "3", "4"]
    return opcion in opciones_validas

def determinar_ganador(usuario, computadora):
    """Aplica las reglas del juego y retorna el resultado."""
    if usuario == computadora:
        return "empate"
    
    # Casos en los que gana el usuario
    if (usuario == "Piedra" and computadora == "Tijera") or \
       (usuario == "Papel" and computadora == "Piedra") or \
       (usuario == "Tijera" and computadora == "Papel"):
        return "usuario"
    
    # Si no es empate y no gana el usuario, gana la computadora
    return "computadora"

def ejecutar_juego():
    """Función principal obligatoria que invocará el Arcade."""
    opciones = {
        "1": "Piedra",
        "2": "Papel",
        "3": "Tijera"
    }
    
    print("\n" + "═" * 40)
    print(" 🎮 ¡BIENVENIDO A PIEDRA, PAPEL O TIJERA! 🎮 ")
    print("═" * 40)
    
    jugadas = 0
    victorias_usuario = 0
    victorias_pc = 0
    
    while True:
        print(f"\n--- RONDA {jugadas + 1} ---")
        print("1. Piedra 🪨")
        print("2. Papel 📄")
        print("3. Tijera ✂️")
        print("4. Volver al menú principal 🚪")
        
        eleccion = input("Elige una opción (1-4): ").strip()
        
        if not validar_opcion(eleccion):
            print("⚠️ Opción inválida. Por favor, ingresa un número del 1 al 4.")
            continue
            
        if eleccion == "4":
            print("\nSaliendo del juego...")
            print(f"📊 Estadísticas finales: Rondas jugadas: {jugadas} | Tú: {victorias_usuario} | PC: {victorias_pc}")
            break
            
        # Obtener las jugadas reales
        jugada_usuario = opciones[eleccion]
        jugada_pc = random.choice(["Piedra", "Papel", "Tijera"])
        
        print(f"\n👉 Tú elegiste: {jugada_usuario}")
        print(f"🤖 La IA eligió: {jugada_pc}")
        
        # Procesar resultado
        resultado = determinar_ganador(jugada_usuario, jugada_pc)
        
        if resultado == "empate":
            print("🤝 ¡Es un empate!")
        elif resultado == "usuario":
            print("🎉 ¡Ganaste esta ronda!")
            victorias_usuario += 1
        else:
            print("💻 La IA gana esta ronda.")
            victorias_pc += 1
            
        jugadas += 1
        print(f"Score actual -> Tú: {victorias_usuario} | Computadora: {victorias_pc}")
        print("-" * 40)

# Permite probar el juego de forma aislada ejecutando directamente este archivo
if __name__ == "__main__":
    ejecutar_juego()
