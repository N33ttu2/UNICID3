#digamos que  queremos distribuir os seguintes numeros em uma tabela hash
#12, 44, 71, 99, 23, 8, 121, 133, 168, 144, 171, 111, 16

#Criar: For e estrutura hash
def espalhamentoInserc(valor):
    if (valor % 3) == 0:
        lista0.append(valor)
    if (valor % 3) == 1:
        lista1.append(valor)
    if (valor % 3) == 2:
        lista2.append(valor)
vetor = [12, 44, 71, 99, 23, 8, 121, 133, 168, 144, 171, 111, 16]

# Qual o valor de M? neste caso M == 2
# Lista Hash dividida em duas partes
lista0 = []
lista1 = []
lista2 = []

listaHash = [lista0, lista1, lista2] # <- vetor vazio dinamicamente alocado, composta de outras listas

for item in vetor:
    espalhamentoInserc(item)

print("lista completa: ", listaHash, "\n")
print("lista0: ", lista0)
print("lista1: ", lista1)
print("lista2: ", lista2)


#Estrutura do hash ^^^^
#Inserir valor dentro da lista