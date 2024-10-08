class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita  # Recebendo/armazenando um nó possui valor, o nó da esquerda e da direita

    # Imprimindo
    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda.chave if self.esquerda else None,
            self.chave,
            self.direita.chave if self.direita else None
        )

# Criando a árvore
raiz = NodoArvore(20)
raiz.esquerda = NodoArvore(8)
raiz.direita = NodoArvore(30)

# Adicionando mais nós
raiz.esquerda.esquerda = NodoArvore(14)
raiz.esquerda.direita = NodoArvore(10)
raiz.direita.esquerda = NodoArvore(5)
raiz.direita.esquerda.direita = NodoArvore(90)  # Corrigido para ser um NodoArvore
raiz.direita.direita = NodoArvore(62)

# Imprimindo a árvore
print("A Árvore é: ", raiz)
print("Filho à esquerda:", raiz.esquerda)
print("Filho à direita:", raiz.direita)

# Função para imprimir a árvore de forma mais legível
def imprimir_Arvore(raiz, espaco="", marcador_raiz="  "):
    if raiz is not None:
        if espaco == "":
            print(raiz.chave)
        else:
            print(espaco[:len(marcador_raiz)] + "¬", raiz.chave)  # Adiciona um caractere de linha
        imprimir_Arvore(raiz.direita, espaco + marcador_raiz, marcador_raiz)
        imprimir_Arvore(raiz.esquerda, espaco + marcador_raiz, marcador_raiz)

# Chamando a função para imprimir a árvore
print("\nEstrutura da árvore:")
imprimir_Arvore(raiz)
