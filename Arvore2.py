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


def em_ordem(raiz):## define a função em ordem com o paramentro raiz, representando o nó raiz da arvore binária
    if not raiz: # verificação de se o nó raiz é nulo e se for o retorno é nada
        return
    em_ordem(raiz.esquerda)# chama a função em ordem rescursivamente para percorrer a subárvore a esquerda do nó atual
    print(raiz.chave,", ",end=""), #imprime a chave do no atual seguida de uma virgula sem quebrar a linha 
    em_ordem(raiz.direita)# mesma coisa da linha 36 porém a direita


def pre_ordem(raiz): #define a função pre ordem com um parametro (raiz)
    if not raiz: # verifica, se for none, retorna
        return
    print(raiz.chave,", ",end=""), #imprime a chave do nó atual
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)# ambas chamam a função recursivamente pra percorrer a subarvore (direita e esquerda) do nó atual

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave,", ",end=""),# mesma definição dos anteriores, uma reescrita


def insere(raiz,nodo):# Define a função insere, que insere um novo nó (nodo) em uma árvore binária de pesquisa. A função recebe 2 parametros,sendo raiz (nó raiz da árvore) e nodo(novo nó)
    if raiz is None: # verificação, se raiz for vazia, insere um novo nó (nodo)
        raiz = nodo
    elif raiz.chave < nodo.chave: # Se a chave do nó raiz for menor do que a chave do novo nó, seguindo as regras e se a raiz a direita for vazia, então a raiz a direita recebe o novo no
        if raiz.direita is None:
            raiz.direita = nodo
        else: # se raiz a direita estiver ocupada, a função insere será chamada para inserir o novo nó a direita
            insere(raiz.direita,nodo)
    else: # Caso acondição do elif na linha 59 não bater, mesmo feito dentro do if e else das linhas 60 - 62 acontece só que a esquerda
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda,nodo)


def busca(raiz, valor): # definição da função de busca, recebe a raiz da arvore como parametro e valor, como o valor a ser buscado.
    if raiz is None:# se não tiver raiz, só retorna
        return None
    if raiz.chave == valor: # se a raiz for o valor buscado, retorna ela
       return raiz
    if raiz.chave < valor:# se a chave do nó raiz  for menor do que ovalor, seguindo a regra, a busca segue na subarvore a direita. 
        return busca(raiz.direita,valor)
    return busca(raiz.esquerda,valor) # Se a chave do nó raiz for maior que o valor, a busca continua na subarvore a esquerda


#Utilizando as funções e a classe NodoArvore
raiz = NodoArvore(30)# nó raiz de chave 30 criado
for chave in [28,25,16,11,9]: # usa um for para inserir um novo nó para cada valor
    nodo = NodoArvore(chave)
    insere(raiz,nodo) # o insere pega os nós criados e os insere na arvore
    

imprimir_arvore(raiz) # a arvore é printada

print("Em ordem:")
em_ordem(raiz)
print("\n\nPré ordem:")
pre_ordem(raiz)
print("\n\nPós ordem:")
pos_ordem(raiz)
# a arvore vai ser inserida nas três ordens de ordenação
print("\n")
valor = 16 # define o valor a ser buscado
resultado = busca(raiz,valor) # atribui o que acontece em busca ao resultado
if resultado: # se 16 estiver dentro de resultado como encontrado vai rodar essa linha
    print("Busca pelo valor {}: Sucesso!".format(valor))
else:# se não, roda essa
    print("Busca pelo valor {}: Falha!".format(valor))





    
