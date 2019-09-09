#include <stdio.h>
#include <stdlib.h>
#include "Tarea4.h"
#include <math.h>


int f_hash( int a, int c, int m , int x)
{   

    /*
    Params:
    - a: entero
    - m: tamano tabla hash
    - c: entero
    - x: numero a ser "hasheado"
    Returns:
    hashing de numero x
    */
    int x_hasheado=(a*x+c)%m;
    return x_hasheado;
}

int insertar(int *H, int m, int k)
{
    int pos=f_hash(a,c,m,k);

   if (H[pos]==-1)
    {
        H[pos]=k;
        return 1;
    }
    pos++;
    while(pos<m)
    {
        if (H[pos]==-1)
        {
            H[pos]=k;
            return 2;
        }
        pos++;
    }
    return 0;

    


    /*
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a insertar
    Returns:
    - 0: No se pudo insertar en la tabla
    - 1: Si fue posible sin cambios insertar en la tabla
    - 2: Si fue posible con cambios insertar en la tabla
    */
}

int buscar(int *H, int m, int k)
{
    int num_search=f_hash(a,c,m,k);
    while(num_search<m && H[num_search] !=k)
    {
        num_search++;
    }
    if(H[num_search]==k)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    /*
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a buscar
    Returns:
    - 0: numero k no encontrado
    - 1: se encontro el numero k
    */

}

int eliminar(int *H, int m, int k)
{
    int num_delete=f_hash(a,c,m,k);
    while(num_delete<m && H[num_delete] !=k)
    {
        num_delete++;
    }
    if(H[num_delete]==k)
    {
        H[num_delete]=-1;
        return 1;
    }
    else
    {
        return 0;
    }
    

    /*
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a eliminar
    Returns:
    - 0: Numero no se encuentra en la tabla
    - 1: El numero fue eliminado correctamente
    */
   return -1;
}

float FC (int *H, int m)
{
    int count=0;
    for(int i =0;i<m;i++)
    {
        if(H[count] !=-1)
        {
            count++;
        }
    } //buckets utilizados/buckets totales
     float fact_carga= floorf(count/m);
     
    /*
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    Returns:
    Factor de carga con un deciaml
    */
   
   return fact_carga;
}    
