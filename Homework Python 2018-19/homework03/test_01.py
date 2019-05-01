import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected1, expected2):
        '''Implementazione del test
            - f1:    indirizzo del file .PNG con la foto di partenza
            - f2:    indirizzo del file .PNG in cui registrare la foto prodotta
            - expected1: indirizzo con la foto che ci si aspetta
            - expected2: il numero atteso di rettangoli evidenziati
        '''
        with self.ignored_function('builtins.print'):
            result   = program.es1(f1,f2)
        self.check(type(result), int, None, "il risultato non e' un intero")
        self.check(result, expected1, None, "il numero restituito non e' corretto")
        self.check_img_file(f2, expected2)
        return 1

    @data(  ('figura100x100', 'e1_f1.png', 'e1_r1.png',   3,'e1_Risf1.png'),
            ('figura402X402', 'e1_f2.png', 'e1_r2.png',  50,'e1_Risf2.png'),
            ('figura100X100', 'e1_f3.png', 'e1_r3.png',   1,'e1_Risf3.png'),
            ('figura101X101', 'e1_f4.png', 'e1_r4.png',   1,'e1_Risf4.png'),
            ('figura101X101', 'e1_f5.png', 'e1_r5.png',   8,'e1_Risf5.png'),
            ('figura151X151', 'e1_f6.png', 'e1_r6.png',  81,'e1_Risf6.png'),
            ('figura201X201', 'e1_f7.png', 'e1_r7.png', 129,'e1_Risf7.png'),
            ('figura201X201', 'e1_f8.png', 'e1_r8.png',  47,'e1_Risf8.png'),
            ('figura301X301', 'e1_f9.png', 'e1_r9.png', 147,'e1_Risf9.png')
            )
    @unpack
    def test(self, descrizione, file1, file2, Nexpected, fileExpected):
        return self.do_test(file1, file2, Nexpected, fileExpected)

if __name__ == '__main__':
    Test.main()

