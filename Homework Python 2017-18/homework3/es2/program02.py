'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import *


class Robot:

    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.x = 0
        self.y = 0
        self.faceTo = 0  # right = 0 |   down = 1    |   left = 2    |   up = 3
        self.movement = [(40,0),        (0,40),         (-40,0),         (0,-40)]
        self.bannedSquare = [(0,255,0) , (255,0,0)]
        self.next = True
        self.nextStep = (0, 0)
        self.step = 40
        self.rotationCount = 0
        self.historyString = ''

    def move(self):
        self.x += self.movement[self.faceTo][0]
        self.y += self.movement[self.faceTo][1]
        self.rotationCount = 0
        self.historyString += str(self.faceTo)


    def inside(self,y,x):
        return 0 <= y < len(self.chessboard)  and 0 <= x < len(self.chessboard[0])

    def checkNextStep(self):
        if (not self.inside(self.nextStep[1],self.nextStep[0])) or self.chessboard[self.nextStep[1]]  [self.nextStep[0]] in self.bannedSquare:
            return False
        else:
            return True

    def rotate90(self):
        self.faceTo = (self.faceTo+1)%4
        self.rotationCount += 1

    def drawPath(self,color):
        for y in range(self.y,self.y+self.step):
            for x in range(self.x,self.x+self.step):
                self.chessboard[y][x] = color


def startWalk(rob):
    while rob.rotationCount < 4:
        if rob.checkNextStep():
            rob.drawPath((0, 255, 0))
            rob.move()
        else:
            rob.rotate90()
        rob.nextStep = (rob.x + rob.movement[rob.faceTo][0], rob.y + rob.movement[rob.faceTo][1])

    rob.drawPath((0, 0, 255))

def cammino(fname,  fname1):
    '''Implementare qui la funzione'''
    chessboard = load(fname)
    rob = Robot(chessboard)
    startWalk(rob)

    save(rob.chessboard,fname1)
    return rob.historyString


