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

