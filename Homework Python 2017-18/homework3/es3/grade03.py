#! /usr/bin/env python3 -B

from testlib import check, runtests,check_img_file

import program03
import cProfile
rosso = (255,   0,   0)
blu   = (  0,   0, 255)
verde = (  0, 255,   0)
nero  = (  0,   0,   0)
bianco= (255, 255, 255)
giallo= (255, 255,   0)
cyan  = (  0, 255, 255)
magenta= (255,  0, 255)


def test_program_1():
    '''\nNell'immagine  'I1.png' un pixel (verde) e i suoi connessi vengono ricolorati di rosso. 
    Il bordo dell'area viene colorato di blu.
    '''
    args        = ('I1.png',[(10,10,rosso,blu)],'test1.png')
    expected    = [(2304, 196)]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test1.png','risTest1.png')
    return 1.0
    
def test_program_2():
    '''\nNell'immagine'I1.png' si ricolorano i pixel connessi a due diversi pixel, 
il  primo (verde), coi suoi connessi,  verra' ricolorato di  rosso, il  secondo 
pixel (bianco), coi suoi connessi, verra' ricolorato di nero. 
Il bordo delle aree verra' ricolorato rispettivamente di blu e di verde.
'''
    args        = ('I1.png',[(10,10,rosso,blu),(90,10,nero,verde)],'test2.png')
    expected    = [(2304, 196), (2304, 196)]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test2.png','risTest2.png')
    return 1.0
    
def test_program_3():
    '''\nNell'immagine'I1.png' si ricolorano i pixel connessi a  due diversi pixel, 
il primo pixel (verde), coi suoi connessi, verra'  ricolorato di  bianco, il  secondo  
pixel (bianco) coi suoi connessi verra' ricolorato  di  verde. 
I bordi delle aree ricolorate verranno ricolorati rispettivamente di blu e di rosso.
'''
    args        = ('I1.png',[(10,10,bianco,blu),(90,10,verde,rosso)],'test3.png')
    expected    = [(2304, 196), (2304, 196)]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test3.png','risTest3.png')
    return 1.0

def test_program_4():
    '''\nNell'immagine'I2.png' si ricolorano  50 diversi pixel rossi e i loro connessi, 
tutti questi pixel  verranno  ricolorati di bianco. I bordi delle 50 aree verranno ricolorati di verde.
'''
    lista=[(i*30+1,j*30+1,bianco,verde) for i in range(10) for j in range (10)if not (i+j)%2]
    args       = ('I2.png',lista,'test4.png')
    expected    = [(784, 116)] * 50
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test4.png','risTest4.png')
    
    return 1.0

def test_program_5():
    '''\nNell'immagine'I2.png' si ricolorano  100 diversi pixel tra rossi e neri, e i loro connessi. 
Di questi,  i pixel rossi verranno ricolorati di nero e quelli neri verranno ricolorati di rosso. 
I bordi delle aree divenute nere saranno colorati di verde, quelli delle aree divenute rosse saranno colorati di bianco.
'''
    lista0=[(i*30+1,j*30+1,nero, verde) for i in range(10) for j in range (10)if not (i+j)%2]
    lista1=[(i*30+1,j*30+1,rosso,bianco) for i in range(10) for j in range (10)if  (i+j)%2]
    args        = ('I2.png',lista0+lista1,'test5.png')
    expected    = [(784, 116)] * 100
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test5.png','risTest5.png')
    return 1.0

def test_program_6():
    '''\nNell'immagine 'I1.png' si ricolora lo stesso pixel al centro del quadrato e i suoi connessi più volte, 
    dando colori digradanti ai bordi. 
    '''
    lista=[(25,25,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    args        = ('I1.png',lista,'test6.png')
    expected    = [ ((50-i*2)**2,(50-i*2+1)*4) for i in range(1,25) ]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test6.png','risTest6.png')
    return 1.0

def test_program_7():
    '''\nNell'immagine 'I1.png' si ricolora lo stesso pixel che sta sul bordo e i suoi connessi più volte, dando colori digradanti ai bordi. 
    '''
    lista=[(0,0,(0,0,0),(0,5*i,5*i)) for i in range(1,25)]
    args        = ('I1.png',lista,'test7.png')
    expected    = [(2304, 196)] + [(0, 196)] * 23 
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test7.png','risTest7.png')
    return 1.0
    
def test_program_8():
    '''\nNell'immagine 'I3.png' si ricolora lo stesso pixel che sta al centro dell'immagine  e i suoi connessi più volte, 
    dando colori digradanti ai bordi. 
    '''
    lista=[(5*i+2,5*i+2,(0,255-6*i,0),(0,0,255-6*i)) for i in range(40)]
    args        = ('I3.png',lista,'test8.png')
    expected    = [(4744-120*i,3156-80*i) for i in range(40)]
    #[(4744, 3156), (4624, 3076), (4504, 2996), (4384, 2916), (4264, 2836), (4144, 2756), (4024, 2676), (3904, 2596), (3784, 2516), (3664, 2436), (3544, 2356), (3424, 2276), (3304, 2196), (3184, 2116), (3064, 2036), (2944, 1956), (2824, 1876), (2704, 1796), (2584, 1716), (2464, 1636), (2344, 1556), (2224, 1476), (2104, 1396), (1984, 1316), (1864, 1236), (1744, 1156), (1624, 1076), (1504, 996), (1384, 916), (1264, 836), (1144, 756), (1024, 676), (904, 596), (784, 516), (664, 436), (544, 356), (424, 276), (304, 196), (184, 116), (64, 36)]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test8.png','risTest8.png')
    return 1.0

def test_program_9():
    '''\nNell'immagine 'I4.png' si ricolora lo stesso pixel che sta al centro dell'immagine  e i suoi connessi più volte, 
    dando colori digradanti ai bordi. 
    '''
    lista=[(100,100,(255-x,255,255),(0,0,255-x)) for x in range(100)]
    args        = ('I4.png',lista,'test9.png')
    expected    = [(30195, 560), (29643, 552), (29095, 548), (28551, 544), (28011, 540), (27475, 536), (26943, 532), 
                   (26415, 528), (25891, 524), (25371, 520), (24855, 516), (24343, 512), (23835, 508), (23331, 504), 
                   (22831, 500), (22335, 496), (21847, 488), (21363, 484), (20883, 480), (20407, 476), (19935, 472), 
                   (19467, 468), (19003, 464), (18547, 456), (18095, 452), (17647, 448), (17203, 444), (16763, 440), 
                   (16331, 432), (15903, 428), (15479, 424), (15059, 420), (14643, 416), (14235, 408), (13831, 404), 
                   (13431, 400), (13035, 396), (12643, 392), (12259, 384), (11879, 380), (11503, 376), (11135, 368), 
                   (10771, 364), (10411, 360), (10059, 352), (9711, 348), (9367, 344), (9031, 336), (8699, 332), 
                   (8371, 328), (8051, 320), (7739, 312), (7431, 308), (7127, 304), (6831, 296), (6539, 292), (6251, 288), 
                   (5971, 280), (5699, 272), (5431, 268), (5167, 264), (4911, 256), (4659, 252), (4411, 248), (4171, 240), 
                   (3939, 232), (3715, 224), (3495, 220), (3279, 216), (3071, 208), (2871, 200), (2675, 196), (2483, 192), 
                   (2299, 184), (2123, 176), (1955, 168), (1795, 160), (1639, 156), (1487, 152), (1343, 144), (1207, 136), 
                   (1079, 128), (959, 120), (843, 116), (731, 112), (627, 104), (531, 96), (443, 88), (363, 80), (291, 72), 
                   (227, 64), (171, 56), (123, 48), (83, 40), (51, 32), (27, 24), (11, 16), (3, 8), (0, 3), (0, 3)] 
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test9.png','risTest9.png')
    return 1.0

def test_program_10():
    '''\nNell'immagine 'I7.png' si ricolora lo stesso pixel (1,1)   e i suoi connessi più volte, 
    dando al bordo lo stesso colore dell'area interna. 
    '''
    lista=[(1,1,(255,255,255),(255,255,255)),(1,1,(255,0,0),(255,0,0))]*40
    args        = ('I5.png',lista,'test10.png')
    expected    = [(882+980*i-98*j,218+20*i-2*j) for i in range(0,39)for j in range(1,-1,-1)]+[(39004,996)]*2
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test10.png','risTest10.png')
    return 1.0

def test_program_11():
    '''\nNell'immagine 'I6.png' si ricolorano in modo alternato piu' volte i pixel adiacenti (200,200) e (201,201) 
    assegnando all'area e ai bordi colori digradanti

    '''
    lista=[(200+j,200+j,(255-i,255*j,0),(255*j,255-i,0))for i in range(10) for j in range(2)]
    args        = ('I6.png',lista,'test11.png')
    expected    = [(0, 79198), (5, 80797)]*2+[(0, 79198), (0, 80797)]*8
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test11.png','risTest11.png')
    return 1.0
    
def test_program_12():
    '''\nNell'immagine 'I7.png' si ricolora lo stesso pixel  (205,205) 
    assegnando all'area e ai bordi sempre gli stessi due colori
    '''
    lista=[(204,204,(0,250,0),(240,0,250))for i in range(10) ]
    args        = ('I7.png',lista,'test12.png')
    expected    = [(112908, 31902), (81086, 31822), (49344, 31742), (17682, 31662), 
    (609, 17073), (0, 6), (111483, 32724), (78531, 32952), (40945, 29087), (25, 38)]
    explanation = "il secondo e' l'output corretto"
    ret=program03.ricolora(*args)
    check(ret, expected, args, explanation )
    check_img_file('test12.png','risTest12.png')
    return 1.0


tests = [
        test_program_1, 
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
        test_program_12
        ]


if __name__ == '__main__':
    runtests(tests)

