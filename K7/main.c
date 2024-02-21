#include <stdio.h>

int busca(int lista[], int tamanho, int chave){
    for (int i = 0; i< tamanho; i++){
        if (lista[i] == chave){
            return i;
        }
    }
    return -1;
}//Metodo

int main(){
    int lista[] = {20, 5, 15, 24, 67,45, 1 ,76,21, 11};
    //calcula o tamanho da lista
    int tamanho = sizeof(lista) / sizeof(lista[0]);

    int chave = 45;
    int posicao = busca(lista, tamanho, chave);

    if (posicao != -1){
        printf("Posicao da chave %d na lista: %d\n", chave, posicao);
    } else
    {
        printf("A chave %d nao se encontra na lista:\n", chave);
    }
    
    return 0;
}
