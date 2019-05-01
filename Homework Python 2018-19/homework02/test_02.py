import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program02 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Implementazione del test
            - fname:    indirizzo del file di testo con i post del forum
            - expected: stringa risultante attesa
        '''
        result   = program.es2(fname)
        self.assertNotEqual( result, None, "La funzione non torna nessun risultato")
        self.check(type(result), list,     None, "il risultato non e' una lista")
        for line in result:
            self.check(type(line), dict,     None, "alcune righe della tabella non sono dizionari")
        self.check(result,       expected, None, "il risultato non e' corretto")
        return 1

    def test_fp1(self):
        '''...'''
        tab1= [ {'parola': 'hw1',       'I1': 6, 'I2': 3, 'I3': (3, '30')},
                {'parola': 'python',    'I1': 3, 'I2': 2, 'I3': (2, '30')},
                {'parola': 'hw2',       'I1': 2, 'I2': 1, 'I3': (2, '1')},
                {'parola': '30',        'I1': 1, 'I2': 1, 'I3': (1, '21')},
                {'parola': 'monti',     'I1': 1, 'I2': 1, 'I3': (1, '30')},
                {'parola': 'spognardi', 'I1': 1, 'I2': 1, 'I3': (1, '1')},
                {'parola': 'sterbini',  'I1': 1, 'I2': 1, 'I3': (1, '21')},
                ]
        return self.do_test('fp1.txt', tab1)

    def test_fp2(self):
        '''file casuale con 5000 post ciascuno con al piu' 200 parole'''
        tab2=[  {'parola': 'h', 'I1': 69312, 'I2': 4991, 'I3': (39, '9533')},
                {'parola': 'd', 'I1': 69250, 'I2': 4979, 'I3': (37, '27312')},
                {'parola': 'b', 'I1': 69032, 'I2': 4984, 'I3': (38, '26089')},
                {'parola': 'c', 'I1': 69001, 'I2': 4990, 'I3': (38, '28149')},
                {'parola': 'a', 'I1': 68929, 'I2': 4980, 'I3': (41, '27893')},
                {'parola': 'f', 'I1': 68829, 'I2': 4981, 'I3': (38, '41778')},
                {'parola': 'e', 'I1': 68760, 'I2': 4984, 'I3': (39, '10436')},
                {'parola': 'g', 'I1': 68391, 'I2': 4987, 'I3': (38, '23016')}]
        return self.do_test('fp2.txt', tab2)
        
    def test_fp3(self):
        '''file casuale con 20000 post ciascuno 10 righe di 10 parole'''
        tab3=[  {'parola': 'f', 'I1': 252020, 'I2': 14805, 'I3': (70, '159467')},
                {'parola': 'b', 'I1': 251050, 'I2': 14736, 'I3': (70, '88881')},
                {'parola': 'c', 'I1': 250370, 'I2': 14778, 'I3': (60, '116575')},
                {'parola': 'd', 'I1': 249680, 'I2': 14723, 'I3': (60, '123864')},
                {'parola': 'h', 'I1': 249390, 'I2': 14778, 'I3': (60, '143501')},
                {'parola': 'a', 'I1': 249360, 'I2': 14713, 'I3': (70, '117737')},
                {'parola': 'g', 'I1': 249190, 'I2': 14688, 'I3': (70, '129128')},
                {'parola': 'e', 'I1': 248940, 'I2': 14698, 'I3': (60, '110325')}]
        return self.do_test('fp3.txt', tab3)
    def test_fp4(self):
        '''file casuale con 20000 post ciascuno 1 riga di 10 parole lunghe 5 con molte ripetizioni'''
        tab4=[{'parola': 'olceb', 'I1': 11182, 'I2': 8753, 'I3': (6, '30083')}, 
        {'parola': 'nomma', 'I1': 11168, 'I2': 8751, 'I3': (5, '152385')}, 
        {'parola': 'lhfdn', 'I1': 11150, 'I2': 8735, 'I3': (5, '103364')}, 
        {'parola': 'ddoco', 'I1': 11123, 'I2': 8659, 'I3': (6, '178894')}, 
        {'parola': 'cecob', 'I1': 11117, 'I2': 8714, 'I3': (5, '156445')}, 
        {'parola': 'idoli', 'I1': 11086, 'I2': 8631, 'I3': (5, '10056')}, 
        {'parola': 'nbmfh', 'I1': 11070, 'I2': 8678, 'I3': (5, '18469')}, 
        {'parola': 'lmdih', 'I1': 11060, 'I2': 8705, 'I3': (5, '153944')}, 
        {'parola': 'ihgoe', 'I1': 11012, 'I2': 8608, 'I3': (4, '100333')}, 
        {'parola': 'iabng', 'I1': 11007, 'I2': 8645, 'I3': (5, '100811')}, 
        {'parola': 'hfldi', 'I1': 11002, 'I2': 8608, 'I3': (5, '28713')}, 
        {'parola': 'gogae', 'I1': 10976, 'I2': 8606, 'I3': (5, '20218')}, 
        {'parola': 'ibfgf', 'I1': 10949, 'I2': 8572, 'I3': (5, '30180')}, 
        {'parola': 'ihbbf', 'I1': 10906, 'I2': 8536, 'I3': (5, '111018')}, 
        {'parola': 'ihbei', 'I1': 10905, 'I2': 8576, 'I3': (5, '11046')}, 
        {'parola': 'lehbl', 'I1': 10905, 'I2': 8551, 'I3': (6, '44277')}, 
        {'parola': 'hieao', 'I1': 10881, 'I2': 8570, 'I3': (6, '125464')}, 
        {'parola': 'loein', 'I1': 10838, 'I2': 8543, 'I3': (5, '137418')}, 
        {'parola': 'fnbdl', 'I1': 10835, 'I2': 8558, 'I3': (6, '41465')}, 
        {'parola': 'enbif', 'I1': 10828, 'I2': 8503, 'I3': (6, '54982')}]
        return self.do_test('fp4.txt', tab4)
    def test_fp5(self):
        '''file casuale con 30000 post ciascuno 1 riga di 1 parola lunghe 5 con molte ripetizioni'''
        tab5=[{'parola': 'lhfdn', 'I1': 16713, 'I2': 13085, 'I3': (5, '188905')}, 
        {'parola': 'ddoco', 'I1': 16692, 'I2': 13011, 'I3': (5, '113853')}, 
        {'parola': 'olceb', 'I1': 16660, 'I2': 13046, 'I3': (5, '219668')}, 
        {'parola': 'nbmfh', 'I1': 16622, 'I2': 13073, 'I3': (6, '207068')}, 
        {'parola': 'iabng', 'I1': 16610, 'I2': 13009, 'I3': (5, '213120')}, 
        {'parola': 'hfldi', 'I1': 16590, 'I2': 12950, 'I3': (5, '102838')}, 
        {'parola': 'ihgoe', 'I1': 16575, 'I2': 12954, 'I3': (5, '93622')}, 
        {'parola': 'nomma', 'I1': 16547, 'I2': 12943, 'I3': (5, '204077')}, 
        {'parola': 'idoli', 'I1': 16543, 'I2': 12928, 'I3': (5, '251936')}, 
        {'parola': 'cecob', 'I1': 16531, 'I2': 13067, 'I3': (5, '246310')}, 
        {'parola': 'lmdih', 'I1': 16509, 'I2': 12885, 'I3': (5, '151269')}, 
        {'parola': 'ihbei', 'I1': 16470, 'I2': 12935, 'I3': (5, '117487')}, 
        {'parola': 'lehbl', 'I1': 16445, 'I2': 12830, 'I3': (6, '199798')}, 
        {'parola': 'gogae', 'I1': 16432, 'I2': 12888, 'I3': (5, '121721')}, 
        {'parola': 'ihbbf', 'I1': 16426, 'I2': 12895, 'I3': (5, '143967')}, 
        {'parola': 'ibfgf', 'I1': 16419, 'I2': 12810, 'I3': (5, '120539')}, 
        {'parola': 'loein', 'I1': 16358, 'I2': 12932, 'I3': (6, '254695')}, 
        {'parola': 'hieao', 'I1': 16343, 'I2': 12846, 'I3': (6, '99989')}, 
        {'parola': 'enbif', 'I1': 16261, 'I2': 12753, 'I3': (5, '108131')}, 
        {'parola': 'fnbdl', 'I1': 16254, 'I2': 12768, 'I3': (6, '264957')}]
        return self.do_test('fp5.txt', tab5)

    def test_fp6(self):
        '''file casuale con 40000 post ciascuno 5 righe di 5 parole lunghe 5 con molte ripetizioni'''
        tab6=[{'parola': 'ddoco', 'I1': 60459, 'I2': 31573, 'I3': (8, '122458')}, 
        {'parola': 'idoli', 'I1': 60350, 'I2': 31483, 'I3': (8, '138828')}, 
        {'parola': 'nbmfh', 'I1': 60344, 'I2': 31544, 'I3': (8, '137701')}, 
        {'parola': 'lehbl', 'I1': 60243, 'I2': 31364, 'I3': (9, '82929')}, 
        {'parola': 'olceb', 'I1': 60230, 'I2': 31548, 'I3': (8, '35379')}, 
        {'parola': 'lmdih', 'I1': 60103, 'I2': 31429, 'I3': (10, '158535')}, 
        {'parola': 'hfldi', 'I1': 60091, 'I2': 31330, 'I3': (8, '181046')}, 
        {'parola': 'cecob', 'I1': 60090, 'I2': 31462, 'I3': (8, '128637')}, 
        {'parola': 'ihgoe', 'I1': 60030, 'I2': 31435, 'I3': (8, '220824')}, 
        {'parola': 'gogae', 'I1': 60026, 'I2': 31368, 'I3': (9, '97308')}, 
        {'parola': 'ihbei', 'I1': 59984, 'I2': 31434, 'I3': (8, '329139')}, 
        {'parola': 'nomma', 'I1': 59967, 'I2': 31499, 'I3': (8, '324402')}, 
        {'parola': 'ihbbf', 'I1': 59907, 'I2': 31492, 'I3': (8, '215042')}, 
        {'parola': 'loein', 'I1': 59902, 'I2': 31355, 'I3': (8, '226738')}, 
        {'parola': 'hieao', 'I1': 59887, 'I2': 31420, 'I3': (8, '335043')}, 
        {'parola': 'lhfdn', 'I1': 59767, 'I2': 31296, 'I3': (8, '103542')}, 
        {'parola': 'iabng', 'I1': 59737, 'I2': 31225, 'I3': (8, '286841')}, 
        {'parola': 'fnbdl', 'I1': 59728, 'I2': 31332, 'I3': (9, '381551')}, 
        {'parola': 'ibfgf', 'I1': 59693, 'I2': 31420, 'I3': (9, '135254')}, 
        {'parola': 'enbif', 'I1': 59462, 'I2': 31270, 'I3': (8, '207187')}]
        return self.do_test('fp6.txt', tab6)
    def test_fp7(self):
        '''file casuale con 50000 post ciascuno 5 righe di 5 parole lunghe 5 con molte ripetizioni'''
        tab7=[{'parola': 'ddoco', 'I1': 75497, 'I2': 39396, 'I3': (10, '260616')}, 
        {'parola': 'idoli', 'I1': 75364, 'I2': 39352, 'I3': (8, '186834')}, 
        {'parola': 'ihgoe', 'I1': 75276, 'I2': 39348, 'I3': (8, '28441')}, 
        {'parola': 'lehbl', 'I1': 75265, 'I2': 39261, 'I3': (8, '159359')}, 
        {'parola': 'nbmfh', 'I1': 75221, 'I2': 39438, 'I3': (9, '89618')}, 
        {'parola': 'olceb', 'I1': 75167, 'I2': 39347, 'I3': (10, '259853')}, 
        {'parola': 'cecob', 'I1': 75119, 'I2': 39496, 'I3': (8, '353038')}, 
        {'parola': 'hfldi', 'I1': 75080, 'I2': 39053, 'I3': (9, '356902')}, 
        {'parola': 'ihbei', 'I1': 75063, 'I2': 39390, 'I3': (9, '384302')}, 
        {'parola': 'gogae', 'I1': 75037, 'I2': 39189, 'I3': (8, '16723')}, 
        {'parola': 'lmdih', 'I1': 74983, 'I2': 39359, 'I3': (9, '350451')}, 
        {'parola': 'ihbbf', 'I1': 74948, 'I2': 39245, 'I3': (9, '175971')}, 
        {'parola': 'nomma', 'I1': 74904, 'I2': 39314, 'I3': (9, '335174')}, 
        {'parola': 'loein', 'I1': 74897, 'I2': 39144, 'I3': (8, '491451')}, 
        {'parola': 'iabng', 'I1': 74893, 'I2': 39216, 'I3': (8, '161337')}, 
        {'parola': 'hieao', 'I1': 74874, 'I2': 39203, 'I3': (8, '42145')}, 
        {'parola': 'ibfgf', 'I1': 74679, 'I2': 39199, 'I3': (9, '122865')}, 
        {'parola': 'lhfdn', 'I1': 74637, 'I2': 39110, 'I3': (8, '123533')}, 
        {'parola': 'fnbdl', 'I1': 74590, 'I2': 39118, 'I3': (8, '145034')}, 
        {'parola': 'enbif', 'I1': 74506, 'I2': 39090, 'I3': (8, '133594')}]
        return self.do_test('fp7.txt', tab7)
    def test_fp8(self):
        '''file casuale con 60000 post ciascuno 5 righe di 5 parole lunghe 5 con molte ripetizioni'''
        tab8=[{'parola': 'idoli', 'I1': 90442, 'I2': 47231, 'I3': (8, '214740')}, 
        {'parola': 'lehbl', 'I1': 90427, 'I2': 47180, 'I3': (8, '131183')}, 
        {'parola': 'ddoco', 'I1': 90379, 'I2': 47164, 'I3': (9, '560696')}, 
        {'parola': 'cecob', 'I1': 90301, 'I2': 47185, 'I3': (9, '165305')}, 
        {'parola': 'lmdih', 'I1': 90266, 'I2': 47144, 'I3': (9, '563055')}, 
        {'parola': 'ihgoe', 'I1': 90146, 'I2': 47192, 'I3': (8, '309287')}, 
        {'parola': 'hfldi', 'I1': 90131, 'I2': 46989, 'I3': (8, '445319')}, 
        {'parola': 'nbmfh', 'I1': 90067, 'I2': 47141, 'I3': (8, '395290')}, 
        {'parola': 'olceb', 'I1': 90049, 'I2': 47238, 'I3': (9, '247490')}, 
        {'parola': 'gogae', 'I1': 90043, 'I2': 47184, 'I3': (8, '174565')}, 
        {'parola': 'ihbbf', 'I1': 90034, 'I2': 47207, 'I3': (9, '265286')}, 
        {'parola': 'loein', 'I1': 89983, 'I2': 47122, 'I3': (8, '128490')}, 
        {'parola': 'ihbei', 'I1': 89934, 'I2': 47118, 'I3': (9, '6066')}, 
        {'parola': 'hieao', 'I1': 89917, 'I2': 47007, 'I3': (9, '331647')}, 
        {'parola': 'fnbdl', 'I1': 89893, 'I2': 47027, 'I3': (8, '220265')}, 
        {'parola': 'iabng', 'I1': 89792, 'I2': 47038, 'I3': (9, '109041')}, 
        {'parola': 'nomma', 'I1': 89663, 'I2': 47164, 'I3': (8, '111561')}, 
        {'parola': 'ibfgf', 'I1': 89612, 'I2': 47022, 'I3': (8, '152142')}, 
        {'parola': 'lhfdn', 'I1': 89609, 'I2': 46952, 'I3': (8, '141443')}, 
        {'parola': 'enbif', 'I1': 89312, 'I2': 46984, 'I3': (8, '141579')}]
        return self.do_test('fp8.txt', tab8)
#    def test_fp3b(self):
#        '''file casuale con 100000 post ciascuno 10 righe di 10 parole'''
#        tab4=[{'parola': 'h', 'I1': 1254590, 'I2': 73817, 'I3': (70, '30076')}, 
#        {'parola': 'b', 'I1': 1251490, 'I2': 73729, 'I3': (70, '134887')}, 
#        {'parola': 'e', 'I1': 1250600, 'I2': 73622, 'I3': (70, '313483')}, 
#        {'parola': 'a', 'I1': 1250300, 'I2': 73476, 'I3': (80, '702758')}, 
#        {'parola': 'd', 'I1': 1249940, 'I2': 73869, 'I3': (70, '431455')}, 
#        {'parola': 'c', 'I1': 1249850, 'I2': 73671, 'I3': (80, '170445')}, 
#        {'parola': 'f', 'I1': 1247410, 'I2': 73533, 'I3': (70, '114816')}, 
#        {'parola': 'g', 'I1': 1245820, 'I2': 73504, 'I3': (70, '258097')}]
#        return self.do_test('fp3b.txt', tab4)

if __name__ == '__main__':
    Test.main()

