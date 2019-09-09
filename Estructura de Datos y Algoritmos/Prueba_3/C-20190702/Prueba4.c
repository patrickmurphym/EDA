#include <stdio.h>
#include <stdlib.h>
#include "Prueba4.h"

//Las funciones entregadas son las dos últimas que se listan acá

char labels[5] = {'A','B','C','D','E'};

struct tree_node* newTreeNode(char data){
    struct tree_node* node = (struct tree_node*)malloc(sizeof(struct tree_node)); 
    node->data = data;
    node->left = NULL; 
    node->right = NULL; 
    return(node);
}

struct list_node* newListNode(char data){
    struct list_node* node = (struct list_node*)malloc(sizeof(struct list_node)); 
    node->data = data;
    node->next = NULL; 
    return(node);
}

//Estructura trinaria para utilizar en un árbol trinario
struct trinity {
    char data;
    struct trinity* first;
    struct trinity* second;
    struct trinity* third;
};

struct trinity* newTrinity(char data){
    struct trinity* node = (struct trinity*)malloc(sizeof(struct trinity)); 
    node->data = data;
    node->first = NULL; 
    node->second = NULL; 
    node->third = NULL;
    return(node);
}

//Función recursiva que añade nodos nuevos al árbol binario
void AddToTree(int orig, int data, struct tree_node* root){
    
    if (labels[orig] == root->data){
        if (root->left == NULL){
            root->left = newTreeNode(labels[data]);
        } else {
            root->right = newTreeNode(labels[data]);
        }
    } else {
        if (root->left != NULL){
            AddToTree(orig, data, root->left);
        }
        if (root->right != NULL){
            AddToTree(orig, data, root->right);
        }
    }
}

//Función recursiva que añade nodos nuevos al árbol trinario
void AddToTrinity(int orig, int data, struct trinity* root){
    
    if (labels[orig] == root->data){
        if (root->first == NULL){
            root->first = newTrinity(labels[data]);
        } else {
            if (root->second == NULL) {
                root->second = newTrinity(labels[data]);
            } else {
            root->third = newTrinity(labels[data]);
            }
        }
    } else {
        if (root->first != NULL){
            AddToTrinity(orig, data, root->first);
        }
        if (root->second != NULL){
            AddToTrinity(orig, data, root->second);
        }
        if (root->third != NULL){
            AddToTrinity(orig, data, root->second);
        }
    }
}

//Imprime el árbol MaxST de manera que se note los hijos de cada nodo padre
void Print(struct tree_node* root, int level){
    
    if (root != NULL){
        for (int i = 0; i < level; i++){
            printf("   ");
        }
        printf("- %c\n", root->data);
    }
    if (root->left != NULL){Print(root->left, level+1);}
    if (root->right != NULL){Print(root->right, level+1);}
}

//Imprime el árbol trinario nuevo
void PrintTrinity(struct trinity *root, int level){
    
    if (root != NULL){
        for (int i = 0; i < level; i++){
            printf("   ");
        }
        printf("- %c\n", root->data);
    }
    if (root->first != NULL){PrintTrinity(root->first, level+1);}
    if (root->second != NULL){PrintTrinity(root->second, level+1);}
    if (root->third != NULL){PrintTrinity(root->third, level+1);}
}

//Self-explanatory
void Append(struct list_node* head, char data){
    while(head->next != NULL){
        head = head->next;
    }
    head->next = newListNode(data);
}

//Busca los amigos sugeridos en los nietos del árbol trinario
void SearchFriends(struct list_node* head, struct trinity *root, int level){
    if (level == 2){
        Append(head, root->data);
    }
    if (root->first != NULL){
        SearchFriends(head,root->first,level+1);
    }
    if (root->second != NULL){
        SearchFriends(head,root->second,level+1);
    }
    if (root->third != NULL){
        SearchFriends(head,root->third,level+1);
    }
}

//Self-explanatory
void PrintList(struct list_node* head){
    if (head == NULL){
        return;
    }
    printf("%c ", head->data);
    while(head->next != NULL){
        head = head->next;
        printf("- %c", head->data);
    }
    printf("\n");
}

//Crea un árbol trinario para ordenar los datos
struct trinity* TrinityTree(int graph[5][5], int size, char data){   

    if (size == 0){
        return NULL;
    }

    int in[size];
    for (int k = 1; k < size; k++){
        if (labels[k] == data){
            in[k] = 1;
        } else {
            in[k] = 0;
        }
    }

    //Raiz corresponde al nodo A
    struct trinity* root = newTrinity(data);
    
    //Árbol con N-1 enlaces
    int tree_size = 0;
    while (tree_size < size - 1){
        int max = 0; 
        int a = -1; //Qué nodo se añade
        int b = -1; //Desde que nodo se añade 'a'
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++) {  
                //Algoritmo Prim para Matrices de Adayacencia
                if (in[j] == 1 && in[i] == 0 && i != j){ 
                    if (graph[i][j] > max && graph[i][j] != -1){
                        max = graph[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }   
        AddToTrinity(b, a, root);
        in[a] = 1;
        tree_size = tree_size + 1;
    }
    return root;
}






/* Acá están las funciones entregadas. Lo anterior son funciones que cree para completar mi propósito. */


struct tree_node* MaxST(int graph[5][5], int size){   
    /*
    Params:
    - graph: Matriz de adyacencia
    Returns:
    Puntero p que apunta al inicio del arbol MaxST
    */

    if (size == 0){
        return NULL;
    }

    //Inicializo arreglo que determina si un nodo se encuentra ya en el árbol
    int in[size];
    in[0] = 1;
    for (int k = 1; k < size; k++){
        in[k] = 0;
    }

    //Raiz del árbol corresponde al nodo A
    struct tree_node* root = newTreeNode(labels[0]);
    
    //Árbol con N-1 enlaces
    int tree_size = 0;
    while (tree_size < size - 1){
        int max = 0; 
        int a = -1; //Qué nodo se añade
        int b = -1; //Desde que nodo se añade 'a'
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++) {  
                //Algoritmo Prim para Matrices de Adayacencia
                if (in[j] == 1 && in[i] == 0 && i != j){ 
                    if (graph[i][j] > max && graph[i][j] != -1){
                        max = graph[i][j];
                        a = i;
                        b = j;
                    }
                }
            }
        }
        
        AddToTree(b, a, root);
        in[a] = 1;
        tree_size = tree_size + 1;
        
    }

    //Imprimo Árbol Resultante en terminal
    Print(root,0);

    return root;
}

struct list_node* Amigos_Sugeridos(int graph[5][5],int size, struct tree_node *tree, char name){   
    /*
    Params:
    - graph: Matriz de adyacencia
    - tree: Puntero al inicio del arbol
    - name: Caracter
    Returns:
    Puntero p que apunta al inicio de la lista con los amigos sugeridos
    */


    /*
    - Hice un nuevo árbol en donde pone como raiz al carácter de interés
    - Como originalmente estaban estructurados como árboles binarios, como máximo los nodos están conectados de a tres
    - Por eso mi estructura es un árbol trinario
    - Para buscar los amigos sugeridos solo hace falta buscar a el/los nieto/s del nuevo arbol
    */
    struct trinity* root = TrinityTree(graph, size, name);


    //Inicializo lista con valor cualquiera al cual luego le hago un by-pass
    struct list_node* head = newListNode('P');
    SearchFriends(head, root, 0);

    //Imprimo en terminal para mostrar el arbol y lista nuevas
    PrintTrinity(root,0);
    PrintList(head);

    return head->next;
}

