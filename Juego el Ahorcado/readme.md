#Juego El Ahorcado

El juego consiste en que el usuario debe de adivinar las palabras
solamente tendrá 5 oportunidades.

##Lenguace C++

#include <iostream>
#include <string>
using namespace std;

int main() {
    string palabras[] = {"hola", "mundo", "adios"};
    int numPalabras = sizeof(palabras) / sizeof(palabras[0]);
    string palabraAdivinar = palabras[rand() % numPalabras]; // Selecciona una palabra al azar
    int longitudPalabra = palabraAdivinar.length();
    string palabraAdivinada(longitudPalabra, '_');
    int intentosMaximos = 5;
    int intentos = 0;
    bool adivinada = false;
    
    cout << "Adivina la palabra: " << palabraAdivinada << endl;

    while (intentos < intentosMaximos && !adivinada) {
        char letra;
        cout << "Ingresa una letra: ";
        cin >> letra;

        bool letraAdivinada = false;

        for (int i = 0; i < longitudPalabra; i++) {
            if (palabraAdivinar[i] == letra) {
                palabraAdivinada[i] = letra;
                letraAdivinada = true;
            }
        }

        if (!letraAdivinada) {
            intentos++;
        }

        cout << "Palabra actual: " << palabraAdivinada << endl;

        if (palabraAdivinar == palabraAdivinada) {
            cout << "¡Felicidades! Has adivinado la palabra: " << palabraAdivinar << endl;
            adivinada = true;
        }
    }

    if (!adivinada) {
        cout << "Lo siento, has alcanzado el número máximo de intentos. La palabra era: " << palabraAdivinar << endl;
    }

    return 0;
}

##Lenguaje Python

def main():
    numero = int(input("Ingrese un número entero positivo: "))
    
    # Validar que el número sea positivo
    if numero <= 0:
        print("Por favor, ingrese un número entero positivo.")
        return

    # Mostrar las opciones de triángulos
    print("Seleccione el tipo de triángulo rectángulo a visualizar:")
    print("1. Triángulo rectángulo con catetos en la izquierda y base abajo.")
    print("2. Triángulo rectángulo con catetos en la izquierda y base arriba.")
    print("3. Triángulo rectángulo con catetos en la derecha y base abajo.")
    print("4. Triángulo rectángulo con catetos en la derecha y base arriba.")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    # Mostrar el triángulo seleccionado
    if opcion == 1:
        # Triángulo rectángulo con catetos en la izquierda y base abajo
        for i in range(1, numero + 1):
            print("* " * i)
    elif opcion == 2:
        # Triángulo rectángulo con catetos en la izquierda y base arriba
        for i in range(numero, 0, -1):
            print("* " * i)
    elif opcion == 3:
        # Triángulo rectángulo con catetos en la derecha y base abajo
        for i in range(1, numero + 1):
            print("  " * (numero - i) + "* " * i)
    elif opcion == 4:
        # Triángulo rectángulo con catetos en la derecha y base arriba
        for i in range(numero, 0, -1):
            print("  " * (numero - i) + "* " * i)
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

