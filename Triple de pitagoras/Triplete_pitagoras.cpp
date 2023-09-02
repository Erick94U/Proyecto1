
#include <iostream>

int main() { 
int max = 500;

    std::cout<<"TRIPLE DE PITAGORAS MENOR O IGUAL A 500" <<std:: endl;

    for(int ladoA = 1; ladoA<max; ++ladoA) {
        for(int ladoB = ladoA; ladoB<=max; ++ladoB){
            for(int hipotenusa = ladoB; hipotenusa<=max; ++hipotenusa){
                if (ladoA * ladoA + ladoB * ladoB == hipotenusa*hipotenusa){
                    std::cout<<"("<< ladoA <<","<< ladoB <<","<< hipotenusa <<")"<< std :: endl;
                     }
                }


            }
        
        
        }
    
    return 0;
}