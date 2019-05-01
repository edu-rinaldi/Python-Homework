import argparse, csv, glob, time, sys

import unittest

class TestCase(unittest.TestCase):

    def check(self, value, expected, params=None, explanation=''):
        # TODO: add deepcopy of value to avoid side effects
        msg = ''
        if params:
            msg += '\twhen input={} '.format(params)
        msg += '\n\t\t%r != %r' % (value, expected)
        if explanation:
            msg += "\t<- " + explanation
        self.assertEqual(value, expected, msg)

    def check_text_file(self,a,b):
        with open(a,'rU', encoding='utf8') as f: txt_a = f.read()
        with open(b,'rU', encoding='utf8') as f: txt_b = f.read()
        lines_a = [l.strip() for l in txt_a.splitlines()]
        lines_b = [l.strip() for l in txt_b.splitlines()]
        # todo: usare una diff
        msg = 'text differ: ' + a + ' ' + b
        self.assertEqual(lines_a, lines_b, msg)

    def __image_load(self, filename):
        '''Carica l'immagine in formato PNG dal file
        filename, la converte nel formato a matrice
        di tuple e la ritorna'''
        import png
        with open(filename,'rb') as f:
            # legge l'immagine come RGB a 256 valori
            r = png.Reader(file=f)
            iw, ih, png_img, _ = r.asRGB8()
            # converte in lista di liste di tuple
            img = []
            for png_row in png_img:
                row = []
                # l'immagine PNG ha i colori in
                # un'unico array quindi li leggiamo
                # tre alla volta in una tupla
                for i in range(0,len(png_row),3):
                    row.append( ( png_row[i+0],
                                  png_row[i+1],
                                  png_row[i+2] ) )
                img.append( row )
        return img

    def check_img_file(self, a,b):
        img_a = self.__image_load(a)
        img_b = self.__image_load(b)
        wa, ha = len(img_a[0]),len(img_a)
        wb, hb = len(img_b[0]),len(img_b)
        self.assertEqual(wa, wb, "images have different widts {} != {})".format(wa,wb))
        self.assertEqual(ha, hb, "images have different heights {} != {})".format(ha,hb))
        for y in range(ha):
            for x in range(wa):
                ca, cb = img_a[y][x], img_b[y][x] 
                msg = 'images differ, starting at coordinates {},{} (colors: {} != {})'.format(x, y, ca, cb)
                self.assertEqual(ca, cb, msg)

#    @classmethod
#    def main(_cls):
#        unittest.main()

    @classmethod
    def main(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
        result = runner.run(suite)
        failed = len(result.failures)
        passed = result.testsRun-failed
        print("{} test passed, {} tests failed".format(passed, failed))  

