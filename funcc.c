#include <stdio.h>
#include <stdlib.h>

extern int  calc(int a,int b);

int main(int argc, char **argv){

int BAdolar =  atoi(argv[1]);
int cotizacion =  atoi(argv[2]);


int BAMonedaDeseada = calc(1000, 1);

return BAMonedaDeseada;
}
