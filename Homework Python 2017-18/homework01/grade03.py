#! /usr/bin/env python3 -B

from testlib import check, runtests
import program03


def test_codifica_1():
    "chiave che contiene tutte le 26 lettere dell'alfabeto"
    ret = program03.codifica('the quick brown fox jumps over the lazy dog', 'papaveri e papere')
    check(ret,'rqrqzbhx b rqrbhb')
    
def test_decodifica_1():
    "chiave che contiene tutte le 26 lettere dell'alfabeto"
    ret = program03.decodifica('the quick brown fox jumps over the lazy dog', 'rqrqzbhx b rqrbhb')
    check(ret,'papaveri e papere')


def test_codifica_2():
    "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
    ret = program03.codifica('abracadabra', 'abracadabra')
    check(ret,'cdacbcrcdac')

def test_decodifica_2():
    "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
    ret = program03.decodifica('abracadabra', 'cdacbcrcdac')
    check(ret,'abracadabra')


def test_codifica_3():
    "il testo da codificare contiene caratteri che non appartengono alla chiave, la lettera 'e' non viene modificata (mappa su se stessa)"
    ret = program03.codifica('chiave crittografica', 'Ciao! ben tornato. Rivederti E’ un piacere')
    check(ret,'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie')

def test_decodifica_3():
    "il testo da codificare contiene caratteri che non appartengono alla chiave"
    ret = program03.decodifica('chiave crittografica', 'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie')
    check(ret,'Ciao! ben tornato. Rivederti E’ un piacere')


def test_codifica_4():
    "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
    ret = program03.codifica('zyxwvutsrqponmlkjihgfedcba', 'la nebbia agli irti colli')
    check(ret,'oz mvyyrz ztor rigr xloor')

def test_decodifica_4():
    "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
    ret = program03.decodifica('zyxwvutsrqponmlkjihgfedcba', 'oz mvyyrz ztor rigr xloor')
    check(ret,'la nebbia agli irti colli')

    
tests = [test_codifica_1, test_decodifica_1, test_codifica_2, test_decodifica_2, test_codifica_3, test_decodifica_3, test_codifica_4, test_decodifica_4]


if __name__ == '__main__':
    runtests(tests)

