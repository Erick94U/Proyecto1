
valor_max = 500
print("TRIPLE DE PITAGORAS MENOR O IGUAL A ", ":")

for ladoA in range(1, valor_max + 1):
    for ladoB in range(1, valor_max + 1):
        for hipotenusa in range(1, valor_max + 1):
            if ladoA**2 + ladoB**2 == hipotenusa**2:
                print("ladoA:", ladoA, ", ladoB:", ladoB, ", hipotenusa:", hipotenusa)
