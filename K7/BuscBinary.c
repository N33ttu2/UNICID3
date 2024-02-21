#include <stdio.h>

int buscaB(int lista[], int tamanho, int chave){
    int pos_ini = 0;
    int pos_fim = tamanho - 1;

    while (pos_ini <= pos_fim)
    {
        int pos_meio = (pos_fim + pos_ini) / 2;

        if (lista[pos_meio] == chave)
        {
            return pos_meio; // cahve encontrada
        }else if (lista[pos_meio] < chave)
        {
            pos_ini = pos_meio + 1;
        } else
        {
            pos_fim = pos_meio - 1;
        }
    
        
        
        
    }
    return -1;// chav nao encintrada
}// metodo

int main() {
    int lista[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int tamanho = sizeof(lista) / sizeof(lista[0]);
    int chave = 5;
    int resultado = buscaB(lista, tamanho, chave);
    if (resultado != -1) {
        printf("Elemento encontrado na posição: %d\n", resultado);
    } else {
        printf("Elemento não encontrado na lista.\n");
    }
    return 0;
}