public class BuscaLista{
    public static int busca(int[] lista, int chave){
        for(int i = 0; i < lista.length; i ++){
            if(lista[i] == chave) {
                return i; //para chave encontrada
            }
        }
        return -1;// para chave não encontrada.
    }
    //algorítmo
    public static void main(String[] args) {
        int[] lista = {20, 5, 15, 24, 67, 45, 1, 76, 21, 11};
        int chave = 45;

        int posicao = busca(lista, chave);

        if (posicao != -1){
            System.out.printf("Posição da Chave %d na lista: %d\n", chave, posicao);
        } else{
            System.out.printf("A chave %d não se encontra na lista\n", chave);
        }
    }
}