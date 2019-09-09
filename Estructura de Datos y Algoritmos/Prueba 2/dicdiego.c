#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char dic[10][100] = {
    "pieza cubica para juegos de azar",         //0 dado
    "fenomeno acustico",                        //1 eco
    "piel de animal",                           //2 pellejo
    "tira o banda elastica",                    //3 goma
    "saludo informal",                          //4 hola
    "maquina electronica",                      //5 computador
    "dejer caer algo",                          //6 tirar
    "unidad de masa",                           //7 kilo
    "maleta grande para transportar cosas",     //8 baul
    "sensacion de temperatura alta"             //9 calor
};

int pow(int num, int p){
    int val = 1;
    for(int i = 0; i<p; i++){
        val = num * val;
    }
    return val;
}

int f_hash(char a[], int m){
    int suma = 0;
    for(int i = 0; i < strlen(a); i++)
    {
        int potencia = pow(10, i);
        suma = ((int)a[i] * potencia) + suma;
    }
    return suma % m;
}

char *obtener(char a[], int m){
    int hash = f_hash(a, m);
    char *sig = dic[hash];
    return sig;
}

void insertar(char *a, char *s, int m){
    int hash = f_hash(a, m);
    if (strcmp(dic[hash], "") == 0 ){
        strcpy(dic[hash], s);
        printf("Palabra cambiada\n");
    }else{
        printf("Puesto ocupado\n");
    }
    
}

void eliminar(char a[], int m){
    int hash = f_hash(a, m);
    strcpy(dic[hash], "\0");
}

int main(){
    //char dic[10][100];
    char text[10];
    char *significado;
    int menu = -1;
    /*printf("Ingrese una palabra para generar su hash: ");
    scanf("%s",text);
    int hash = f_hash(text, 10, strlen(text));
    printf("su valor hash es: %d\n", hash);*/
    printf("Palabras del diccionario:\n");
    printf("dado\n"); printf("eco\n"); printf("pellejo\n"); printf("goma\n"); printf("hola\n");
    printf("computador\n"); printf("tirar\n"); printf("kilo\n");printf("baul\n"); printf("calor\n");
    while(menu != 0){
        
        printf("-Obtener una definicion     [1]\n");
        printf("-Insertar una nueva palabra [2]\n");
        printf("-Eliminar una palabra       [3]\n");
        printf("-Salir del programa         [0]\n");
        printf("\n>> ");
        scanf("%d", &menu);
        if (menu == 0) {
            break;
        }else if (menu == 1){
            printf("Ingrese la palabra: ");
            scanf("%s", text);
            significado = obtener(text, 10);
            printf("su significado es:%s\n", significado);
        }else if (menu == 2){
            printf("Ingrese la palabra: ");
            scanf("%s", text);
            printf("Ingrese el significado: ");
            scanf("%s", significado);
            insertar(text, significado, 10);
            printf("---CAMBIO COMPLETADO---\n");
        }else if (menu == 3){
            printf("Ingrese la palabra: ");
            scanf("%s", text);
            eliminar(text, 10);
            printf("---PALABRA ELIMINADA---\n");
        }
        
    }
    /*scanf("%s", text);
    significado = obtener(text, 10);
    printf("%s", significado);*/
    return 0;
}