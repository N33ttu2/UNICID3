def busca (lista, chave):
    for i, elemento in enumerate(lista):
        if elemento == chave:
            return i # = chave encontrada
    return -1 # = chave n encontrada(fora do for)
    # Acima -> algorítmo da busca
    # Abaixo -> MAIN
def main():
    lista = [20, 5, 15, 24, 67, 45, 1, 76, 21, 11]
    chave = 45

    posicao = busca(lista, chave)

    if posicao != -1: 
        print(f"Posição da chave {chave} na lista: {posicao}")
    else:
        print(f"A chave {chave} não se encontra na lista.")
#MAIN para executar o algorítmo com a busca.
if __name__ == "__main__":
    main()