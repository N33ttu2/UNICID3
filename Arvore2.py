class NodoArvore:
    def __init__(self,chave = None,
                 esquerda = None,
                 direita = None): #atribui o valo  do paramentro a instacia
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self): # define o método construtor/inicializador da classe, representa como uma string
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)
# o % serve pra armazenar os valores do atributo e and é um verificador de valores se existem ou não a esquerda/direita
# retorna o valor se tiver e se não retorna false ou "none"
#fora da classe

# melhorar esse codígo abaixo para imprimir corretamente a arvore binária
#----------------------------------------------------------------------------
def imprimir_arvore(raiz, espaco = "", marcador_raiz = "    "): # raiz da arvore/subarvore que sera impressa , espaco 
    # uma sreing usada para alinhar visualmente os nós da impressao
    # marcador raiz é uma identação, indica a profundidade do nó na árvore, o padrão é "   " quatro espaços vazios
    if raiz is not None: # Verifica se a raiz fornecida não é none( ou se arvore não esta vazia)
        if espaco == "": # verfica se o paramentro de espaco está vazio, usado pra dizes se estamos na raiz ou em um nó filho(quando espaço está vazio apenas o valor da chave é impresso)
            print(raiz.chave)#imprime a chave do no atual
        else: # caso não seja raiz ( se espaço não esta vazio), imprime o no com os filhos
            print(espaco[:-len(marcador_raiz)]+"└─", raiz.chave) # imprime a have do no atual alianhando com a impressão para indicar sua pos na arvore e mostrar a conec com os filhos
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


#Utilizando as funções e a classe NodoArvore
raiz = NodoArvore(30)
for chave in [28,25,16,11,9]:
    nodo = NodoArvore(chave)
    insere(raiz,nodo)
    

imprimir_arvore(raiz)

print("Em ordem:")
em_ordem(raiz)
print("\n\nPré ordem:")
pre_ordem(raiz)
print("\n\nPós ordem:")
pos_ordem(raiz)

print("\n")
valor = 16
resultado = busca(raiz,valor)
if resultado:
    print("Busca pelo valor {}: Sucesso!".format(valor))
else:
    print("Busca pelo valor {}: Falha!".format(valor))





    
