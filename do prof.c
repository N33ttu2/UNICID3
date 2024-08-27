Como colocar nomeaux em **n usando len?

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
/* Alocação de mem dinam*/
int main(void) {
	setlocale(LC_ALL, "Portuguese_Brazil.1252");
	int*x;
	x = (int *) malloc (10* sizeof(int));
	
	x[0] = 15; x[1] = 29; x[2] = 30;
	x[3] = 11; x[4] = 82; x[5] = 60;
	
	int i;
	
	for (i = 0; i < 10;i++){
		printf("%d, ",x[i]);
	}
	free(x);  
	
	char *nome;
	lendoNome(&nome);
	printf("\nDigite seu Nome ");
	gets(auxNome);
	*n (char *) malloc(strlen(auxNome)*sizeof(char));
	strcpy(*n, auxNome);
		
}
void lendoNome(char **n){
	char nomeAux[200];
	printf("Digite seu nome: ");
	gets(nomeAux);
	LendoNome(**n) = nomeAux;
}
	return 0;
