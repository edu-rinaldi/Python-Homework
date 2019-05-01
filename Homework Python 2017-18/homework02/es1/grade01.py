#! /usr/bin/env python3 -B

from testlib import check, runtests
import program01
    
def test_program_1():
    "si cerca una parola tra i post in 'file01.txt'"
    args        = ('file01.txt', {'return'})
    expected    = {'6', '10', '2', '4'}
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0


def test_program_2():
    "si cercano due  parole tra i post in 'file01.txt'"
    args        = ('file01.txt', {'non','Si'})
    expected    = {'9', '24', '3', '21', '6', '17', '7', '4', '15'}
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0


def test_program_3():
    "si cerca una parola non presente tra i post in 'file01.txt'"
    args        =('file01.txt', {'no'})
    expected    = set()
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0

def test_program_4():
    "si cerca una parola in  'file01_20.txt'"
    args        =('file01_20.txt', {'Sorellina'})
    expected    = {'58112', '27338', '34258', '18465', '34019', '16759', '27263', '12383', '23950', 
 '24717', '38402', '3254', '47188', '12965', '6219', '14115', '17677', '52148',
 '63054', '51390', '1370', '65662', '68409', '40207', '21884', '17118', '58467',
 '20887', '2974', '7668', '36388', '13016', '35844', '24832', '18837', '33089',
 '726', '23787', '15271', '64729'}
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0

def test_program_5():
    "si cerca una parola in  'file01_40.txt'"
    args        =('file01_40.txt', {'campanelli'})
    expected    = {'29720', '40754', '22025', '85789', '37558', '53242', '120001', '109367', 
    '125019', '131005', '50260', '54635', '17291', '8295', '108302', '71227', '38231', '78882',
    '80481', '6855', '235', '31475', '76293', '84123', '117477', '99386', '93516', '114762', '71080', 
	'102337', '90799', '66057', '90166', '189', '73049', '8470', '27681', '18666', '128236', '82956'}
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0


def test_program_6():
    "si cerca un insieme di 26 parole di cui una sola presente in  'file01_40.txt'"
    args        =('file01_40.txt', {'campanell'+chr(c) for c in range(ord('a'), ord('z')+1)})
    expected    = {'29720', '40754', '22025', '85789', '37558', '53242', '120001', '109367', 
    '125019', '131005', '50260', '54635', '17291', '8295', '108302', '71227', '38231', '78882',
    '80481', '6855', '235', '31475', '76293', '84123', '117477', '99386', '93516', '114762', '71080', 
	'102337', '90799', '66057', '90166', '189', '73049', '8470', '27681', '18666', '128236', '82956'}
    explanation = "l' insieme corretto e' il secondo"
    returned    = program01.post(*args)
    check(returned, expected, args, explanation)
    return 1.0

tests = [test_program_1, test_program_2,test_program_3, test_program_4, test_program_5, test_program_6]


if __name__ == '__main__':
    runtests(tests)

