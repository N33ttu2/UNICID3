int main(){
    int idade;
    char sexo;
    float n1;
    int i;

    // Para criar o vetor, é necessário indicar o tipo de dado e o identificador.

    int num1[10]; // Vetor indicado por colchetes
    int num2[] = {1, 5, 9, 43}; // Forma correta de inicializar usando colchetes
    int num3[5] = {1, 1, 2}; // Tamanho definido, posições não usadas terão valor 0
    int num5[] = {0}; // Um elemento informado, o resto será 0
    int num4[5] = {1, 2, 3, 4, 5}; // Tamanho definido com 5 elementos, corrigido para não exceder
    int num9[5];
    char letras[100]; // Vetor de caracteres
    char vogais[5] = {'a', 'e', 'i', 'o', 'u'}; // Correção: usar chaves para caracteres
    float notasa[3] = {4, 4, 5.6999}; // Correção: chaves para inicializar float

    // Imprimindo o primeiro elemento de num2
    printf("%d\n", num2[0]);
    printf("\n\n");
    //fazendo um for pra printar o array
    for( i = 0; i <5; i++)
      printf("%d ", num3[i]);//num inteiro %d
    printf("\n\n");
    for( i = 0; i<5; i++)
    printf("%c ", vogais[i]);// char %c
    printf("\n\n");
    for(i = 0; i < 5; i++)
    printf("%.2f ", notasa[i]);

    //ler numeros diretamente do teclado
    for( i = 0; i <10; i++){
    printf("digite aqui o que voce quer na pos %d: ", i);
    scanf("%d", &num9[i]);
     }
         printf("\n\n");
     for(i = 0 ; i< 10; i++)
     printf("%d",num9[i] );
    printf("\n\n");
    return 0;
}
