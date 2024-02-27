package desafio;
public class ExpRec{

    public static void main(String[]args){
        int base = 2;
        int expoente = 5;
        int resultado = 
    exponeciacao(base, expoente);
        System.out.println(base + "elevado a" +expoente + "é igual a" + resultado);
    }
    public static int exponeciacao(int base, int expoente){
        if (expoente == 0){
            return 1;
        }else{
            return base * exponeciacao(base, expoente - 1);
        }
    }
}
