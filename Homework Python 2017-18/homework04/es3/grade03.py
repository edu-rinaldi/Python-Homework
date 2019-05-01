#! /usr/bin/env python3 -B

from isrecursive import *
from testlib import check, runtests, check_text_file
import program03

def test_program3_1():
    '''Conto dei nodi con dato ID non esistente'''
    fileIn    = 'page1-3.html'
    selettore = '#id1'
    expected  = 0
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_2():
    '''Conto dei nodi con dato ID'''
    fileIn    = 'page1-3.html'
    selettore = '#intestazione'
    expected  = 1
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_3():
    '''Conto dei nodi con dato tag'''
    fileIn    = 'page1-3.html'
    selettore = 'p'
    expected  = 2
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_4():
    '''Conto dei nodi con data class'''
    fileIn    = 'page1-3.html'
    selettore = '.title'
    expected  = 1
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_5():
    '''Conto dei nodi con dato attributo'''
    fileIn    = 'page1-3.html'
    selettore = '@[width="300"]'
    expected  = 1
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_6():
    '''Conto dei nodi con relazione padre > figlio'''
    fileIn    = 'page1-3.html'
    selettore = 'p > em'
    expected  = 1
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_7():
    '''Conto dei nodi con relazione padre > figlio non esistente'''
    fileIn    = 'page1-3.html'
    selettore = 'p > a'
    expected  = 0
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

def test_program3_8():
    '''Conto dei nodi con relazione avo discendente'''
    fileIn    = 'page1-3.html'
    selettore = 'p a'
    expected  = 1
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1


def test_program3_9():
    '''Eliminazione dei nodi di tipo 'p a' '''
    fileIn    = 'page1-3.html'
    fileOut   = 'test9.html'
    fileExp   = 'risTest9-3.html'
    selettore = 'p a'
    ris       = program03.elimina_nodi(fileIn, selettore, fileOut)
    check_text_file(fileOut, fileExp)
    return 1

def test_program3_10():
    '''Selezione di un 'p a' e cambio colore in rosso'''
    fileIn    = 'page1-3.html'
    fileOut   = 'test10.html'
    fileExp   = 'risTest10-3.html'
    selettore = 'p a'
    chiave    = 'style'
    valore    = 'background-color:red'
    ris         = program03.cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    check_text_file(fileOut, fileExp)
    return 1

def test_program3_11():
    '''Selezione di un 'p a' e cambio colore in rosso'''
    fileIn    = 'python.org.html'
    fileOut   = 'test11.html'
    fileExp   = 'risTest11-3.html'
    selettore = 'p a'
    chiave    = 'style'
    valore    = 'background-color:red'
    ris         = program03.cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    check_text_file(fileOut, fileExp)
    return 1

def test_program3_12():
    '''Eliminazione di tutti gli '@[class="container"] > .main-wrap #firehose > .row strong' '''
    fileIn    = 'slashdot.html'
    fileOut   = 'test12.html'
    fileExp   = 'risTest12-3.html'
    selettore = '@[class="container"] > .main-wrap #firehose > .row strong'
    program03.elimina_nodi(fileIn, selettore, fileOut)
    check_text_file(fileOut, fileExp)
    return 1

def test_program3_13():
    '''Sfondo rosso a tutti gli '#slashdot_deals-title' '''
    fileIn    = 'slashdot.html'
    fileOut   = 'test13.html'
    fileExp   = 'risTest13-3.html'
    selettore = '#slashdot_deals-title'
    chiave    = 'style'
    valore    = 'background-color:red'
    ris       = program03.cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    check_text_file(fileOut, fileExp)
    return 1

def test_program3_14():
    '''Conteggio degli '@[id="slashboxes"] > article h2 > a' '''
    fileIn    = 'slashdot.html'
    selettore = '@[id="slashboxes"] > article h2 > a'
    expected  = 3
    args      = (fileIn, selettore)
    ris       = program03.conta_nodi(*args)
    check(ris, expected, args)
    return 1

# cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
# elimina_nodi(fileIn, selettore, fileOut)


def test_recursion_1():
    '''Ricorsione nella funzione conta_nodi (usando il test Conto dei nodi con dato ID non esistente)'''
    fileIn    = 'page1-3.html'
    selettore = '#id1'
    expected  = 0
    args      = (fileIn, selettore)
    decorate_module(program03)
    try:
        ris       = program03.conta_nodi(*args)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("Recursion not present")
    finally:
        undecorate_module(program03)

def test_recursion_2():
    '''Ricorsione nella funzione elimina_nodi (usando il test Eliminazione dei nodi di tipo 'p a') '''
    fileIn    = 'page1-3.html'
    fileOut   = 'test9.html'
    fileExp   = 'risTest9-3.html'
    selettore = 'p a'
    decorate_module(program03)
    try:
        ris = program03.elimina_nodi(fileIn, selettore, fileOut)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("Recursion not present")
    finally:
        undecorate_module(program03)

def test_recursion_3():
    '''Ricorsione nella funzione cambia_attributo (usando il test Selezione di un 'p a' e cambio colore in rosso)'''
    fileIn    = 'python.org.html'
    fileOut   = 'test11.html'
    fileExp   = 'risTest11-3.html'
    selettore = 'p a'
    chiave    = 'style'
    valore    = 'background-color:red'
    decorate_module(program03)
    try:
        ris = program03.cambia_attributo(fileIn, selettore, chiave, valore, fileOut)
    except RecursionDetectedError:
        return 3
    else:
        raise Exception("Recursion not present")
    finally:
        undecorate_module(program03)

tests = [
        test_recursion_1,
        test_recursion_2,
        test_recursion_3,
        test_program3_1,
        test_program3_2,
        test_program3_3,
        test_program3_4,
        test_program3_5,
        test_program3_6,
        test_program3_7,
        test_program3_8,
        test_program3_9,
        test_program3_10,
        test_program3_11,

        test_program3_12,
        test_program3_13,
        test_program3_14,
]


if __name__ == '__main__':
    #runtests(tests)
    runtests(tests,logfile='grade03.csv')

