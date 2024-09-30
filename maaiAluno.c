#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definindo a struct Aluno
typedef struct AlunoS
{
    int matricula;
    char nome[100];
    char dataNasc[11];  // Corrigido o tamanho para comportar "10/11/2003" + '\0'
    char cargo[100];
    float salary[4];    // Array de salários, cada posição deve ser preenchida individualmente
} Aluno;

int main(){
    // Declarando um Aluno
    Aluno a;   
    a.matricula = 1212;

    // Usando strcpy para strings
    strcpy(a.nome, "Duana");
    strcpy(a.dataNasc, "10/11/2003");  // Agora cabe na string
    strcpy(a.cargo, "Peuta");

    // Atribuindo valores ao array salary
    a.salary[0] = 2122.00;  // Exemplo de atribuição ao array
    a.salary[1] = 2500.50;
    a.salary[2] = 3200.00;
    a.salary[3] = 1500.75;

    // Exibindo valores para verificação
    printf("Matricula: %d\n", a.matricula);
    printf("Nome: %s\n", a.nome);
    printf("Data de Nascimento: %s\n", a.dataNasc);
    printf("Cargo: %s\n", a.cargo);
    printf("Salário 1: %.2f\n", a.salary[0]);

    return 0;
}
