#! /usr/bin/env python3 -B

from testlib import check, runtests
from copy import deepcopy
from isrecursive import *

import program02

g0 = g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = listaa = listab = listac = rad = None

#def setup():
#    global g0, g1, g2, g3, g4, g5, g6, g7, g8, listaa, listab, listac, rad
g0=[['', '', ''], ['', '', ''], ['', '', '']]
g1=[['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]
g2=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]
g3=[['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]
g4=[['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]

g5=[['', 'x', ''], ['', 'o', ''], ['', '', '']]
g6=[['', 'o', ''], ['', 'x', ''], ['', '', '']]
g7=[['', 'x', 'o'], ['', '', ''], ['', '', '']]
g8=[['', 'o', 'x'], ['', '', ''], ['', '', '']]

listaa=[g1, g2, g3, g4]
listab=[g5, g6, g7, g8]
listac=[program02.gen_tree(x) for x in listaa]
rad=None

def test_program2_1():
    '''\nsi applica il metodo tipo() a 4 diversi nodi della classe  NodoTris. 
    I 4 nodi sono radici di alberi da gioco che partono dalle seguenti configurazioni\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]\n
    [['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]\n
    '''
    args        = ''
    expected    = ['?', 'o', 'x', '-']
    explanation = "il secondo e' l'output corretto"
    lista=[y.tipo() for y in listac]
    check(lista, expected, args, explanation,'')
    return 1
    

def test_program2_2():
    '''\nsi applica il metodo esiti() a 4 diversi nodi della classe  NodoTris. 
    I 4 nodi sono radici di alberi da gioco che partono dalle seguenti configurazioni\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', 'x', 'o']]\n
    [['x', 'o', 'o'], ['x', 'x', 'o'], ['o', '', 'x']]\n
    [['o', 'x', 'x'], ['x', 'o', 'o'], ['o', 'o', 'x']]\n
    '''
    args        = ''
    expected    = [(0, 2, 3), (0, 1, 0), (0, 0, 1), (1, 0, 0)]
    explanation = "il secondo e' l'output corretto"
    lista=[y.esiti() for y in listac]
    check(lista, expected, args, explanation,'')
    return 1
    
def test_program2_3():
    '''\nsi applica il metodo vittorie_livelli() all'albero di gioco che ha il nodo  radice 
    che rappresenta la configurazione  [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']].
    Si chiede di restituire la lista con le vittorie del giocatore 'o' ai livelli che vanno da 0 a 3.
    '''
    args        = ''
    expected    = [0, 1, 0, 1]
    explanation = "il secondo e' l'output corretto"
    lista=[listac[0].vittorie_livello('o',h) for h in range(4)]
    check(lista, expected, args, explanation,'')
    return 1
    
def test_program2_4():
    '''\nsi applica il metodo vittorie_livelli() all'albero di gioco che ha il nodo  radice 
    che rappresenta la configurazione  [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']].
    Si chiede di restituire la lista con le vittorie del giocatore 'x' ai livelli che vanno da 0 a 3.
    '''
    args        = ''
    expected    = [0, 0, 3, 0]
    explanation = "il secondo e' l'output corretto"
    lista=[listac[0].vittorie_livello('x',h) for h in range(4)]
    check(lista, expected, args, explanation,'')
    return 1

def test_program2_5():
    '''\nsi applica il metodo strategia_vincente() all'albero di gioco che ha il nodo  radice 
    che rappresenta la configurazione  [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']].
    Chiede di restituire la lista con  la risposta del metodo per il giocatore  'x' 
    e poi quella per il giocatore 'o'.
    '''
    args        = ''
    expected    = [False, True]
    explanation = "il secondo e' l'output corretto"
    lista=[listac[0].strategia_vincente('x'), listac[0].strategia_vincente('o')]
    check(lista, expected, args, explanation,'')
    return 1

def test_program2_6():
    '''\nsi applica il metodo esiti() al nodo radice dell'albero di gioco che 
    rappresenta la configurazione iniziale dove tutte le celle sono libere.  

    '''
    global rad
    rad=program02.gen_tree(g0)
    args        = ''
    expected    = (46080, 131184, 77904)
    explanation = "il secondo e' l'output corretto"
    t=rad.esiti()
    check(t, expected, args, explanation,'')
    return 1

def test_program2_7():
    '''\nsi applica il metodo vittorie_livello() al nodo radice dell'albero di gioco che 
    rappresenta la configurazione iniziale dove tutte le celle sono libere.\n  Bisogna restituire la 
    lista coi numeri di nodi che rappresentano vittorie  del giocatore 'o' e che si trovano nell'albero 
    ai livelli che vanno da 0 a 9.
    '''
    global rad
    args        = ''
    expected    = [0, 0, 0, 0, 0, 1440, 0, 47952, 0, 81792]
    explanation = "il secondo e' l'output corretto"
    lista=[rad.vittorie_livello('o',h) for h in range(10)]
    check(lista, expected, args, explanation,'')
    return 1

def test_program2_8():
    '''\nsi applica il metodo vittorie_livello() al nodo radice dell'albero di gioco che 
    rappresenta la configurazione iniziale dove tutte le celle sono libere.\n  Bisogna restituire la 
    lista coi numeri di nodi che rappresentano vittorie  del giocatore 'x' e che si trovano nell'albero 
    ai livelli che vanno da 0 a 9.
    '''
    global rad
    args        = ''
    expected    = [0, 0, 0, 0, 0, 0, 5328, 0, 72576, 0] 
    explanation = "il secondo e' l'output corretto"
    lista=[rad.vittorie_livello('x',h) for h in range(10)]
    check(lista, expected, args, explanation,'')
    rad = None
    return 1
 
def test_program2_9():
    '''\nsi applica il metodo esiti() ai 4 nodi radice degli alberi  di gioco che 
    rappresentano  le seguenti 4 configurazioni iniziali: \n
    [['', 'x', ''], ['', 'o', ''], ['', '', '']]\n
    [['', 'o', ''], ['', 'x', ''], ['', '', '']]\n
    [['', 'x', 'o'], ['', '', ''], ['', '', '']]\n
    [['', 'o', 'x'], ['', '', ''], ['', '', '']]\n
    Bisogna restituire la lista con le 4 risposte per il giocatore 'o'.
    '''
    global lista1
    args        = ''
    expected    = [(576, 2082, 612), (720, 1438, 1652), (864, 2048, 756), (864, 1798, 1276)]
    explanation = "il secondo e' l'output corretto"
    lista1= [program02.gen_tree(x) for x in listab]
    lista2=[y.esiti() for y in lista1]
    check(lista2, expected, args, explanation,'')
    return 1   

def test_program2_10():
    '''\nsi applica il metodo strategia_vincente() ai 4 nodi radice degli alberi  di gioco che 
    rappresentano  le seguenti 4 configurazioni iniziali: \n
    [['', 'x', ''], ['', 'o', ''], ['', '', '']]\n
    [['', 'o', ''], ['', 'x', ''], ['', '', '']]\n
    [['', 'x', 'o'], ['', '', ''], ['', '', '']]\n
    [['', 'o', 'x'], ['', '', ''], ['', '', '']]\n
    Bisogna restituire la lista con le 4 risposte per il giocatore 'o'.
    '''
    args        = ''
    expected    = [True, False, True, False]
    explanation = "il secondo e' l'output corretto"
    lista2=[y.strategia_vincente('o') for y in lista1]
    check(lista2, expected, args, explanation,'')
    return 1

def test_recursion_1():
    '''Verifica della NON ricorsione di 'tipo' '''
    args = ''
    expected = ['?', 'o', 'x', '-']
    explanation = "il secondo e' l'output corretto"
    decorate_module(program02)
    try:
        lista = [y.tipo() for y in listac]
        return 3
    finally:
        undecorate_module(program02)


def test_recursion_2():
    '''Verifica della ricorsione di 'esiti' '''
    decorate_module(program02)
    try:
        lista = [y.esiti() for y in listac]
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'esiti'")
    finally:
        undecorate_module(program02)

def test_recursion_3():
    '''Verifica della ricorsione di 'gen_tree' '''
    decorate_module(program02)
    try:
        program02.gen_tree(g0)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'gen_tree'")
    finally:
        undecorate_module(program02)


def test_recursion_4():
    '''Verifica della ricorsione di 'vittorie_livello' '''
    decorate_module(program02)
    try:
        lista = [listac[0].vittorie_livello('o', h) for h in range(4)]
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'vittorie_livello'")
    finally:
        undecorate_module(program02)

def test_recursion_5():
    '''Verifica della ricorsione di 'strategia_vincente' '''
    decorate_module(program02)
    try:
        lista = [listac[0].strategia_vincente('x'), listac[0].strategia_vincente('o')]
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'strategia_vincente'")
    finally:
        undecorate_module(program02)

tests = [
        test_recursion_1,
        test_recursion_2,
        test_recursion_3,
        test_recursion_4,
        test_recursion_5,
        test_program2_1,
        test_program2_2,
        test_program2_3,
        test_program2_4,
        test_program2_5,
        test_program2_6,
        test_program2_7,
        test_program2_8,
        test_program2_9,
        test_program2_10,
]


if __name__ == '__main__':
    #runtests(tests)
    runtests(tests,logfile='grade02.csv')

