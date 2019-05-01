#! /usr/bin/env python3 -B

from testlib import check, runtests
import program02

def test_program_1():
    "numero semplice senza elisioni"
    ret = program02.conv(3)
    check(ret,'tre')
    
def test_program_2():
    "numero speciale tra 10 e 20"
    ret = program02.conv(17)
    check(ret,'diciassette')


def test_program_3():
    "non-elisione del cento e elisione del venti-otto"
    ret = program02.conv(128)
    check(ret,'centoventotto')

def test_program_4():
    "non-elisione del cento"
    ret = program02.conv(508)
    check(ret,'cinquecentootto')
    
def test_program_5():
    "non-elisione del mille e del cento"
    ret = program02.conv(1501)
    check(ret,'millecinquecentouno')

def test_program_6():
    "non-elisione del mille e elisione di 80"
    ret = program02.conv(17081)
    check(ret,'diciassettemilaottantuno')

def test_program_7():
    "numero grande con molte elisioni e non-elisioni"
    ret = program02.conv(981008818)
    check(ret,'novecentottantunomilioniottomilaottocentodiciotto')
    
tests = [test_program_1, test_program_2,test_program_3, test_program_4, test_program_5, test_program_6, test_program_7]


if __name__ == '__main__':
    runtests(tests)

