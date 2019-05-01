#! /usr/bin/env python3 -B

from testlib import check, runtests, check_img_file

import program02
def test_program_1():
    '''\nScacchiera in cui il cammino del robottino e' molto breve
    '''
    args        = ('I1.png','t1.png')
    explanation = "il cammino corretto e' nella seconda stringa"
    ret= program02.cammino(*args)
    check( ret, '000112223', args,explanation )
    check_img_file('t1.png','risT1.png')
    return 1.0
    
def test_program_2():
    '''\nScacchiera in cui il robottino ha un cammino di media lunghezza
'''
    args        = ('I2.png','t2.png')
    explanation = "il cammino corretto e' nella seconda stringa"
    ret=program02.cammino(*args)
    check( ret, '0001211111111111122333333333333', args,explanation )
    check_img_file('t2.png','risT2.png')
    return 1.0
    
def test_program_3():
    '''\nScacchiera in cui il robottino ha un cammino piuttosto lungo
'''
    args        = ('I3.png','t3.png')
    explanation = "il cammino corretto e' nella seconda stringa"
    ret=program02.cammino(*args)
    check( ret, '000121111111111110000000003000333333332222222222211111011123', args,explanation )
    check_img_file('t3.png','risT3.png')
    return 1.0

def test_program_4():
    '''\nScacchiera priva di ostacoli in cui il robottino tocca tutte le caselle
'''
    args       = ('I4.png','t4.png')
    explanation = "il cammino corretto e' nella seconda stringa"
    stringa='00000000000000111111111111112222222222222233333333333330000000000000111111111111222222222222333333333330000000000011111111112222222222333333333000000000111111112222222233333330000000111111222222333330000011112222333000112230'
    ret=program02.cammino(*args)
    check( ret, stringa, args,explanation )
    check_img_file('t3.png','risT3.png')
    return 1.0


def test_program_5():
    '''\nScacchiera in cui il robottino fa un bel giro contorto quasi dappertutto
'''
    args       = ('I5.png','t5.png')
    explanation = "il cammino corretto e' nella seconda stringa"
    stringa='0101010101010101010101122323232323232323221101010101122322110110300010030010000330333333333333222222222210101010101010100333333322222101010101'
    ret=program02.cammino(*args)
    check( ret, stringa, args,explanation )
    check_img_file('t5.png','risT5.png')
    return 1.0


tests = [
        test_program_1, test_program_2,test_program_3, test_program_4, test_program_5,
        ]


if __name__ == '__main__':
    runtests(tests)

