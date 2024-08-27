#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Para usar strcpy

// Definição das estruturas fora da função main
struct Data {
    int dia;
    int mes;
    int ano;
};

struct Conta {
    int num_Conta;
    char tipo_conta;
    char nome[80];
    float saldo;
    struct Data dataAbertura;
    struct Data ultPagamento;
};

// Funções para imprimir dados
void imprimir(struct Conta p) {
    printf("\nNúmero de Conta: %d", p.num_Conta);
    printf("\nTipo de Conta: %c", p.tipo_conta);
    printf("\nNome Portador: %s", p.nome);
    printf("\nSaldo: %.2f", p.saldo);
    printf("\n--------------------\n\n");
}

void imprimirData(struct Data dt, char rotulo[20]) {
    if (dt.mes < 10)
        printf("\n%s: %d/0%d/%d", rotulo, dt.dia, dt.mes, dt.ano);
    else
        printf("\n%s: %d/%d/%d", rotulo, dt.dia, dt.mes, dt.ano);
}

int main(void) {
    struct Conta pessoa3;    
    
    // Inicializando a estrutura Conta
    pessoa3.num_Conta = 1234;
    pessoa3.tipo_conta = 'c';
    strcpy(pessoa3.nome, "Juliano Souza");
    pessoa3.saldo = 100.00;
    pessoa3.dataAbertura.dia = 20;
    pessoa3.dataAbertura.mes = 8;
    pessoa3.dataAbertura.ano = 2024;
    pessoa3.ultPagamento.dia = 18;
    pessoa3.ultPagamento.mes = 2;
    pessoa3.ultPagamento.ano = 2024;
    
    // Imprimindo os dados
    imprimir(pessoa3);
    imprimirData(pessoa3.dataAbertura, "Data de Abertura");
    imprimirData(pessoa3.ultPagamento, "Último Pagamento");
    
    return 0;
}

