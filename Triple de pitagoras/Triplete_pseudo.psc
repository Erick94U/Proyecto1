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
