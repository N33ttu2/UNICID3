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
    print(raiz.chave,", ",end=""),
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave,", ",end=""),


def insere(raiz,nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita,nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda,nodo)


def busca(raiz, valor):
    if raiz is None:
        return None
    if raiz.chave == valor:
       return raiz
    if raiz.chave < valor:
        return busca(raiz.direita,valor)
    return busca(raiz.esquerda,valor)

###################################################################################
def calcularAlturaNo(raiz):
    if not raiz:
        return
    calcularAlturaNo(raiz.esquerda)
    calcularAlturaNo(raiz.direita)
    
    if not raiz.esquerda and not raiz.direita:
        raiz.altura = 0

    if raiz.esquerda and not raiz.direita:
        raiz.altura = raiz.esquerda.altura + 1

    if not raiz.esquerda and raiz.direita:
        raiz.altura = raiz.direita.altura + 1

    if raiz.esquerda and raiz.direita:
        if raiz.esquerda.altura >= raiz.direita.altura:
            raiz.altura = raiz.esquerda.altura + 1
        else:
            raiz.altura = raiz.direita.altura + 1

def em_ordemAltura(raiz):
    if not raiz:
        return
    em_ordemAltura(raiz.esquerda)
    print(raiz.altura,", ",end=""),
    em_ordemAltura(raiz.direita)


def calcularFatorBalanceamentoNo(raiz,noDesbalanceado = None):
    if not raiz:
        return noDesbalanceado
    noDesbalanceado = calcularFatorBalanceamentoNo(raiz.esquerda,noDesbalanceado)
    noDesbalanceado = calcularFatorBalanceamentoNo(raiz.direita,noDesbalanceado)

    if not raiz.esquerda and not raiz.direita:
        fator = 0
    if raiz.esquerda and not raiz.direita:
        fator = raiz.esquerda.altura - (-1)
    if not raiz.esquerda and raiz.direita:
        fator = (-1) - raiz.direita.altura
    if raiz.esquerda and raiz.direita:
        fator = raiz.esquerda.altura - raiz.direita.altura

    if fator < 0:
        fator = fator *(-1)

    if not noDesbalanceado and fator > 1:
        noDesbalanceado = raiz.chave
    return noDesbalanceado



def rotacaoEsqEsq(raiz):
    aux = NodoArvore(raiz.chave)
    if raiz.direita:
        aux.direita = raiz.direita
    raiz.chave = raiz.esquerda.chave
    raiz.esquerda = raiz.esquerda.esquerda
    raiz.direita = aux

def rotacaoEsqDir(raiz):
    return

def rotacaoDirEsq(raiz):
    return

def rotacaoDirDir(raiz):
    aux = NodoArvore(raiz.chave)
    if raiz.esquerda:
        aux.esquerda = raiz.esquerda
    raiz.chave = raiz.direita.chave
    raiz.direita = raiz.direita.direita
    raiz.esquerda = aux

    
    

###################################################################################

#Utilizando as funções e a classe NodoArvore
raiz = NodoArvore(15)
for chave in [10,5]:
    nodo = NodoArvore(chave)
    insere(raiz,nodo)
    

imprimir_arvore(raiz)
print("Em ordem:")
em_ordem(raiz)
calcularAlturaNo(raiz)
print("         ")
em_ordemAltura(raiz)
print("\nO nó desbalanceado é:",calcularFatorBalanceamentoNo(raiz))
rotacaoEsqEsq(raiz)
imprimir_arvore(raiz)






    
