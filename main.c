#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura de um nó
typedef struct Node {
    char* nome;         // Ponteiro para armazenar o nome
    struct Node* prox;  // Ponteiro para o próximo nó
} Node;

Node* createNode(const char* nome) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Erro ao alocar memória para o nó.\n");
        exit(1);
    }

    newNode->nome = (char*)malloc(strlen(nome) + 1); // Alocando memória para o nome
    if (!newNode->nome) {
        printf("Erro ao alocar memória para o nome.\n");
        exit(1);
    }

    strcpy(newNode->nome, nome);  // Copiando o nome
    newNode->prox = NULL;         // Inicializando o próximo nó como NULL
    return newNode;
}

void insertEnd(Node** cabeca, const char* nome) {
    Node* newNode = createNode(nome);
    
    if (*cabeca == NULL) {
        // Se a lista estiver vazia, o novo nó aponta para si mesmo
        *cabeca = newNode;
        newNode->prox = newNode;
    } else {
        Node* temp = *cabeca;

        // Encontrando o último nó
        while (temp->prox != *cabeca) {
            temp = temp->prox;
        }

        // Inserindo o novo nó no final
        temp->prox = newNode;
        newNode->prox = *cabeca; // Aponta para o primeiro nó
    }
}

void displayList(Node* head) {
    if (head == NULL) {
        printf("A lista está vazia.\n");
        return;
    }

    Node* temp = head;
    do {
        printf("%s ", temp->nome);
        temp = temp->prox;
    } while (temp != head);
    printf("\n");
}

Node* busca(Node* cabeca, const char* nome){
    if (cabeca == NULL){
        printf("A lista está vazia\n");
        return NULL;
    }
    Node* temp = cabeca;
    do {
        if (strcmp(temp->nome, nome) == 0){
            return temp; // Nome encontrado
        }
        temp = temp->prox;
    } while (temp != cabeca);

    return NULL; // Nome não encontrado
}

int countNodes(Node* cabeca){
    if (cabeca == NULL) {
        return 0; // Lista vazia, contagem 0
    }

    int count = 0;
    Node* temp = cabeca;
    do {
        count++; // Incrementa o contador
        temp = temp->prox;
    } while (temp != cabeca);

    return count;
}

void freeList(Node** head) {
    if (*head == NULL) return;

    Node* current = *head;
    Node* next;

    do {
        next = current->prox;
        free(current->nome);
        free(current);
        current = next;
    } while (current != *head);

    *head = NULL;
}

int main() {
    Node* cabeca = NULL; // Lista vazia

    insertEnd(&cabeca, "Mariana");
    insertEnd(&cabeca, "Leticia");

    printf("Lista:\n");
    displayList(cabeca);

    // Buscar um nome na lista
    const char* nameToSearch = "Leticia";
    Node* foundNode = busca(cabeca, nameToSearch);
    if (foundNode) {
        printf("Nome '%s' encontrado.\n", nameToSearch);
    } else {
        printf("Nome '%s' não foi encontrado.\n", nameToSearch);
    }

    // Contando o número de nós
    int numerodeGente = countNodes(cabeca);
    printf("O número de participantes é: %d\n", numerodeGente);

    // Liberando a memória
    freeList(&cabeca);

    return 0;
}
