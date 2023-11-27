import time
import random

caso1_range = 500
caso2_range = 1000
caso3_range = 10000
ejecuciones = 100

# algoritmo de ordenamiento
def bubble_sort(lista):
    inicio = time.time()
    long = len(lista)
    for i in range(long):
        for j in range(long-i-1):
            if lista[j] > lista[j+1]:
                (lista[j],lista[j+1]) = (lista[j+1],lista[j])
    fin = time.time()
    return fin - inicio

# crea las listas dependiendo el caso
def mkSet(n):
    lista = [0] * n
    if n == caso1_range:
        for i in range(n):
            lista[i] = numRandom(n,0)
    elif n == caso2_range:
        for i in range(n):
            lista[i] = numRandom(n)
    elif n == caso3_range:
        for i in range(n):
            lista[i] = numRandom(n)
    return lista

# devuelve un numero int o float al azar
def numRandom(n,k=None):
    num = random.randint(0,n)
    if num%2 == 0 and k == None:
        return random.randint(0,n)
    else:
        return round(random.uniform(0.5,n),2)

# ejecuta el algoritmo de ordenamiento un numero determinado de ejecuciones
def exec(l):
    tt = 0
    for i in range(ejecuciones):
            t_ejecucion = bubble_sort(l)
            tt += t_ejecucion
    return tt

# mensaje de salida una vez que se terminaron todas las ejecuciones
def message(n,rango,tt):
    print('Despues de {} ejecucion(es) de ordenamiento para el caso {} con un conjunto de {} datos, el tiempo promedio fue de:'.format(ejecuciones,n,rango))
    print('{:f}'.format(tt/ejecuciones))

# punto de entrada de los casos
def caso(n):
    if n == 1:
        l = mkSet(caso1_range) 
        tt = exec(l)
        message(n,caso1_range,tt)
    elif n == 2:
        l = mkSet(caso2_range)
        tt = exec(l)
        message(n,caso2_range,tt)
    elif n == 3:
        l = mkSet(caso3_range)
        tt = exec(l)
        message(n,caso3_range,tt)

#l = mkSet(caso2_range)
#l = mkSet(caso2_range)
#l = mkSet(caso3_range)
#bubble_sort(l)

#caso(1)
caso(2)
#caso(3)