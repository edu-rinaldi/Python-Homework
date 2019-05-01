#! /usr/bin/env python3 -B

from testlib import check, runtests

import program03
def test_program_1():
    "si cercano in 'file03.txt' parole compatibili con la struttura '121'"
    args        = ('file03.txt','121')
    expected    = {'afa', 'ada', 'gag', 'sos', 'ere', 'ivi', 'aia', 'ala', 'iti', 'odo', 'ara', 'ava', 'imi', 'oro', 'ama', 'non', 'idi', 'oso'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0
    
def test_program_2():
    "si cercano in 'file03.txt' parole compatibili con la struttura '3533939339'"
    args        = ('file03.txt','3533939339')
    expected    = {'ninnananna'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0
    
def test_program_3():
    "si cercano in 'file03.txt' parole compatibili con la struttura '138831'"
    args        = ('file03.txt','138831')
    expected    = set()
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0

def test_program_4():
    "si cercano in 'file03.txt' parole compatibili con la struttura '609155'"
    args       = ('file03.txt','609155')
    expected   = {'aderii', 'soiree', 'kaputt', 'scalee', 'servii', 'dormii', 'fornii', 
        'spedii', 'lintee', 'barcee', 'prozii', 'cornee', 'chinee', 'ipogee', 'stonii', 
        'vitree', 'lambii', 'acquee', 'sparii', 'tropee', 'arguii', 'limnee', 'gradii', 
        'trabee', 'giudee', 'livree', 'nutrii', 'orwell', 'colpii', 'carnee', 'pendii', 
        'sorbii', 'cupree', 'guarii', 'mirtee', 'platee', 'svenii', 'morfee', 'pentii', 
        'partii', 'lignee', 'tradii', 'patrii', 'brucii', 'idonee', 'tornii', 'yankee', 
        'reagii', 'bypass', 'abolii', 'condii', 'nausee', 'ruglii', 'svolii', 'mentii', 
        'stupii', 'mazdee', 'pigmee', 'epizoo', 'gremii', 'raspii', 'scolii', 'glacee', 
        'lauree', 'refill', 'restii', 'sancii', 'seguii', 'lincee', 'glorii', 'spazii', 
        'gneiss', 'brusii', 'sentii', 'svanii', 'tarpee', 'ronzii', 'spurii', 'uvacee', 
        'contee', 'ghinee', 'ascree', 'bandii', 'dionee'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0

def test_program_5():
    "si cercano in 'all.txt' parole compatibili con la struttura '2091555'"
    args        = ('all.txt','2091555')
    expected    = {'nuwclll', 'crazeee', 'cerusss', 'enumiii', 'pdkinnn', 'wreniii', 'qdainnn', 
            'ncsappp', 'parswww', 'gtesccc', 'topazzz', 'hpljiii', 'linuxxx', 'portwww', 'goateee', 
            'bingccc', 'charxxx', 'ortciii', 'itemzzz', 'sfkinnn', 'ludewww', 'machiii', 'troniii', 
            'tojinnn', 'fghinnn', 'hostwww', 'qljinnn', 'blechhh', 'hpsinnn', 'makewww', 'comviii', 'ditommm'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0

def test_program_6():
    "si cercano in 'all.txt' parole compatibili con la struttura '99223475'"
    args        = ('all.txt','99223475')
    expected    = {'mmccarty', 'aassiden', 'eeggplnt', 'llooking', 'aakkostu'}
    explanation = "il secondo e' l'insieme corretto"
    returned    = program03.decod(*args)
    check(returned, expected, args, explanation )
    return 1.0
   
tests = [
        test_program_1, 
        test_program_2,
        test_program_3, 
        test_program_4,
        test_program_5,
        test_program_6,
        ]


if __name__ == '__main__':
    runtests(tests)

