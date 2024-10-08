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

# Função para imprimir a árvore de forma hierárquica
def imprimir_Arvore(raiz, nivel=0, prefixo=""):
    if raiz is not None:
        # Primeiro imprime a subárvore da direita
        imprimir_Arvore(raiz.direita, nivel + 1, "    " * nivel + "L ")

        # Imprime o valor da raiz atual com o nível de profundidade
        print("    " * nivel + prefixo + str(raiz.chave))

        # Depois imprime a subárvore da esquerda
        imprimir_Arvore(raiz.esquerda, nivel + 1, "    " * nivel + "L ")

# Criando a árvore
raiz = NodoArvore(20)
raiz.esquerda = NodoArvore(8)
raiz.direita = NodoArvore(30)

# Adicionando mais nós
raiz.esquerda.esquerda = NodoArvore(14)
raiz.esquerda.direita = NodoArvore(10)
raiz.direita.esquerda = NodoArvore(5)
raiz.direita.esquerda.direita = NodoArvore(90)
raiz.direita.direita = NodoArvore(62)

# Chamando a função para imprimir a árvore
print("Estrutura da árvore:")
imprimir_Arvore(raiz)