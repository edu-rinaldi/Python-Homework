#! /usr/bin/env python3 -B

from testlib import check, runtests
import program03

def test_codifica_1():
    "chiave che contiene tutte le 26 lettere dell'alfabeto"
    args=('the quick brown fox jumps over the lazy dog', 'papaveri e papere')
    ret = program03.codifica(*args)
    check(ret,'rqrqzbhx b rqrbhb', args, 'return')
    return 1
    
def test_decodifica_1():
    "chiave che contiene tutte le 26 lettere dell'alfabeto"
    args = ('the quick brown fox jumps over the lazy dog', 'rqrqzbhx b rqrbhb')
    ret = program03.decodifica(*args)
    check(ret,'papaveri e papere', args, 'return')
    return 1


def test_codifica_2():
    "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
    args = ('abracadabra', 'abracadabra')
    ret = program03.codifica(*args)
    check(ret,'cdacbcrcdac', args, 'return')
    return 1

def test_decodifica_2():
    "chiave che NON contiene tutte le 26 lettere dell'alfabeto, il testo contiene solo lettere della chiave, la chiave sposta tutte le lettere (nessuna mappa su se stessa)"
    args = ('abracadabra', 'cdacbcrcdac')
    ret = program03.decodifica(*args)
    check(ret,'abracadabra', args, 'return')
    return 1


def test_codifica_3():
    "il testo da codificare contiene caratteri che non appartengono alla chiave, la lettera 'e' non viene modificata (mappa su se stessa)"
    args = ('chiave crittografica', 'Ciao! ben tornato. Rivederti E’ un piacere')
    ret = program03.codifica(*args)
    check(ret,'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie', args, 'return')
    return 1

def test_decodifica_3():
    "il testo da codificare contiene caratteri che non appartengono alla chiave"
    args = ('chiave crittografica', 'Crhf! ben cfinhcf. Rraedeicr E’ un prhveie')
    ret = program03.decodifica(*args)
    check(ret,'Ciao! ben tornato. Rivederti E’ un piacere', args, 'return')
    return 1


def test_codifica_4():
    "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
    key  = 'zyxwvutsrqponmlkjihgfedcba'
    text = 'la nebbia agli irti colli'
    res  = 'oz mvyyrz ztor rigr xloor'
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_decodifica_4():
    "la chiave contiene l'alfabeto completo una sola volta, invertito, essendo un numero pari di lettere, nessuna mappa su se stessa"
    key  = 'zyxwvutsrqponmlkjihgfedcba'
    res  = 'la nebbia agli irti colli'
    text = 'oz mvyyrz ztor rigr xloor'
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_codifica_5():
    "la chiave contiene l'alfabeto completo una sola volta"
    key  = 'abcdefghijklmnopqrstuvxywz'
    text = 'papaveri e papere'
    res  = 'papaveri e papere'
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_decodifica_5():
    "la chiave contiene l'alfabeto completo una sola volta"
    key  = 'abcdefghijklmnopqrstuvxywz'
    text = 'papaveri e papere'
    res  = 'papaveri e papere'
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_codifica_6():
    "la chiave non contiene  lettere dell’alfabeto tra ‘a’ e ‘z’ "
    key  = "QUESTA E' UNA CODIFICA DEBOLE"
    text = 'papaveri e papere'
    res  = 'papaveri e papere'
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_decodifica_6():
    "la chiave non contiene  lettere dell’alfabeto tra ‘a’ e ‘z’ "
    key  = "QUESTA E' UNA CODIFICA DEBOLE"
    text = 'papaveri e papere'
    res  = 'papaveri e papere'
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_codifica_7():
    "la chiave e il testo da codificare sono simili"
    key  = "Monti Spognardi e Sterbini"
    text = 'Sterbini Spognardi e Monti'
    res  = 'Sianotet Sbrdepngt a Mreit'
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_decodifica_7():
    "la chiave e il testo da codificare sono simili"
    key  = "Monti Spognardi e Sterbini"
    text = 'Sterbini Spognardi e Monti'
    res  = 'Sinoptrt Sabdreogt n Mbrit'
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_codifica_8():
    "la chiave contiene solo vocali"
    key  = "Le aiuoLE"
    text = 'verranno codificate solo le vocali'
    res  = 'varrennu cudificeta sulu la vuceli'
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_decodifica_8():
    "la chiave contiene solo vocali"
    key  = "Le aiuoLE"
    text = 'varrennu cudificeta sulu la vuceli'
    res  = 'verranno codificate solo le vocali'
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1

def test_codifica_9():
    "chiave che contiene tutte le 26 lettere dell'alfabeto ripetuta 100 volte"
    key  = 'the quick brown fox jumps over the lazy dog'*100
    text = 'papaveri e papere'*100
    res  = 'rqrqzbhx b rqrbhb'*100
    args = (key, text)
    ret  = program03.codifica(*args)
    check(ret, res, args, 'return')
    return 1
    
def test_decodifica_9():
    "chiave che contiene tutte le 26 lettere dell'alfabeto ripetuta 100 volte"
    key  = 'the quick brown fox jumps over the lazy dog'*100
    text = 'rqrqzbhx b rqrbhb'*100
    res  = 'papaveri e papere'*100
    args = (key, text)
    ret  = program03.decodifica(*args)
    check(ret, res, args, 'return')
    return 1
    
tests = [
        test_codifica_1, 
        test_decodifica_1, 
        test_codifica_2, 
        test_decodifica_2, 
        test_codifica_3, 
        test_decodifica_3, 
        test_codifica_4, 
        test_decodifica_4,
        test_codifica_5, 
        test_decodifica_5,
        test_codifica_6, 
        test_decodifica_6,
        test_codifica_7, 
        test_decodifica_7,
        test_codifica_8, 
        test_decodifica_8,
        test_codifica_9, 
        test_decodifica_9,
        ]


if __name__ == '__main__':
    runtests(tests,logfile='grade03.csv')

