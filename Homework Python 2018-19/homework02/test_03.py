import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fname, expected):
        '''Implementazione del test
            - fname:    indirizzo del file di testo con percorsi ed insieme di quadrati
            - expected: numero intero atteso
        '''
        result   = program.es3(fname)
        self.assertNotEqual( result, None, "La funzione non torna nessun risultato")
        self.check(type(result), int,     None, "il risultato non e' un intero")
        self.check(result,       expected, None, "il risultato non e' corretto")
        return 1

    @file_data('test_03.json')
    def test_from_json(self, enabled, filename, expected, descrizione):
        if enabled:
            return self.do_test(filename, expected)
        else:
            raise unittest.SkipTest("Test disabled")

if __name__ == '__main__':
    Test.main()

