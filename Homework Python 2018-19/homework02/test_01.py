import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, cruci, expected):
        '''Implementazione del test
            - cruci:    indirizzo del file di testo con il crucipuzzle
            - expected: stringa risultante attesa
        '''
        self.maxDiff = None
        result   = program.es1(cruci)
        self.assertNotEqual( result, None, "La funzione non torna nessun risultato")
        self.check(type(result), str,     None, "il risultato non e' una stringa")
        self.check(result,       expected, None, "il risultato non e' corretto")
        return 1

    @file_data('test_01.json')
    def test_from_json(self, filename, expected, enabled):
        if enabled:
            return self.do_test(filename, expected)
        else:
            raise unittest.SkipTest("Test disabled")

if __name__ == '__main__':
    Test.main()

