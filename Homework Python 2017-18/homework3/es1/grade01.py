#! /usr/bin/env python3 -B

from testlib import check, runtests

import program01
def test_program_0():
    "\nSi cerca il piu' grande quadrato bianco nell'immagine 'Inst0.png'. C'e' un solo pixel di colore bianco\n"
    args        = ('Ist0.png',(255,255,255))
    expected    = (1, (188, 118))
    explanation = "il secondo e' l'output corretto"
    returned    = program01.quadrato(*args)
    check(returned, expected, args, explanation )
    return 1.0
    
def test_program_1():
    "\nSi cerca il piu' grande quadrato rosso nell'immagine 'Inst1.png'. I rettangoli del colore cercato inseriti nell'immagine sono quadrati disgiunti\n"
    args        = ('Ist1.png',(255,0,0))
    expected    = (20, (30, 20))
    explanation = "il secondo e' l'output corretto"
    returned    = program01.quadrato(*args)
    check(returned, expected, args, explanation )
    return 1.0
    
def test_program_2():
    "\nSi cerca il piu' grande quadrato rosso nell'immagine 'Inst2.png'. I rettangoli  del colore cercato inseriti nell'immagine sono  disgiunti\n"
    args        = ('Ist2.png',(255,0,0))
    expected    = (30, (60, 50))
    explanation = "il secondo e' l'output corretto"
    returned    = program01.quadrato(*args)
    check(returned, expected, args, explanation )
    return 1.0
    
def test_program_3():
    "\nSi cerca il piu' grande quadrato rosso in 'Inst3.png'. I rettangoli del colore cercato inseriti nell'immagine si sovrappongono\n"
    args        = ('Ist3.png',(255,0,0))
    expected    = (60, (100, 50))
    explanation = "il secondo e' l'output corretto"
    returned    = program01.quadrato(*args)
    check(returned, expected, args, explanation )
    return 1.0

def test_program_4():
    "\nSi cerca il piu' grande quadrato blu in 'Inst4.png'. Lo sfondo dell'immagine ha il colore cercato ed abbonda\n"
    args       = ('Ist4.png',(0,0,255))
    expected   = (201,(54,240))
    explanation = "il secondo e' l'output corretto"
    returned    = program01.quadrato(*args)
    check(returned, expected, args, explanation )
    return 1.0


tests = [
        test_program_0, 
        test_program_1, 
        test_program_2,
        test_program_3, 
        test_program_4,
        ]


if __name__ == '__main__':
    runtests(tests)

