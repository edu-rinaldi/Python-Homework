#! /usr/bin/env python3 -B

from testlib import check, runtests 
print('\n'*3)

import program02
from json import load
def test_program_1():
    "\n il file contiene informazioni su soli 10 compiti\n"
    args=('file02_10_2.txt', {'2','4','11','1','6','9','10'},'test1.json')
    ret =  program02.pianifica(*args)
    with open('test1.json')as f: d1=load(f)
    with open('risTest1.json')as f: d2=load(f)
    check(d1,d2, args, 'risultato corretto',('test1.json','risTest1.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0


def test_program_2():
    "\n il file contiene informazioni su 10000 compiti e l'insieme ne contiene    10\n\n"
    args= ('file02_10000_50.txt',{'10','20','30','40','50','60','70','80'},'test2.json')
    ret = program02.pianifica(*args)
    with open('test2.json')as f: d1=load(f)
    with open('risTest2.json')as f: d2=load(f)
    check(d1,d2,args, 'risultato corretto',('test2.json','risTest2.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0


def test_program_3():
    "\n il file contiene informazioni su 50000 compiti e l'insieme ne contiene    10\n\n"
    args= ('file02_50000_100.txt', {'1','2','3','4','5','6','7','8','9'},'test3.json')
    ret = program02.pianifica(*args)
    with open('test3.json')as f: d1=load(f)
    with open('risTest3.json')as f: d2=load(f)
    check(d1,d2,args, 'risultato corretto',('test3.json','risTest3.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0

def test_program_4():
    "\n il file contiene informazioni su 50000 compiti e l'insieme ne contiene  1000\n\n"
    args=('file02_50000_100.txt', 'set([str(i) for i in range(1000,2001)])','test4.json')
    ret = program02.pianifica('file02_50000_100.txt', set([str(i) for i in range(1000,2001)]),'test4.json')
    with open('test4.json')as f: d1=load(f)
    with open('risTest4.json')as f: d2=load(f)
    check(d1,d2, args,'risultato corretto',('test4.json','risTest4.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0

def test_program_5():
    "\n il file contiene informazioni su 50000 compiti e l'insieme ne contiene 50000\n\n"
    args= ('file02_50000_100.txt', 'set([str(i) for i in range(2000,52001)])','test5.json')
    ret = program02.pianifica('file02_50000_100.txt', set([str(i) for i in range(2000,52001)]),'test5.json')
    with open('test5.json')as f: d1=load(f)
    with open('risTest5.json')as f: d2=load(f)
    check(d1,d2, args, 'risultato corretto',('test5.json','risTest5.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0

def test_program_6():
    "\n il file contiene informazioni su 200000 compiti e l'insieme ne contiene 80\n\n"
    z=80
    args= ('file02_200000.txt', '{1,3,..79} | {199998-80,199998-78,...199998}','test6.json')
    ret = program02.pianifica('file02_200000.txt', set([str(x) for x in range(1,z,2)]) | set([str(x) for x in range(199998,199998-z-1,-2)]),'test6.json')
    with open('test6.json')as f: d1=load(f)
    with open('risTest6.json')as f: d2=load(f)
    check(d1,d2, args, 'risultato corretto',('test6.json','risTest6.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0

def test_program_7():
    "\n il file contiene informazioni su 200000 compiti e l'insieme ne contiene 100\n\n"
    z=100
    args= ('file02_200000.txt', '{1,3,..99} | {199998-100,199998-98,...199998}','test7.json')
    ret = program02.pianifica('file02_200000.txt', set([str(x) for x in range(1,z,2)]) | set([str(x) for x in range(199998,199998-z-1,-2)]),'test7.json')
    with open('test7.json')as f: d1=load(f)
    with open('risTest7.json')as f: d2=load(f)
    check(d1,d2, args, 'risultato corretto',('test7.json','risTest7.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0

def test_program_8():
    "\n il file contiene informazioni su 200000 compiti e l'insieme ne contiene 140\n\n"
    z=140
    args= ('file02_200000.txt',  '{1,3,..139} | {199998-140,199998-138,...199998}','test8.json')
    ret = program02.pianifica('file02_200000.txt', set([str(x) for x in range(1,z,2)]) | set([str(x) for x in range(199998,199998-z-1,-2)]),'test8.json')
    with open('test8.json')as f: d1=load(f)
    with open('risTest8.json')as f: d2=load(f)
    check(d1,d2, args, 'risultato corretto',('test8.json','risTest8.json'))
    check(ret,None,args,'risultato corretto',('valore restituito', 'None'))
    return 1.0
tests = [test_program_1 ,test_program_2,test_program_3,test_program_4,test_program_5,test_program_6,test_program_7,test_program_8]


if __name__ == '__main__':
    runtests(tests)

