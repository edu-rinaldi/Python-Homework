#! /usr/bin/env python3 -B

from testlib import check, runtests
import program02

def test_program_1():
    "numero semplice senza elisioni"
    ret = program02.conv(3)
    check(ret,'tre', 3, 'return')
    return 1
    
def test_program_2():
    "numero speciale tra 10 e 20"
    ret = program02.conv(17)
    check(ret,'diciassette', 17, 'return')
    return 1


def test_program_3():
    "non-elisione del cento e elisione del venti-otto"
    ret = program02.conv(128)
    check(ret,'centoventotto', 128, 'return')
    return 1

def test_program_4():
    "non-elisione del cento"
    ret = program02.conv(508)
    check(ret,'cinquecentootto',508,'return')
    return 1
    
def test_program_5():
    "non-elisione del mille e del cento"
    ret = program02.conv(1501)
    check(ret,'millecinquecentouno',1501,'return')
    return 1

def test_program_6():
    "non-elisione del mille e elisione di 80"
    ret = program02.conv(17081)
    check(ret,'diciassettemilaottantuno', 17081, 'return')
    return 1

def test_program_7():
    "numero grande con molte elisioni e non-elisioni"
    orig = 981008818
    ret = program02.conv(orig)
    check(ret,'novecentottantunomilioniottomilaottocentodiciotto', orig, 'return')
    return 1
   
def test_program_8():
    "elisioni 800-80 e 80-8"
    orig = 888888888
    res  = 'ottocentottantottomilioniottocentottantottomilaottocentottantotto'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_9():
    'non elisioni 800-8 e elisioni 800-80'
    orig = 808080808080
    res  = 'ottocentoottomiliardiottantamilioniottocentoottomilaottanta'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_10():
    'non elisioni 800-1 e elisioni 80-1'
    orig = 801081801081
    res  = 'ottocentounomiliardiottantunomilioniottocentounomilaottantuno'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_11():
    'elisioni sessanta-otto, cinquanta-otto, quaranta-otto, trenta-otto'
    orig = 68258148238
    res  = 'sessantottomiliardiduecentocinquantottomilionicentoquarantottomiladuecentotrentotto'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_12():
    'elisioni ottanta-uno,settanta-uno,novanta-uno, venti-uno'
    orig = 81071091021
    res  = 'ottantunomiliardisettantunomilioninovantunomilaventuno'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_13():
    'numeri speciali tra 10 e 20'
    orig = 11012013014
    res  = 'undicimiliardidodicimilionitredicimilaquattordici'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

def test_program_14():
    'numero massimo da convertire'
    orig = 99999999999
    res  = 'novantanovemiliardinovecentonovantanovemilioninovecentonovantanovemilanovecentonovantanove'
    ret = program02.conv(orig)
    check(ret, res, orig, 'return')
    return 1

tests = [   test_program_1, 
            test_program_2,
            test_program_3, 
            test_program_4, 
            test_program_5, 
            test_program_6, 
            test_program_7,
            test_program_8,
            test_program_9,
            test_program_10,
            test_program_11,
            test_program_12,
            test_program_13,
            test_program_14,
            ]


if __name__ == '__main__':
    runtests(tests,logfile='grade02.csv')

