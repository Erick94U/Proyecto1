#Triples de Pitagoras

Un triángulo recto puede tener lados cuyas longitudes sean valores enteros. Un conjunto de 
tres valores enteros para los lados de un triángulo recto se conoce como triple de Pitágoras. 
Estos tres lados deben satisfacer la relación que establece que la suma de los cuadrados de 
dos lados es igual al cuadrado de la hipotenusa. Encuentre todos los triples de Pitágoras para 
lado1, lado2, y la hipotenusa, que no sean mayores de 500. Use un ciclo for triplemente anidado 
para probar todas las posibilidades. Este método es un ejemplo de la computación de fuerza bruta 

Lenguaje C++

#include <iostream>
using namespace std;

int main() {
    int numero;

    // Solicitar al usuario un número entero positivo
    do {
        cout << "Ingrese un número entero positivo: ";
        cin >> numero;
    } while (numero <= 0);

    // Mostrar las opciones de triángulos
    cout << "Seleccione el tipo de triángulo rectángulo a visualizar:" << endl;
    cout << "1. Triángulo rectángulo con catetos en la izquierda y base abajo." << endl;
    cout << "2. Triángulo rectángulo con catetos en la izquierda y base arriba." << endl;
    cout << "3. Triángulo rectángulo con catetos en la derecha y base abajo." << endl;
    cout << "4. Triángulo rectángulo con catetos en la derecha y base arriba." << endl;

    int opcion;
    cin >> opcion;

    // Mostrar el triángulo seleccionado
    switch (opcion) {
        case 1:
            // Triángulo rectángulo con catetos en la izquierda y base abajo
            for (int i = 1; i <= numero; i++) {
                for (int j = 1; j <= i; j++) {
                    cout << "* ";
                }
                cout << endl;
            }
            break;

        case 2:
            // Triángulo rectángulo con catetos en la izquierda y base arriba
            for (int i = numero; i >= 1; i--) {
                for (int j = 1; j <= i; j++) {
                    cout << "* ";
                }
                cout << endl;
            }
            break;

        case 3:
            // Triángulo rectángulo con catetos en la derecha y base abajo
            for (int i = 1; i <= numero; i++) {
                for (int j = 1; j <= numero - i; j++) {
                    cout << "  ";
                }

##lenguaje python

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

##Lenguaje Pseudocodigo

Algoritmo TriplesDePitagoras
    Definir valor_max Como Entero
    valor_max <- 500
    
    Escribir "Triples de Pitágoras menores o iguales a 500", ":"
    
    Para ladoA <- 1 Hasta valor_max Hacer
        Para ladoB <- 1 Hasta valor_max Hacer
            Para hipotenusa <- 1 Hasta valor_max Hacer
                Si (ladoA * ladoA + ladoB * ladoB = hipotenusa * hipotenusa) Entonces
                    Escribir ", LadoA:", ladoA, ", LadoB:", ladoB, ", Hipotenusa:", hipotenusa
                Fin Si
            Fin Para
        Fin Para
    Fin Para
    
FinAlgoritmo


