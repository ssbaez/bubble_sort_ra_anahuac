import time
import random

caso1_range = 500
caso2_range = 1000
caso3_range = 10000
ejecuciones = 100

def bubble_sort(lista):
    inicio = time.time()
    long = len(lista)
    for i in range(long):
        for j in range(long-i-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    fin = time.time()
    return fin - inicio

def mkSet(n):
    lista = [0] * n
    if n == caso1_range:
        for i in range(n):
            lista[i] = round(numRandom(0.5,n),2)
    elif n == caso2_range:
        for i in range(n):
            lista[i] = round(numRandom(0,n))
    elif n == caso3_range:
        for i in range(n):
            lista[i] = round(numRandom(0,n))

    return lista

def numRandom(i,f):
    return random.uniform(i,f)

def exec(l):
    tt = 0
    for i in range(ejecuciones):
            t_ejecucion = bubble_sort(l)
            tt += t_ejecucion
    return tt

def message(n,tt):
    print('Despues de {} ejecuciones de ordenamiento para el caso {}, el tiempo promedio fue de:'.format(ejecuciones,n))
    print(tt/ejecuciones)

def caso(n):
    if n == 1:
        l = mkSet(caso1_range)
        tt = exec(l)
        message(n,tt)
    elif n == 2:
        l = mkSet(caso2_range)
        tt = exec(l)
        message(n,tt)
    elif n == 3:
        l = mkSet(caso3_range)
        tt = exec(l)
        message(n,tt)      

caso(3)

