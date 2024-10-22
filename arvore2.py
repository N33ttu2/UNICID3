class NodoArvore:
    def __init__(self,chave = None,
                 esquerda = None,
                 direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

#fora da classe

# melhorar esse codígo abaixo para imprimir corretamente a arvore binária
#----------------------------------------------------------------------------
def imprimir_arvore(raiz, espaco = "", marcador_raiz = "    "):
    if raiz is not None:
        if espaco == "":
            print(raiz.chave)
        else:
            print(espaco[:-len(marcador_raiz)]+"└─", raiz.chave)
        imprimir_arvore(raiz.direita,espaco + marcador_raiz,marcador_raiz)
        imprimir_arvore(raiz.esquerda,espaco + marcador_raiz,marcador_raiz)            
#----------------------------------------------------------------------------
# melhorar esse codígo acima para imprimir corretamente a arvore binária


def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave,", ",end=""),
    em_ordem(raiz.direita)

def pre_ordem(raiz):
    if not raiz:
        return
    print(raiz.chave, ", ",end=""),
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave, ", ",end=""),








#Utilizando as funções e a clase NodoArvore

raiz = NodoArvore(20)
raiz.esquerda = NodoArvore(8)
raiz.direita = NodoArvore(30)
raiz.esquerda.esquerda = NodoArvore(14)
raiz.esquerda.direita = NodoArvore(10)
raiz.direita.esquerda = NodoArvore(5)
raiz.direita.esquerda.direita = NodoArvore(11)
raiz.direita.direita = NodoArvore(62)

print(raiz)
print(raiz.esquerda)
print(raiz.direita)
print(raiz.direita.esquerda)

print("\n")

imprimir_arvore(raiz)

print("\n")

em_ordem(raiz)
print("\n")
pre_ordem(raiz)
print("\n")
pos_ordem(raiz)
