
import sys
from time       import sleep
from copy       import deepcopy
from gwidget    import *
from random     import randint
from importlib  import import_module

#from PyQt5.QtMultimedia import *

# TODO:
# - log del n° di step, id della macchina, n° di lap eccetera
# - log csv per poter ricostruire calcoli o replay
# - modalità headless senza grafica
# - torneo tra due player
# - esecuzione su più piste di gara
# - verso di rotazione (orario/antiorario)

from mappe import *

colors = {
        ' ' : (128, 128, 128),  # grigio        strada
        '#' : (128, 255, 128),  # verdino       prato
        'O' : (255, 255, 128),  # giallo        buca
        '|' : (255, 255, 255),  # bianco        traguardo
        '*' : (255, 128, 255),  # magenta       altro
        'A' : (255,   0, 255),  # viola         auto
        'B' : (  0,   0, 255),  # blu           auto
        'X' : (  0,   0, 255),  # blu           auto
        }

tilesize = 20

DEBUG = True
DEBUG = False
class Car:
    '''
    Una macchina contiene le sue informazioni di stato (posizione, velocita')
    e la funzione 'ai' caricata dal modulo indicato
    '''
    def __init__(self, player, car='X'):
        '''Simulazione di una gara per un giocatore.
            player= modulo che contiene la funzione ai()
            car   = carattere che individua la macchina sulla pista (A,X,B)
        '''
        self.simulatore   = None            # riferimento al simulatore che contiene la mappa
        self.player       = player          # modulo che contiene la funzione ai
        self.module       = import_module(player)
        self.ai           = self.module.ai
        self.x,  self.y   = 0, 0            # posizione
        self.vx, self.vy  = 0, 0            # velocità
        self.px, self.py  = 0, 0            # posizione precedente
        self.startx, self.starty  = 0, 0    # posizione iniziale
        self.laps         = 0               # quante volte ha superato il traguardo nella direzione giusta
        self.car          = car             # carattere della macchina (A,B,X)
        self.botto        = False           # ha urtato contro un ostacolo o una macchina?
        self.completed    = False           # ha completato la gara? (laps>0 e velocita' zero)
        self.steps        = 0
        self.replay       = []              # se vogliamo il replay di una corsa qui abbiamo le posizioni
        self.verso        = 1
        self.fermo        = 0

    def inside(self):
        '''Torna True se la posizione e' nella griglia.'''
        return 0 <= self.x < self.simulatore.width and 0 <= self.y < self.simulatore.height

    def traguardo(self):
        '''Torna True se in questo step si e' attraversato il traguardo nella direzione corretta.'''
        # FIXME?
        miny = min(self.py, self.y)
        maxy = max(self.py, self.y)
        for y in range(miny, maxy+1):                                       # per tutte le righe attraversate dal movimento
            if self.vx != 0:                                                # ma solo se la macchina si è mossa di almeno una casella
                for x in range(self.px, self.x+self.verso, self.verso):     # per tutte le colonne attraversate dal movimento nella direzione di partenza
                                                                            # range torna lista vuota se il verso è opposto alla direzione da px a x
                    if self.simulatore.griglia_corr[y][x] is '|':           # se è presente il traguardo
                        return True
        else:
            return False

    def inversione(self):
        '''Torna True se in questo step si e' attraversato il traguardo nella direzione sbagliata.'''
        # FIXME?
        miny = min(self.py, self.y)
        maxy = max(self.py, self.y)
        for y in range(miny, maxy+1):                                       # per tutte le righe attraversate dal movimento
            if self.vx != 0:                                                # ma solo se la macchina si è mossa di almeno una casella
                for x in range(self.px, self.x+self.verso, -self.verso):    # per tutte le colonne attraversate dal movimento nella direzione opposta alla partenza
                                                                            # range torna lista vuota se il verso è opposto alla direzione da px a x
                    if self.simulatore.griglia_corr[y][x] is '|':           # se è presente il traguardo
                        return True
        else:
            return False

    def step(self, ax, ay):
        '''Esegue uno step di simulazione usando l'accelerazione fornita da ai()
            torna True se la macchina e' ancora in gioco, False se il gioco e' finito o ha urtato.
        '''
        assert ax in [-1, 0, 1], "Accelerazione x fuori dal range permesso (-1, 0, 1)"
        assert ay in [-1, 0, 1], "Accelerazione y fuori dal range permesso (-1, 0, 1)"
        assert not self.botto, "Non posso eseguire un step se hai sbattuto"
        if self.laps > 0 and self.vx == self.vy == 0:
            self.completed = True
            return False
        self.px     = self.x    # pos precedente
        self.py     = self.y
        self.vx    += ax        # velocita'
        self.vy    += ay
        self.x     += self.vx   # nuova posizione
        self.y     += self.vy
        self.steps += 1         # uno step in più

        if self.vx or self.vy:
            self.fermo = 0
        else:
            self.fermo += 1
        if self.replay:
            if self.steps < len(self.replay):
                self.x, self.y, self.vx, self.vy = self.replay[self.steps]
                print("replaying: {0.car} {0.player} pos {0.x},{0.y} speed {0.vx},{0.vy} ".format(self))
            else:
                return False

        if not self.inside():
            self.botto = True
            return False

        c = self.simulatore.griglia_corr[self.y][self.x]
        while c == 'O':         # se finisco in una buca slitto a caso in una casella vicina (che potrebbe essere di nuovo una buca)
            sx = randint(-1,1)
            sy = randint(-1,1)
            self.x += sx        # nuova posizione
            self.y += sy
            print('slittato! player: {0.player} {0.car} x: {0.x} y: {0.y}'.format(self))
            if not self.inside():
                self.botto = True
                return False
            c = self.simulatore.griglia_corr[self.y][self.x]

        #print("moving car {0.car} with a: {1},{2} from {0.px},{0.py} to {0.x},{0.y} ".format(self, ax, ay))

        if c in ' |':     # se tutto OK (pista o traguardo)
            if self.traguardo():
                self.laps += 1
            elif self.inversione():
                self.laps -= 1
            return True
        elif c in 'ABX':
            pass    # ignoro l'urto con una macchina che viene gestito in handle_collisions
        else:
            print("botto! {.car} ha urtato {}".format(self,c))
            self.botto = True
            return False

    def done(self):
        '''True se esplosa oppure finito il giro'''
        if self.fermo > 5:
            print("L'auto {0.car} del giocatore {0.player} e' ferma da piu' di 5 steps ... (ma perche'?)".format(self))
            self.completed = True
        return self.botto or self.completed

    def __repr__(self):
        return '\n' + self.status()

    def __str__(self):
        return self.status()

    def status(self):
        '''Riga di status'''
        return '{0.steps:5d} car: {0.car} player: {0.player}   x:{0.x:5d}    y:{0.y:5d}    vx:{0.vx:5d}    vy:{0.vy:5d}    giri:{0.laps:5d}  Urtato: {0.botto} Finito: {0.completed}'.format(self)

    def draw(self, painter):
        '''Disegna la macchina sulla pista/widget'''
        if self.botto:              # esplosione = quadrato rosso
            r, g, b = 255, 0, 0
            painter.setPen(QColor(r,g,b))
            painter.setBrush(QColor(2*r//3, 2*g//3, 2*b//3))
            painter.drawRect((self.x-1)*tilesize, (self.y-1)*tilesize, 3*tilesize, 3*tilesize)
        else:                       # tutto bene = quadratino colorato
            r, g, b = colors[self.car]
            painter.setPen(QColor(r,g,b))
            painter.setBrush(QColor(2*r//3, 2*g//3, 2*b//3))
            painter.drawRect(self.x*tilesize, self.y*tilesize, tilesize, tilesize)

class Simulatore:
    '''Il simulatore gestisce una lista di Car su una pista'''

    def __init__(self, cars=[], pista='monza'):
        '''Simulazione di una gara per un giocatore.
            cars  = macchine sulla pista (A,X,B)
            corsa = nome del circuito
            il verso della corsa (-1,+1) dipende dalla posizione del carattere rispetto al traguardo.
            Il traguardo e' sempre su un tratto orizzontale ed ha almeno 3 caselle di larghezza.
        '''
        self.cars         = cars
        self.pista        = pista
        for car in cars:  car.simulatore = self             # ciascuna sa chi la simula
        self._decode_griglia(piste[pista], cars)            # setta le pos delle car e genera la griglia vuota
        self.height       = len(self.griglia_vuota)         # dimensioni
        self.width        = len(self.griglia_vuota[0])      #
        self.steps        = 0                               # numero di steps
        self.griglia_corr = deepcopy(self.griglia_vuota)    # costruisce la posizione iniziale
        for car in cars:
            self.griglia_corr[car.y][car.x] = car.car
        self.griglia_prec = deepcopy(self.griglia_corr)     # all'inizio la griglia precedente è la stessa
        self.done         = False
        self.logfile      = None

    def _decode_griglia(self, mappa, cars):
        '''
        Decodifica la mappa e ricava la griglia vuota (lista di liste di caratteri), le posizioni iniziali delle Car e le direzioni di gara.
        '''
        if DEBUG: print("Decoding map {.pista}".format(self))
        griglia = []
        for y,linea in enumerate(mappa):
            riga = []
            for x,carattere in enumerate(linea):
                if carattere in 'ABCDX':
                    riga.append(' ')
                    for car in cars:
                        if car.car == carattere:
                            car.x = car.startx = x
                            car.y = car.starty = y
                            print("player '{0.player}' starts at {0.x} {0.y} with car '{0.car}'".format(car))
                        if mappa[y][x+1] == '|':
                            car.verso = -1     # verso sinistra
                        else:
                            car.verso = +1     # verso destra
                else:
                    riga.append(carattere)
            griglia.append(riga)
        self.griglia_vuota = griglia

    def status(self):
        return "Step: {0.steps} {0.cars}".format(self)

    def __str__(self):
        s  =  self.status()
        #s += '\n' + '\n'.join([ ''.join(l) for l in self.griglia_corr])
        return s

    def draw(self, painter):
        '''disegna la mappa e le macchine (o l'esplosione)'''
        for y, line in enumerate(self.griglia_vuota):
            for x, c in enumerate(line):
                r, g, b = colors[c]
                painter.setPen(QColor(r,g,b))
                painter.setBrush(QColor(2*r//3, 2*g//3, 2*b//3))
                painter.drawRect(x*tilesize, y*tilesize, tilesize, tilesize)
        for car in self.cars:
            car.draw(painter)

    def step(self):
        '''Esegue uno step di simulazione per le sole macchine restate in gioco.'''
        if all([car.botto for car in self.cars]):           # se tutte esplose, basta
            print("ENORME PILE UP!!!")
            self.done = True
            return
        for car in self.cars:
            if car.completed:                               # se una ha vinto, basta
                # FIXME: gestire il caso in cui due passano il traguardo e si fermano nello stesso step
                print("Ha vinto '{}' con la macchina '{}' in {} steps!!!".format(car.player, car.car, self.steps))
                self.done = True
                return
        if all([car.done() for car in self.cars]):           # se tutte ferma basta
            print("STOP SIMULAZIONE: nessuno si sta muovendo")
            self.done = True
            self.steps = 0
            return
        self.griglia_prec = deepcopy(self.griglia_corr)     # copio la situazione corrente
        self.griglia_corr = deepcopy(self.griglia_vuota)    # costruisco la mappa aggiornata
        for car in self.cars:
            self.griglia_corr[car.y][car.x] = car.car       # con le auto
        for car in self.cars:
            if not car.done():                              # avanzando solo quelle che sono in gara
                if car.replay:
                    car.step(0, 0)
#                    print(car.status())
                else:
                    corr = deepcopy(self.griglia_corr)
                    prec = deepcopy(self.griglia_prec)
                    try:
                        res = car.ai(corr, prec, car.x, car.y, car.vx, car.vy, car.car, car.verso, car.startx, car.starty, car.laps)
                    except:
                        res = car.ai(corr, prec, car.x, car.y, car.vx, car.vy, car.car, car.verso, car.startx, car.starty, car.laps)
                    assert res, "La funzione 'ai' non torna nessun valore, hai dimenticato il return?"
                    ax, ay = res
                    car.step(ax, ay)
                    print(car.status())
        self.handle_collisions()                            # controllo se hanno sbattuto tra loro
        if self.logfile:
            self.log()
        self.steps += 1

    @classmethod
    def replay(cls, logfile):
        '''riesegue un log.'''
        cars = []
        with open(logfile) as play:
            firstline = play.readline().strip()
            pista, *players = firstline.split('|')          # monza|monti.A|p1.B
            for player in players:
                module, car = player.split('.')
                cars.append(Car(module, car))
            for line in play:                               # 100|xA.yA.vxA.xyA|xB.yB.vxB.vyB
                step, *posizioni = line.strip().split('|')
                for pos,car in zip(posizioni,cars):
                    car.replay.append([int(x) for x in pos.split('.')])
            for car in cars:
                car.x, car.y, car.vx, car.vy = car.replay[0]
                #print(car.x, car.y, car.replay)
        return cls(cars,pista)

    def handle_collisions(self):
        '''Se due macchine si urtano'''
        done = set()
        for car1 in self.cars:
            for car2 in self.cars:
                if car1 is not car2 and (car2, car1) not in done and \
                        car1.x == car2.x and car1.y == car2.y:
                    car1.botto = True
                    car2.botto = True
                    done.add((car1,car2))
                    print("Scontro mortale tra '{0.car}' guidata da '{0.player}' e '{1.car}' guidata da '{1.player}'!".format(car1, car2))

    def paint(self, painter):
        '''Se la gara non è finita simulo uno step e visualizzo'''
        if not self.done:
            self.step()
            self.draw(painter)

    def run(self):
        while not self.done:
            self.step()
            print(self)
            #sleep(1)
        return self.steps

    def start_log(self,logfile):
        self.logfile = logfile
        with open(logfile, mode='w', encoding='utf8') as f:
            f.write("{.pista}|{}\n".format(self,"|".join("{0.player}.{0.car}".format(car) for car in self.cars)))

    def log(self):
        '''Logs a step'''
        if self.logfile:
            with open(self.logfile, mode='a', encoding='utf8') as f:
                f.write("{.steps}|{}\n".format(self,"|".join(["{0.x}.{0.y}.{0.vx}.{0.vy}".format(car) for car in self.cars])))


####################################################################################

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--logfile',  default='program02-anello.log', type=click.Path(exists=True),   help='Nome del file di log da caricare per il replay')
@click.option('--speed',    default=50,                     type=int,                       help='Millisecondi per il refresh della simulazione (0=fastest possible)')
@click.option('--tile',     default=20,                     type=int,                       help='Dimensioni dei quadretti nella visualizzazione')
def replay(logfile, speed, tile):
    global tilesize
    tilesize = tile
    sim = Simulatore.replay(logfile)
    run_app(sim.paint, sim.width * tilesize, sim.height * tilesize, speed)


@cli.command()
@click.option('--pista',    default='anello',               type=click.Choice(piste),   help='Nome della pista')
@click.option('--logfile',  default='program02-anello.log', type=click.Path(),          help='Nome del file di log da creare')
@click.option('--players',  default='program02',                                        help='Nomi dei file dei giocatori (separati da virgola)')
def nogui(pista, logfile, players):
    players = players.split(',')
    available = 'ABCD'
    cars = []
    if len(players) == 1:
        cars.append(Car(players[0],'X'))
    else:
        for i in range(len(players)):
            cars.append(Car(players[i], available[i]))
    sim = Simulatore(cars, pista)
    sim.start_log(logfile)
    return sim.run()


@cli.command()
@click.option('--pista',    default='anello',             type=click.Choice(piste),  help='Nome della pista')
@click.option('--players',  default='program02',                                     help='Nomi dei file dei giocatori (separati da virgola)')
@click.option('--speed',    default=50,                   type=int,                  help='Millisecondi per il refresh della simulazione (0=fastest possible)')
@click.option('--tile',     default=20,                   type=int,                  help='Dimensioni dei quadretti nella visualizzazione')
def simulate(pista, players, speed, tile):
    global tilesize
    tilesize = tile
    players = players.split(',')
    available = 'ABCD'
    cars = []
    if len(players) == 1:
        cars.append(Car(players[0],'X'))
    else:
        for i in range(len(players)):
            cars.append(Car(players[i], available[i]))
    sim = Simulatore(cars, pista)
    run_app(sim.paint, sim.width * tilesize, sim.height * tilesize, speed)

if __name__ == '__main__':
    print("Per ottenere l'help usate il comando:")
    print("     python simulatore.py simulate --help")
    print("     python simulatore.py nogui    --help")
    print("     python simulatore.py replay   --help")
    cli()
