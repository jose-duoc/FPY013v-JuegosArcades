import random

# Símbolos posibles
simbolos = ["guinda", "limon", "sandia", "naranja", "7"]

# Función para girar la máquina
def girar():
    return [random.choice(simbolos) for _ in range(3)]

# Juego principal
credito = 3
print("=== Bienvenido a la Máquina de frutas en Python ===")
print("Comienzas con", credito, "créditos")

while credito > 0:
    input("Presiona ENTER para girar...")
    resultado = girar()
    print(" | ".join(resultado))
    # Condiciones de premio
    if resultado[0] == resultado[1] == resultado[2]:
        print("¡Jackpot! Ganaste 5 créditos ")
        credito += 3
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        print("¡Ganaste 2 créditos! ")
        credito += 2
    else:
        print("No ganaste nada ")
        credito -= 1
    print("Créditos restantes:", credito)

print("Juego terminado. Te quedaste sin créditos.")