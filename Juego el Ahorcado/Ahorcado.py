import random

# Lista de palabras a adivinar
palabras = ["hola", "mundo", "python"]

# Selecciona una palabra al azar
palabra_a_adivinar = random.choice(palabras)
longitud_palabra = len(palabra_a_adivinar)

# Inicializa la palabra a mostrar con guiones bajos
palabra_mostrada = ["_"] * longitud_palabra

intentos_maximos = 6
intentos = 0

while intentos < intentos_maximos:
    # Muestra la palabra actual
    print(" ".join(palabra_mostrada))

    # Pide al jugador que ingrese una letra
    letra = input("Ingresa una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa una sola letra válida.")
        continue

    # Verifica si la letra está en la palabra
    if letra in palabra_a_adivinar:
        for i in range(longitud_palabra):
            if palabra_a_adivinar[i] == letra:
                palabra_mostrada[i] = letra
        if "".join(palabra_mostrada) == palabra_a_adivinar:
            print("¡Felicidades! Has adivinado la palabra:", palabra_a_adivinar)
            break
    else:
        intentos += 1
        print("Letra incorrecta. Intentos restantes:", intentos_maximos - intentos)

if intentos == intentos_maximos:
    print("Lo siento, has agotado todos los intentos. La palabra era:", palabra_a_adivinar)
