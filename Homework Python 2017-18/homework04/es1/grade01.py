#! /usr/bin/env python3 -B

from testlib import check, runtests
from isrecursive import *
from json import load

import program01

def test_program1_1():
    "\nsi applica la funzione genera_sottoalbero() su albero di 10 nodi\n"
    args        = ('Alb10.json','d','tAlb10_1.json')
    explanation = ''
    program01.genera_sottoalbero(*args)
    with open('tAlb10_1.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb10_1.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb10_1.json','risAlb10_1.json',) )
    return 1
    

def test_program1_2():
    "\nsi applica la funzione cancella_sottoalbero() su albero di 10 nodi\n"
    args        = ('Alb10.json','d','tAlb10_2.json')
    explanation = ''
    program01.cancella_sottoalbero(*args)
    with open('tAlb10_2.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb10_2.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args, explanation,('tAlb10_2.json','risAlb10_2.json') )
    return 1
    
def test_program1_3():
    "\nsi applica la funzione dizionario_livelli() su albero di 10 nodi\n"
    args        = ('Alb10.json','tAlb10_3.json')
    explanation = ''
    program01.dizionario_livelli(*args)
    with open('tAlb10_3.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb10_3.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args, explanation,('tAlb10_3.json','risAlb10_3.json') )
    return 1
    
def test_program1_4():
    "\nsi applica la funzione dizionario_gradi__antenati() su albero di 10 nodi\n"
    args        = ('Alb10.json',2,'tAlb10_4.json')
    explanation = ''
    program01.dizionario_gradi_antenati(*args)
    with open('tAlb10_4.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb10_4.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args,explanation, ('tAlb10_4.json','risAlb10_4.json')  )
    return 1


    
def test_program1_5():
    "\nsi applica la funzione genera_sottoalbero() su albero di 100 nodi\n"
    args        = ('Alb100.json','ultras','tAlb100_1.json')
    explanation = ''
    program01.genera_sottoalbero(*args)
    with open('tAlb100_1.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb100_1.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb100_1.json','risAlb100_1.json') )
    return 1
    
def test_program1_6():
    "\nsi applica la funzione cancella_sottoalbero() su albero di 100 nodi\n"
    args        = ('Alb100.json','ultras','tAlb100_2.json')
    explanation = ''
    program01.cancella_sottoalbero(*args)
    with open('tAlb100_2.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb100_2.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb100_2.json','risAlb100_2.json') )
    return 1

def test_program1_7():
    "\nsi applica la funzione dizionario_livelli() su albero di 100 nodi\n"
    args        = ('Alb100.json','tAlb100_3.json')
    explanation = ''
    program01.dizionario_livelli(*args)
    with open('tAlb100_3.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb100_3.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args, explanation,('tAlb100_3.json','risAlb100_3.json'))
    return 1
    
def test_program1_8():
    "\nsi applica la funzione dizionario_gradi__antenati() su albero di 100 nodi\n"
    args        = ('Alb100.json',2,'tAlb100_4.json')
    explanation = ''
    program01.dizionario_gradi_antenati(*args)
    with open('tAlb100_4.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb100_4.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args, explanation,('tAlb100_4.json','risAlb100_4.json') )
    return 1

def test_program1_9():
    "\nsi applica la funzione genera_sottoalbero() su albero di 20000 nodi\n"
    args       = ('Alb20000.json','felici','tAlb20000_1.json')
    explanation = ''
    program01.genera_sottoalbero(*args)
    with open('tAlb20000_1.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb20000_1.json', encoding='utf8')as f: d2=load(f)
    check(d1,d2, args,explanation,('tAlb20000_1.json','risAlb20000_1.json')  )
    return 1
    
def test_program1_10():
    "\nsi applica la funzione cancella_sottoalbero() su albero di 20000 nodi\n"
    args       = ('Alb20000.json','felici','tAlb20000_2.json')
    explanation = ''
    program01.cancella_sottoalbero(*args)
    with open('tAlb20000_2.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb20000_2.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb20000_2.json','risAlb20000_2.json') )
    return 1

def test_program1_11():
    "\nsi applica la funzione dizionario_livelli() su albero di 20000 nodi\n"
    args       = ('Alb20000.json','tAlb20000_3.json')
    explanation = ''
    program01.dizionario_livelli(*args)
    with open('tAlb20000_3.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb20000_3.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb20000_3.json','risAlb20000_3.json'))
    return 1
    
def test_program1_12():
    "\nsi applica la funzione dizionario_gradi__antenati() su albero di 20000 nodi\n"
    args       = ('Alb20000.json',2,'tAlb20000_4.json')
    explanation = ''
    program01.dizionario_gradi_antenati(*args)
    with open('tAlb20000_4.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb20000_4.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb20000_4.json','risAlb20000_4.json') )
    return 1

def test_recursion_1():
    '''Verifica della ricorsione di 'genera_sottoalbero' '''
    args        = ('Alb10.json','d','tAlb10_1.json')
    explanation = ''
    decorate_module(program01)
    try:
        program01.genera_sottoalbero(*args)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'genera_sottoalbero'")
    finally:
        undecorate_module(program01)

def test_recursion_2():
    '''Verifica della ricorsione di 'cancella_sottoalbero' '''
    args = ('Alb10.json', 'd', 'tAlb10_2.json')
    decorate_module(program01)
    try:
        program01.cancella_sottoalbero(*args)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'cancella_sottoalbero'")
    finally:
        undecorate_module(program01)

def test_recursion_3():
    '''Verifica della ricorsione di 'dizionario_livelli' '''
    args = ('Alb10.json', 'tAlb10_3.json')
    decorate_module(program01)
    try:
        program01.dizionario_livelli(*args)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'dizionario_livelli'")
    finally:
        undecorate_module(program01)

def test_recursion_4():
    '''Verifica della ricorsione di 'dizionario_gradi_antenati' '''
    args        = ('Alb10.json',2,'tAlb10_4.json')
    decorate_module(program01)
    try:
        program01.dizionario_gradi_antenati(*args)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("No recursion detected in 'dizionario_gradi_antenati'")
    finally:
        undecorate_module(program01)


def test_program1_13():
    "\nsi applica la funzione genera_sottoalbero() su albero di 50000 nodi\n"
    args       = ('Alb50000.json','anglofobo','tAlb50000_1.json')
    explanation = ''
    program01.genera_sottoalbero(*args)
    with open('tAlb50000_1.json', encoding='utf8') as f: d1=load(f)
    with open('risAlb50000_1.json', encoding='utf8') as f: d2=load(f)
    check(d1,d2, args,explanation,('tAlb50000_1.json','risAlb50000_1.json')  )
    return 1

def test_program1_14():
    "\nsi applica la funzione cancella_sottoalbero() su albero di 50000 nodi\n"
    args       = ('Alb50000.json','zarzuela','tAlb50000_2.json')
    explanation = ''
    program01.cancella_sottoalbero(*args)
    with open('tAlb50000_2.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb50000_2.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb50000_2.json','risAlb50000_2.json') )
    return 1


def test_program1_15():
    "\nsi applica la funzione dizionario_livelli() su albero di 50000 nodi\n"
    args       = ('Alb50000.json','tAlb50000_3.json')
    explanation = ''
    program01.dizionario_livelli(*args)
    with open('tAlb50000_3.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb50000_3.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb50000_3.json','risAlb50000_3.json'))
    return 1

def test_program1_16():
    "\nsi applica la funzione dizionario_gradi__antenati() su albero di 50000 nodi\n"
    args       = ('Alb50000.json',2,'tAlb50000_4.json')
    explanation = ''
    program01.dizionario_gradi_antenati(*args)
    with open('tAlb50000_4.json', encoding='utf8')as f: d1=load(f)
    with open('risAlb50000_4.json', encoding='utf8')as f: d2=load(f)
    check(d1, d2, args, explanation,('tAlb50000_4.json','risAlb50000_4.json') )
    return 1





tests = [
        test_recursion_1,
        test_recursion_2,
        test_recursion_3,
        test_recursion_4,

        test_program1_1, test_program1_2,test_program1_3,test_program1_4,
        test_program1_5,test_program1_6, test_program1_7,test_program1_8,
        test_program1_9, test_program1_10,test_program1_11,test_program1_12,
        test_program1_13, test_program1_14,test_program1_15,test_program1_16,
]


if __name__ == '__main__':
    #runtests(tests)
    runtests(tests,logfile='grade01.csv')

