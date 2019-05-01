#! /usr/bin/env python3 -B

from testlib import check, runtests
import program01

def test_program01_3():
    "lista di valori piccoli max 3 cifre"
    lista=[70,330,293,154,128,113,178]
    orig= [] + lista
    ret= program01.modi(lista,6)
    check(ret,   [293, 113],   orig, 'return')
    check(lista, [70,154,128], orig, 'ls')
    return 1

def test_program01_7():
    "lista di valori tutti di 7 cifre"
    lista=[1234579,1234604,1234613,1234641,1234684,1234687,1234793,1234836,1234837,1234847]
    orig= [] + lista
    ret= program01.modi(lista,6)
    check(ret,   [1234613,1234687,1234837],   orig, 'return')
    check(lista, [1234579,1234641,1234793,1234847 ], orig, 'ls')
    return 1
    
def test_program01_9():
    "lista di valori di max 9 cifre"
    lista=[858659,8640829,777923,178433279,148035889,3125]
    orig= [] + lista
    ret= program01.modi(lista,4)
    check(ret,   [],     orig, 'return')
    check(lista, [3125], orig, 'ls')
    return 1

def test_program01_9_2():
    "lista di valori tutti da 9 cifre"
    lista=[100000300, 100000431, 100000463, 100000647, 100000675, 100000687, 100001025, 100001111]
    orig= [] + lista
    ret= program01.modi(lista,10)
    check(ret,   [100000463,100000687],     orig, 'return')
    check(lista, [100000431, 100000675, 100001111], orig, 'ls')
    return 1

def test_program01_10():
    "lista di valori di max 10 cifre con divisori grandi"
    lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
    orig= [] + lista
    ret= program01.modi(lista,4)
    check(ret, [26237927], orig, 'return')
    check(lista, [],       orig, 'ls')
    return 1

def test_program01_5():
    "lista di valori tutti di 5 cifre"
    lista=[12347,12369,13125, 13127,13202,13750,13751,13838,14406,14407,14421,24010,24019,24035,26364]
    orig= [] + lista
    ret= program01.modi(lista,14)
    check(ret, [ 12347,  13127,  13751 , 14407, 24019], orig, 'return')
    check(lista, [ 12369,  13202,  13838,  14421, 24035 ],       orig, 'ls')
    return 1
        
def test_program01_11():
    "lista di valori tutti di 11 cifre"
    lista=[10000000116, 10000000431, 10000000469, 10000000548, 10000000697, 10000000711, 10000000768, 10000000924]
    orig= [] + lista
    ret= program01.modi(lista,16)
    check(ret, [10000000469,10000000711], orig, 'return')
    check(lista, [10000000116, 10000000548, 10000000768],       orig, 'ls')
    return 1
tests = [   test_program01_3, 
            test_program01_5, 
            test_program01_7, 
            test_program01_9, 
            test_program01_9_2, 
            test_program01_10, 
            test_program01_11,
            ]


if __name__ == '__main__':
    runtests(tests,logfile='grade01.csv')
    #runtests(tests)

