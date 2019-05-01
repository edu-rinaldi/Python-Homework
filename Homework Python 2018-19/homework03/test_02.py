import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

from program02 import Colore, Rettangolo, Skyline

@ddt
class Test(testlib.TestCase):

    # Colore.utilizzo(Skyline)
    # Skyline.larghezza()
    # Skyline.altezza()
    # Skyline.edifici()
    # Skyline.to_tuple()
    # Skyline.salva(filename)   filename -> stringa che finisce per .png
    def do_test(self, sk, nu, ru, vu, bu, wu, w, h, N, f1=None, f2=None):
        '''Implementazione del test
            - sk:   skyline creata
            - nu:   numero di palazzi neri
            - ru:   numero di palazzi rossi
            - vu:   numero di palazzi verdi
            - bu:   numero di palazzi blu
            - wu:   numero di palazzi bianchi
            - w:    larghezza dell'immagine
            - h:    altezza dell'immagine
            - N:    numero di palazzi
            - f1:   file in cui si deve salvare l'immagine
            - f2:   file in cui si trova l'immagine attesa
        '''
        self.check(Test.nero.utilizzo(sk),  nu, None, "il numero di palazzi neri non è giusto")
        self.check(Test.rosso.utilizzo(sk), ru, None, "il numero di palazzi rossi non è giusto")
        self.check(Test.verde.utilizzo(sk), vu, None, "il numero di palazzi verdi non è giusto")
        self.check(Test.blu.utilizzo(sk),   bu, None, "il numero di palazzi blu non è giusto")
        self.check(Test.bianco.utilizzo(sk),wu, None, "il numero di palazzi bianchi non è giusto")
        self.check(sk.larghezza(),          w,  None, "la larghezza non è giusta")
        self.check(sk.altezza(),            h,  None, "l'altezza non è giusta")
        self.check(sk.edifici(),            N,  None, "il numero di edifici non è giusto")
        if f1:
            sk.salva(f1)
            self.check_img_file(f1, f2)
        return 1

    def skyline_specs(self, sk):
        return  (
                Test.nero.utilizzo(sk),
                Test.rosso.utilizzo(sk),
                Test.verde.utilizzo(sk),
                Test.blu.utilizzo(sk),
                Test.bianco.utilizzo(sk),
                sk.larghezza(),
                sk.altezza(),
                sk.edifici(),
                )

################################################################################

    # Colore(r, g, b)           -> r, g, b interi tra 0 e 255
    @data(  [300,   0,   0], 
            [  0,2.55,   0], 
            [  0,   0, '255'], 
            [-10,   0,   0], 
            [256, None, 256] 
            )
    @unpack
    def test_01a_Colore_parametri_errati(self, r, g, b):
        '''tenta di creare dei colori con parametri errati'''
        with self.assertRaises(ValueError):
            Colore(r, g, b)

    # Colore(r, g, b)           -> r, g, b interi tra 0 e 255
    # to_tuple()
    @data(  ['rosso'  , 255,   0,   0], 
            ['verde'  ,   0, 255,   0], 
            ['blu'    ,   0,   0, 255], 
            ['nero'   ,   0,   0,   0], 
            ['bianco' , 255, 255, 255] 
            )
    @unpack
    def test_01b_Colore(self, nome, r, g, b):
        '''Crea dei colori e ne controlla i valori con to_tuple'''
        c = Colore(r, g, b)
        self.check(c.to_tuple(),  (r, g, b), None, "Questo colore non è {}".format(nome))
        setattr(type(self), nome, c)

    # Colore.utilizzo(Skyline)
    @data(  ['rosso', None],
            ['verde',   42],
            ['nero',  12.3],
            ['blu',  'blu'],
            ['bianco', Colore(0,0,0) ]
            )
    @unpack
    def test_02a_Colore_utilizzo_errato(self, colore, skyline):
        '''tenta di chiedere utilizzo() con skyline errata'''
        c = getattr(Test, colore)
        with self.assertRaises(ValueError):
            c.utilizzo(skyline) 


################################################################################

    # Rettangolo(base, altezza, colore) -> base, altezza interi positivi
    # istanziazione errata
    @data(  [  0,  20, Colore()],
            [ 20,   0, Colore()],
            [-20,  10, Colore()],
            [ 20, -10, Colore()],
            [ 20,  10, 'colore'],
            )
    @unpack
    def test_10a_Rettangolo_parametri_errati(self, w, h, colore):
        '''tenta di creare rettangoli con parametri errati'''
        with self.assertRaises(ValueError):
            Rettangolo(w, h, colore) 

    # istanziazione corretta
    # Rettangolo.to_tuple()
    @data(  ['r1', 'rosso'  , 50, 50], 
            ['r2', 'verde'  , 70, 90], 
            ['r3', 'blu'    , 20, 70], 
            ['r4', 'bianco' , 60, 40], 
            ['r5', 'nero'   , 60,120], 
            )
    @unpack
    def test_10b_Rettangolo(self, nome, colore, w, h):
        '''Crea dei rettangoli, li controlla e li mette da parte'''
        c = getattr(self, colore)
        r = Rettangolo(w, h, c)
        base, altezza, col = r.to_tuple()
        self.check(base,    w, None, "Questo Rettangolo non è largo {}".format(w))
        self.check(altezza, h, None, "Questo Rettangolo non è alto {}".format(h))
        self.check(col,     c, None, "Questo Rettangolo non ha il colore {}".format(colore))
        setattr(type(self), nome, r)

################################################################################

    # Skyline(sfondo)
    # istanziazione errata
    @data(  10,
            10.3,
            'colore',
            None
            )
    def test_20a_Skyline_errata(self, colore):
        '''tenta di creare skyline con parametri errati'''
        with self.assertRaises(ValueError):
            Skyline(colore) 

    # Skyline(sfondo)
    # istanziazione corretta
    @data(  ['s1', 'verde'],
            ['s2', 'rosso'],
            ['s3', 'blu'  ],
            )
    @unpack
    def test_20b_Skyline(self, nome, colore):
        '''tenta di creare skyline con parametri corretti'''
        c = getattr(self, colore)
        s = Skyline(c)
        (col, ) = s.to_tuple()
        h = s.altezza()
        w = s.larghezza()
        N = s.edifici()
        self.check( col,     c,     None, "il colore di sfondo non è giusto")
        self.check( id(col), id(c), None, "il colore di sfondo non è lo stesso passato al costruttore")
        self.check( h,       0,     None, "All'inizio una Skyline deve avere altezza 0")
        self.check( w,       0,     None, "All'inizio una Skyline deve avere larghezza 0")
        self.check( N,       0,     None, "All'inizio una Skyline deve avere 0 edifici")
        setattr(type(self), nome, s)

    # Skyline.aggiungi(self, Rettangolo, x)     x -> intero >= 0
    @data( ['s1', 'r1', -10 ],  # pos errata
           ['s1', 'r1', None],  # pos mancante
           ['s2', None,  20 ],  # rettangolo mancante
           ['s2',  -34,  20 ],  # intero invece di rettangolo
           )
    @unpack
    def test_21a_Skyline_aggiungi_errato(self, sk, r, pos):
        '''Data una Skyline e cerca di aggiungere una cosa sbagliata'''
        s = getattr(self, sk)
        if type(r) == str:
            r = getattr(self, r)
        with self.assertRaises(ValueError):
            s.aggiungi(r, pos)

    # Skyline.aggiungi(self, Rettangolo, x)     x -> intero >= 0
    @data( ['s1',  [('r1',10), ('r2',90), ('r3',180)            ], 0, 1, 0, 1, 0, 200,  70, 2, 'es2_test21_1.png', 'es2_risTest21_1.png'],
           ['s2',  [('r4',30), ('r5',70), ('r2',110), ('r4',150)], 1, 0, 1, 0, 2, 210, 120, 4, 'es2_test21_2.png', 'es2_risTest21_2.png'],
           ['s3',  [('r1',30), ('r1',70), ('r1',110), ('r1',150),
                    ('r2',40), ('r2',80), ('r2',120), ('r2',160),
                    ('r3',50), ('r3',90), ('r3',130), ('r3',170),
                    ('r4',60), ('r4',10), ('r4',140), ('r4',180),
                    ('r5',70), ('r5',20), ('r5',150), ('r5',190),
                    ], 2, 4, 4, 0, 4, 250, 120, 14, 'es2_test21_3.png', 'es2_risTest21_3.png'],
           )
    @unpack
    def test_21b_Skyline_aggiungi(self, nome, rettangoli, nu, ru, vu, bu, wu, w, h, N, file1, file2):
        '''Crea una Skyline con N rettangoli'''
        s = getattr(self, nome)
        for r, pos in rettangoli:
            s.aggiungi(getattr(self, r), pos)
        self.do_test(s, nu, ru, vu, bu, wu, w, h, N, file1, file2)
        setattr(type(self), nome, s)

    # Skyline.fondi(Skyline)
    @data(  ['s1', None],
            ['s2', -34],
            ['s2', 'stringa'],
            )
    @unpack
    def test_22a_Skyline_fondi_errato(self, s1, s2):
        s1 = getattr(Test, s1)
        with self.assertRaises(ValueError):
            s1.fondi(s2)

    # Skyline.fondi(Skyline)
    @data(  ['s11', 'rosso', 's1', 's2', [ 1, 0, 1, 1, 2, 210, 120,  5], 'es2_test22_1.png', 'es2_risTest22_1.png'],
            ['s12', 'blu',   's2', 's3', [ 3, 0, 5, 0, 6, 250, 120, 14], 'es2_test22_2.png', 'es2_risTest22_2.png'],
            ['s13', 'nero',  's3', 's1', [ 0, 4, 4, 0, 4, 240,  90, 12], 'es2_test22_3.png', 'es2_risTest22_3.png'],
            )
    @unpack
    def test_22b_Skyline_fondi(self, nome, colore, s1, s2, s_specs, file1, file2):
        '''Fonde due Skyline producendone una terza'''
        c = getattr(Test, colore)
        s = Skyline(c)
        s1 = getattr(Test, s1)
        s1_specs = self.skyline_specs(s1)
        s2 = getattr(Test, s2)
        s2_specs = self.skyline_specs(s2)
        s.fondi(s1)
        s.fondi(s2)
        self.do_test(s1, *s1_specs)
        self.do_test(s2, *s2_specs)
        # print(self.skyline_specs(s))
        self.do_test(s,  *s_specs, file1, file2)
        setattr(type(self), nome, s)

    # Skyline.salva(filename)
    @data(  ['s1', None],
            ['s2', -34],
            ['s3', 'stringa'],
            )
    @unpack
    def test_23a_Skyline_salva_errato(self, s1, filename):
        s1 = getattr(Test, s1)
        with self.assertRaises(ValueError):
            s1.salva(filename)

################################################################################

    # Rettangolo.cancella()
    @data(  ['r3', 's11', [ 1, 0, 1, 0, 2, 210, 120,  4], 'es2_test30_1.png', 'es2_risTest30_1.png'],
            ['r5', 's12', [ 0, 0, 5, 0, 6, 240,  90, 11], 'es2_test30_2.png', 'es2_risTest30_2.png'],
            ['r1', 's13', [ 0, 0, 4, 0, 4, 240,  90,  8], 'es2_test30_3.png', 'es2_risTest30_3.png'],
            )
    @unpack
    def test_30_Rettangolo_cancella(self, nome, sk, sk_specs, file1, file2):
        '''Elimina un rettangolo'''
        r  = getattr(Test, nome)
        sk = getattr(Test, sk)
        r.cancella()
        # print(self.skyline_specs(sk))
        self.do_test(sk, *sk_specs, file1, file2)

if __name__ == '__main__':
    Test.main()

