#include <stdio.h>
#include <stdlib.h>

extern int  calc(int,int);

int main(int argc, char **argv){

int BAdolar =  atoi(argv[1]);
int cotizacion =  atoi(argv[2]);


int BAMonedaDeseada = calc(BAdolar, cotizacion);



printf("%d\n",BAMonedaDeseada);


return 0;
}
