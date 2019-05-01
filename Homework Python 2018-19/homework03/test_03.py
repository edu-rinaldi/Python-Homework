import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

from program03 import Attore, Film, Regista, leggi_archivio_attori, leggi_archivio_film

pippo = 42

@ddt
class Test(testlib.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Carico i file per avere pezzi di json a disposizione'''
        with open('actors.json', encoding='utf8') as f:
            cls.attori_json = json.load(f)
        with open('films.json', encoding='utf8') as f:
            cls.films_json = json.load(f)

################################################################################

    def do_check_attore(self, a, nome, msg=''):
        '''Verifica che l'attore sia proprio quello del catalogo_attori'''
        self.assertEqual(type(a), Attore, f"Gli attori {msg} devono essere istanze di Attore")
        a1 = self.attori[nome]
        self.assertEqual(a.nome(), nome,  f"L'attore {msg} non è {nome}")
        self.assertTrue(a1 is a,
            f"Gli attori {msg} devono essere le stesse istanze che stanno nel catalogo_attori'")

    def do_check_film(self, f, titolo, msg=''):
        '''Verifica che il film sia proprio quello del catalogo_film'''
        self.assertEqual(type(f), Film, f"I film {msg} devono essere istanze di Film")
        f1 = self.films[titolo]
        self.assertEqual(f.titolo(), titolo,  f"Il film {msg} non è {titolo}")
        self.assertTrue(f1 is f,
            f"I film {msg} devono essere le stesse istanze che stanno nel catalogo_films'")

    def do_check_regista(self, r, nome, msg=''):
        '''Verifica che il regista sia proprio quello del catalogo_registi'''
        self.assertEqual(type(r), Regista, f"I registi {msg} devono essere istanze di Regista")
        r1 = self.registi[nome]
        self.assertEqual(r.nome(), nome,  f"Il regista {msg} non è {nome}")
        self.assertTrue(r1 is r,
            f"I registi {msg} devono essere le stesse istanze che stanno nel catalogo_registi'")

    def do_test_gruppo_attori(self, attori, tipo, nomi, msg=''):
        '''Verifica che gli attori tornati siano solo quelli indicati'''
        self.assertEqual(type(attori), tipo,        f"{msg} deve tornare un {tipo}")
        self.assertEqual(len(attori), len(nomi),    f"Gli attori tornati devono essere {len(nomi)}")
        for a in attori:
            self.assertTrue(a.nome() in nomi,       f"L'attore {a.nome()} non va tornato da {msg}")
            self.do_check_attore(a, a.nome(),         f'tornato da {msg}')
        for nome in nomi:
            a = self.attori[nome]
            self.assertTrue(a in attori,            f"L'attore {nome} manca nell'elenco tornato da {msg})")

    def do_test_gruppo_film(self, films, tipo, titoli, msg=''):
        '''Verifica che i film tornati siano solo quelli indicati'''
        self.assertEqual(type(films), tipo,         f"{msg} deve tornare un {tipo}")
        self.assertEqual(len(films), len(titoli),   f"I film tornati devono essere {len(titoli)}")
        for f in films:
            self.assertTrue(f.titolo() in titoli,   f"Il film {f.titolo()} non va tornato da {msg}")
            self.do_check_film(f, f.titolo(),       f'tornato da {msg}')
        for t in titoli:
            f = self.films[t]
            self.assertTrue(f in films,             f"Il film {t} manca nell'elenco tornato da {msg})")

    def do_test_gruppo_registi(self, registi, tipo, nomi, msg=''):
        '''Verifica che gli attori tornati siano solo quelli indicati'''
        self.assertEqual(type(registi), tipo,       f"{msg} deve tornare un {tipo}")
        self.assertEqual(len(registi), len(nomi),   f"I registi tornati devono essere {len(nomi)}")
        for r in registi:
            self.assertTrue(r.nome() in nomi,       f"Il regista {r.nome()} non va tornato da {msg}")
            self.do_check_regista(r, r.nome(),      f'tornato da {msg}')
        for nome in nomi:
            r = self.registi[nome]
            self.assertTrue(r in registi,           f"Il regista {nome} manca nell'elenco tornato da {msg})")

################################################################################

    @data(
        ['actors.json',     22233],
    )
    @unpack
    def test_00_load_attori(self, filename, N):
        '''controlla che vengano caricati gli attori'''
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            attori = leggi_archivio_attori(filename)
        self.assertEqual(type(attori), dict,  "Il risultato non è un dizionario")
        self.assertEqual(len(attori),  N,     f"Il dizionario creato da {filename} deve contenere {N} attori")
        for a in attori.values():
            self.assertEqual(type(a), Attore)
        Test.attori = attori

    @data(
        ['films.json',     2359, 1250],
    )
    @unpack
    def test_01_load_films(self, filename, NF, NR):
        '''controlla che vengano caricati i films e i registi'''
        with self.ignored_function('builtins.print'), self.ignored_function('pprint.pprint'):
            res = leggi_archivio_film(filename, Test.attori)
        self.assertEqual(type(res),       tuple,  "il risultato non è una tupla")
        self.assertEqual(len(res),        2,      "il risultato non ha due elementi")
        films, registi = res
        self.assertEqual(type(films),     dict,   "Il catalogo_film non è un dizionario")
        self.assertEqual(len(films),      NF,     f"Il dizionario creato da {filename} deve contenere {NF} films")
        self.assertEqual(type(registi),   dict,   "Il catalogo_registi non è un dizionario")
        self.assertEqual(len(registi),    NR,     f"Il catalogo_registi creato da {filename} deve contenere {NR} registi")
        for f in films.values():
            self.assertEqual(type(f), Film,       "Tutti i valori di catalogo_film devono essere Film")
        for r in registi.values():
            self.assertEqual(type(r), Regista,    "Tutti i valori di catalogo_registi devono essere Regista")
        Test.films   = films
        Test.registi = registi

        # TODO: controllo su almeno un paio di attori, film e registi

################################################################################

    def do_test_Attore_dati_base(self, attore, nome, eta, genere, truename):
        '''Verifica che l'attore contenga i dati base'''
        self.assertEqual(type(attore),      Attore,     "Non è una istanza di Attore")
        self.assertEqual(attore.nome(),     nome,       f"Il nome dell'attore non è {nome}")
        self.assertEqual(attore.eta(),      eta,        f"L'attore {nome} deve avere {eta} anni")
        self.assertEqual(attore.genere(),   genere,     f"L'attore {nome} è di genere {genere}")
        self.assertEqual(attore.vero_nome(),truename,   f"L'attore {nome} si chiamava {truename}")

    @data(
        # name                   age sex    vero_nome
        ['Marilyn Monroe',       37, 'F',   'Norma Jeane Mortenson'                 ],
        ['David Bowie',          72, 'M',   'David Robert Haywood Jones'            ],
        ['Marlon Brando',        81, 'M',   'Marlon Brando Jr.'                     ],
        ['Benedict Cumberbatch', 43, 'M',   'Benedict Timothy Carlton Cumberbatch'  ],
    )
    @unpack
    def test_10_new_Attore(self, nome, eta, genere, truename):
        '''Controlla che l'attore venga creato correttamente da un blocco di dati json'''
        json_data = self.attori_json[nome]
        attore = Attore(json_data)
        self.do_test_Attore_dati_base(attore, nome, eta, genere, truename)
        self.assertEqual(attore.films(),    set(),
                         f"I film dell'attore all'inizio devono essere un insieme vuoto")

################################################################################

    @data(
        # nome                  eta sex    vero_nome
        # titoli
        ['Marilyn Monroe',       37, 'F', 'Norma Jeane Mortenson'               ],
        ['Scarlett Johansson',   35, 'F', 'Scarlett Ingrid Johansson'           ],
        ['Benedict Cumberbatch', 43, 'M', 'Benedict Timothy Carlton Cumberbatch'],
    )
    @unpack
    def test_11_Attore_from_catalogo_attori(self, nome, eta, genere, vnome):
        '''Controlla che l'attore sia stato creato correttamente dal caricamento del file'''
        self.assertTrue(nome in self.attori, f"L'attore {nome} deve apparire nel catalogo_attori")
        attore = self.attori[nome]
        self.do_test_Attore_dati_base(attore, nome, eta, genere, vnome)

    @data(
        # nome
        ['Marilyn Monroe',
                 ['The Misfits', 'All About Eve', 'Monkey Business', 'The Seven Year Itch', 'Niagara',
                  'The Asphalt Jungle', 'Some Like It Hot', 'Gentlemen Prefer Blondes']],
        ['Scarlett Johansson',
                 ['Vicky Cristina Barcelona', "The Man Who Wasn't There", 'Lost in Translation',
                  'The Avengers', 'The Prestige', 'Ghost World', 'We Bought a Zoo', 'Girl with a Pearl Earring',
                  'Iron Man 2', 'Match Point', 'A Love Song for Bobby Long']],
        ['Benedict Cumberbatch',
                ['The Whistleblower', 'War Horse', 'Atonement', 'Amazing Grace', 'Tinker Tailor Soldier Spy']],
    )
    @unpack
    # Attore.films()
    def test_12_Attore_films(self, nome, titoli ):
        attore = self.attori[nome]
        films = attore.films()
        self.do_test_gruppo_film(films, set, titoli, f"Attore.films()")

    @data(
        # nome                   NA
        ['Marilyn Monroe',       84],
        ['Scarlett Johansson',  148],
        ['Benedict Cumberbatch', 67],
    )
    @unpack
    # Attore.coprotagonisti()
    def test_13_Attore_numero_coprotagonisti(self, nome, NA):
        attore = self.attori[nome]
        attori = attore.coprotagonisti()
        self.assertEqual(len(attori), NA, f"L'attore {nome} ha avuto {NA} coprotagonisti")
        for a in attori:
            self.do_check_attore(a, a.nome(), f'con cui ha lavorato {nome}')

    @data(
        # nome                  registi
        ['Marilyn Monroe',
         ['Howard Hawks', 'Henry Hathaway', 'Billy Wilder', 'Joseph L. Mankiewicz', 'John Huston']
         ],
        ['Scarlett Johansson',
         ['Woody Allen', 'Terry Zwigoff', 'Shainee Gabel', 'Joel Coen', 'Christopher Nolan', 'Peter Webber',
          'Joss Whedon', 'and 1 more credit', 'Sofia Coppola', 'Cameron Crowe', 'Jon Favreau']
         ],
        ['Benedict Cumberbatch',
         ['Tomas Alfredson', 'Larysa Kondracki', 'Michael Apted', 'Steven Spielberg', 'Joe Wright']],
    )
    @unpack
    # Attore.registi()
    def test_14_Attore_registi(self, nome, nomi):
        attore = self.attori[nome]
        registi = attore.registi()
        self.do_test_gruppo_registi(registi, set, nomi, f"Attore.registi()")

    @data(
        # nome                      PR
        ['Marilyn Monroe',          'Billy Wilder'  ],
        ['Scarlett Johansson',      'Woody Allen'   ],
        ['Benedict Cumberbatch',    'Joe Wright'    ],
    )
    @unpack
    # Attore.regista_preferito()
    def test_15_Attore_regista_preferito(self, nome, PR):
        attore = self.attori[nome]
        r = attore.regista_preferito()
        self.do_check_regista(r, PR, f'preferito di {nome}')

    @data(
        # nome                  minD maxD   titoli
        ['Marilyn Monroe',      90, 110,
            ['Gentlemen Prefer Blondes',
             'Niagara',
             'Monkey Business',
             'The Seven Year Itch',
             ],
         ],
        ['Scarlett Johansson',  90, 120,
            ['Vicky Cristina Barcelona',
             'Girl with a Pearl Earring',
             'Lost in Translation',
             'Ghost World',
             'Match Point',
             'The Man Who Wasn\'t There',
             'A Love Song for Bobby Long',
             ],
         ],
        ['Benedict Cumberbatch', 120, None,
            ['Atonement',
             'Tinker Tailor Soldier Spy',
             'War Horse',
            ],
         ],
    )
    @unpack
    # Attore.film_durata(minD, maxD)
    def test_16_Attore_film_durata(self, nome, minD, maxD, titoli):
        attore = self.attori[nome]
        films  = attore.film_durata(minD, maxD)
        self.do_test_gruppo_film(films, list, titoli)
        self.assertEqual(films, [self.films[t] for t in titoli])

    @data(
        # nome                  coppiette
        ['Scarlett Johansson',
            [('Robert Downey Jr.', 'Scarlett Johansson', 2),
             ('Samuel L. Jackson', 'Scarlett Johansson', 2),
             ('Paul Bettany',      'Scarlett Johansson', 2),
             ('Clark Gregg',       'Scarlett Johansson', 2),
             ],
         ],
        ['Woody Allen',
            [('Woody Allen', 'Diane Keaton',            6),
             ('Woody Allen', 'Joan Neuman',             2),
             ('Woody Allen', 'Anjelica Huston',         2),
             ('Woody Allen', 'Helen Hanft',             2),
             ('Woody Allen', 'Janet Margolin',          2),
             ('Woody Allen', 'Julia Louis-Dreyfus',     2),
             ('Woody Allen', 'Stephanie Roth Haberle',  2),
             ('Woody Allen', 'Mia Farrow',              4)
             ]
         ],
    )
    @unpack
    # Attore.in_coppia()
    def test_17_Attore_in_coppia_empty(self, nome, coppiette):
        attore = self.attori[nome]

        incoppia = attore.in_coppia()
        # print("################\n", [ (m.nome(), f.nome(), n) for m,f,n in incoppia] )
        self.assertEqual(type(incoppia), set,       "Attore.in_coppia() deve tornare un set di tuple")
        for t in incoppia:
            self.assertEqual(len(t), 3,             "Attore.in_coppia() deve tornare un set di terne")
            male, female, Nf = t
            self.assertEqual(type(male), Attore,    "Attore.in_coppia() deve tornare un set di terne il cui primo elemento è un Attore")
            self.assertEqual(type(female), Attore,  "Attore.in_coppia() deve tornare un set di terne il cui secondo elemento è un Attore")
            self.assertEqual(type(Nf), int,         "Attore.in_coppia() deve tornare un set di terne il cui terzo elemento è un int")
            self.assertEqual(male.genere(),     'M')
            self.assertEqual(female.genere(),   'F')
            terna = male.nome(), female.nome(), Nf
            self.assertTrue(terna in coppiette,         f"La terna {terna} non va tornata")
            self.do_check_attore(male, male.nome(),     f'tornato da in_coppia()')
            self.do_check_attore(female, female.nome(), f'tornato da in_coppia()')
        for M,F,N in coppiette:
            MM = self.attori[M]
            FF = self.attori[F]
            terna = MM, FF, N
            self.assertTrue( terna in incoppia,         f"La terna {terna} manca nell'elenco tornato da in_coppia()")

    @data(
        # nome                   partner              titoli
        ['Marilyn Monroe',       'Cary Grant',        ['Monkey Business']],
        ['Scarlett Johansson',   'Robert Downey Jr.', ['Iron Man 2', 'The Avengers',]],
        ['Benedict Cumberbatch', 'Keira Knightley',   ['Atonement', ]],
    )
    @unpack
    # Attore.in_coppia(partner)
    def test_18_Attore_in_coppia_partner(self, nome, partner, titoli):
        attore = self.attori[nome]
        films = attore.in_coppia(partner)
        self.do_test_gruppo_film(films, set, titoli, f'Attore.in_coppia({partner})')

        # TODO: what else?

    @data(
        ['Marcello Mastroianni',  'France'],
        ['Woody Allen',           'USA'   ],
    )
    @unpack
    def test_19_Attore_luogo_preferito(self, nome, LP):
        # Attore.attore_preferito()
        attore = self.attori[nome]
        luogo = attore.luogo_preferito()
        self.assertEqual(luogo, LP, f"Il luogo preferito di {nome} è {LP}")

################################################################################

    def do_check_Film_dati_base(self, film, titolo, durata, anno, posti):
        '''Verifica che i dati di base del film ci siano'''
        posti = set(posti)
        self.assertEqual(type(film),    Film,       f"{film} non è una istanza di Film")
        self.assertEqual(film.titolo(), titolo,     f"Il titolo del Film non è {titolo}")
        self.assertEqual(film.durata(), durata,     f"Il film {titolo} dovrebbe durare {durata} minuti")
        self.assertEqual(film.anno(),   int(anno),  f"Il film {titolo} è stato girato nel {anno}")
        self.assertEqual(film.luoghi(), posti,      f"Il film {titolo} è stato girato in {posti}")

################################################################################

    @data(
        # titolo                                durata
        ['Blazing Saddles;1974',                 93,    ['USA']                  ],
        ['Artificial Intelligence: AI;2001',    146,    ['USA']                  ],
        ['V for Vendetta;2005',                 132,    ['USA', 'UK', 'Germany'] ],
        # altri con durate strane
    )
    @unpack
    def test_20_new_Film(self, key, durata, posti):
        '''Controlla che il film venga creato correttamente da un blocco di dati json'''
        json_data = self.films_json[key]
        titolo, anno = key.split(';')
        film = Film(json_data)
        self.do_check_Film_dati_base(film, titolo, durata, anno, posti)
        self.assertEqual(film.attori(), set(),      f"Gli attori del film all'inizio devono essere un insieme vuoto")
        self.assertEqual(film.registi(),set(),      f"I registi del film all'inizio devono essere un insieme vuoto")

        # TODO: what else?

################################################################################

    @data(
        # titolo                                min  luoghi
        ['Blazing Saddles;1974',                 93, ['USA']                    ],
        ['Artificial Intelligence: AI;2001',    146, ['USA']                    ],
        ['V for Vendetta;2005',                 132, ['USA', 'UK', 'Germany']   ],
        ['Underground;1995',                    167, ['Federal Republic of Yugoslavia', 'France', 'Germany',
                                                      'Bulgaria', 'Czech Republic', 'Hungary']],
    )
    @unpack
    def test_21_Film_from_catalogo_film(self, key, durata, posti):
        '''Controlla che il film sia nel dizionario catalogo_film'''
        titolo, anno = key.split(';')
        self.assertTrue(titolo in self.films, f"Nel catalogo dei film ci dev'essere {titolo}")
        film = self.films[titolo]
        self.do_check_Film_dati_base(film, titolo, durata, anno, posti)

    @data(
        # titolo
        ['Blazing Saddles;1974',
         ['Carol Arthur', 'Cleavon Little', 'Mel Brooks', 'George Furth', 'Richard Collier', 'David Huddleston',
          'Slim Pickens', 'Madeline Kahn', 'Liam Dunn', 'Jack Starrett', 'Gene Wilder', 'Burton Gilliam',
          'Harvey Korman', 'Alex Karras', 'John Hillerman']],
        ['Artificial Intelligence: AI;2001',
         ['Theo Greenly', 'Ken Leung', 'Jude Law', 'William Hurt', 'Clark Gregg', 'Haley Joel Osment',
          'April Grace', 'Tom Gallop', 'Kevin Sussman', 'Eugene Osment', "Frances O'Connor",
          'Sabrina Grdevich', 'Jake Thomas', 'Sam Robards', 'Matt Winston']],
    )
    @unpack
    def test_22_Film_attori(self, key, nomiA):
        titolo, anno = key.split(';')
        film = self.films[titolo]
        attori = film.attori()
        self.do_test_gruppo_attori( attori,  set, nomiA, f"Film.attori()")

    @data(
        # titolo                                registi
        ['Blazing Saddles;1974',                ['Mel Brooks']],
        ['Artificial Intelligence: AI;2001',    ['Steven Spielberg']],
    )
    @unpack
    def test_23_Film_registi(self, key, nomiR):
        titolo, anno = key.split(';')
        film = self.films[titolo]
        registi = film.registi()
        # print('REGISTI', [r.nome() for r in registi])
        self.do_test_gruppo_registi(registi, set, nomiR, f"Film.registi()")

        # TODO: what else?

################################################################################

    @data(
        ['Michelangelo Antonioni',  ],
        ['Woody Allen',             ],
    )
    @unpack
    def test_30_new_Regista(self, nome):
        '''Controlla che il film venga creato correttamente da un blocco di dati json'''
        regista = Regista(nome)
        self.assertEqual(type(regista),     Regista, "Non è stata creata una istanza di Regista")
        self.assertEqual(regista.nome(),    nome,    f"Il nome del Regista non è {nome}")
        self.assertEqual(regista.films(),   set(),   f"I film del regista all'inizio devono essere un insieme vuoto")

        # TODO: what else?

################################################################################

    @data(
        ['Michelangelo Antonioni',   7, 16],
        ['Woody Allen',             25, 43],
    )
    @unpack
    def test_31_Regista_from_catalogo_registi(self, nome, NF, anni):
        '''Controlla che il film sia stato creato correttamente dal caricamento del file'''
        self.assertTrue(nome in self.registi,       f"Il regista {nome} deve apparire nel catalogo_registi")
        regista = self.registi[nome]
        self.assertEqual(type(regista), Regista,    "Nel catalogo_registi ci deve essere una istanza di Regista")

        # Regista.nome()
        self.assertEqual(regista.nome(), nome,      f"Il nome del Regista è {nome}")

        # Regista.anni_di_lavoro()
        self.assertEqual(regista.anni_di_lavoro(), anni, f"Il regista {nome} ha lavorato {anni} anni")

    @data(
        ['Michelangelo Antonioni',
         ["L'eclisse", 'La notte', 'Professione: reporter', 'Blowup', 'Il deserto rosso', 'Zabriskie Point',
          "L'avventura"]
         ],
        ['Woody Allen',
         ['Radio Days', 'Take the Money and Run', 'Bullets Over Broadway', 'Husbands and Wives', 'Stardust Memories',
          'Match Point', 'Zelig', 'Manhattan', 'Manhattan Murder Mystery', 'The Purple Rose of Cairo', 'Whatever Works',
          'Annie Hall', 'Love and Death', 'Sweet and Lowdown', 'Interiors', 'Another Woman', 'Crimes and Misdemeanors',
          'Midnight in Paris', 'Deconstructing Harry', 'Broadway Danny Rose', 'Mighty Aphrodite',
          'Vicky Cristina Barcelona', 'Bananas', 'Sleeper', 'Hannah and Her Sisters']
         ],
    )
    @unpack
    def test_31_Regista_films(self, nome, titoli):
        # Regista.films()
        regista = self.registi[nome]
        films = regista.films()
        # print("FILMS", [f.titolo() for f in films])
        self.do_test_gruppo_film(films, set, titoli, f"films del regista {nome}")

    @data(
        # regista                   attore preferito
        ['Michelangelo Antonioni',  'Monica Vitti'],
        ['Woody Allen',             'Woody Allen'],
    )
    @unpack
    def test_31_Regista_attore_preferito(self, nome, AP):
        # Regista.attore_preferito()
        regista = self.registi[nome]
        a = regista.attore_preferito()
        self.do_check_attore(a, AP, f'attore preferito di {nome}')

        # TODO: what else?

################################################################################

if __name__ == '__main__':
    Test.main()

