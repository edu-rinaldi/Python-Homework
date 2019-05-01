#! /usr/bin/env python3 -B

from testlib import check, runtests
import program01


def test_program01_1():
    "lista di valori piccoli"
    lista=[70,330,293,154,128,113,178]
    ret= program01.modi(lista,6)
    check(ret, [293, 113])
    check(lista, [70,154,128])

    
def test_program01_2():
    "lista di valori medi"
    lista=[858659,8640829,777923,178433279,148035889,3125]
    ret= program01.modi(lista,4)
    check(ret, [])
    check(lista, [3125])

def test_program01_3():
    "lista di valori con divisori grandi"
    lista=[340887623,26237927,2491,777923,5311430407,6437635961,82284023]
    ret= program01.modi(lista,4)
    check(ret, [26237927])
    check(lista, [])
        
tests = [test_program01_1, test_program01_2, test_program01_3]


if __name__ == '__main__':
    runtests(tests)

