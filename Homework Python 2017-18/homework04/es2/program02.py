'''
Il tris e' un popolarissimo gioco. Si gioca su una griglia quadrata di 3×3 caselle.
A turno, i due giocatori scelgono una cella vuota e vi disegnano il proprio simbolo
(un giocatore ha come simbolo una "o" e l'avversario una 'x').
Vince il giocatore che riesce a disporre tre dei propri simboli in linea retta
orizzontale, verticale o diagonale. Se la griglia viene riempita
senza che nessuno dei giocatori sia riuscito a completare una linea
retta di tre simboli, il gioco finisce in parità. Nel caso in cui il gioco
finisse in parità, la partita è detta "patta".
Per convenzione a griglia vuota la prima mossa spetta sempre al giocatore 'o'

Una configurazione del gioco e' dunque univocamente determinata  dal contenuto della griglia.

Nel seguito assumiamo che il contenuto della griglia sia  rappresentato tramite  lista di liste.
La dimensione della lista di liste M e'  3x3 ed   M[i][j] contiene  '', 'x', o 'o'  a seconda
che la cella della griglia appartenente all'iesima riga e j-ma colonna sia ancora libera,
contenga il simbolo 'x' o contenga il simbolo 'o'.

Data una configurazione C del gioco, l'albero di gioco per C e' l'albero che
si ottiene ricorsivamente partendo dalla configurazione C e assegnando come figli le configurazioni
che e' possibile ottenere da C con una mossa ulteriore del gioco. Ovviamente  risulteranno
foglie dell'albero i possibili esiti della partita vale a dire le diverse configurazioni cui e'
possibile arrivare partendo da C e che rappresentano patte, vittorie per 'o' o vittorie per 'x'.
Se veda ad esempio l'immagine albero_di_gioco.png che mostra l' albero di gioco che si ottiene a partire
dalla configurazione rappresentata da [['x', 'o', 'o'], ['x', 'x', 'o'], ['', '', '']]


Si consideri la seguente Classe di oggetti:


class NodoTris:
    def __init__(self, griglia):
        self.nome = griglia
        self.lista_figli = []


Bisogna progettare le seguente  funzione

gen_tree(griglia)
che, data la configurazione di gioco griglia,  costruisce l'albero di gioco che si ottiene a partire
dalla configurazione griglia e ne restituisce la radice. I nodi dell'albero devono essere
oggetti della classe NodoTris.

Per testare la correttezza della vostra implementazione di gen_tree() il grade utilizzera' quattro metodi
della   classe NodoTris che dovete comunque implementare:

1)
tipo(self)
che, dato un nodo NodoTris, restituisce:
 'o' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'o'
 'x' se la configurazione rappresentata dal nodo e' una configurazione di vittoria per il giocatore 'x'
 '-' se la configurazione rappresentata dal nodo e' una configurazione di patta
 '?' se la configurazione rappresentata dal nodo e' una configurazione di gioco non ancora terminato

2)
esiti(self)
che, dato un nodo radice di un albero di gioco, restituisce una tripla con i possibili
esiti della partita che ha come configurazione iniziale quella rappresentata dal nodo.
Piu' precisamente: il primo elemento della tripla  è il numero di  patte possibili,
il secondo è il numero di possibili vittorie  per il giocatore 'o' mentre  il terzo elemento
e' il numero di possibili vittorie per il giocatore 'x'.

3)
vittorie_livello(self, giocatore, h)
che, dato un nodo radice di un albero di gioco, uno dei due giocatori ed un intero h,
restituisce il numero di nodi che rappresentano una vittoria per il giocatore e si
trovano ad altezza h nell'albero. In altri termini restituisce il numero di vittorie possibili
per giocatore in esattamente h mosse, nella partita che ha come configurazione iniziale
quella rappresentata dalla radice dell'albero.

4)
strategia_vincente(self,giocatore)
che, dato un nodo radice di un albero di gioco ed uno dei due giocatori, restituisce True o False.
Restituisce True  se  giocatore ha una strategia vincente  nella partita
che ha come configurazione iniziale quella rappresentata dal nodo radice, False altrimenti.

Nota che un giocatore ha una strategia vincente rispetto ad una certa configurazione se,
qualunque siano le mosse dell'avversario ha sempre la possibilita' di rispondere in modo
che la partita termini con la sua vittoria.

Potete ovviamente definire ulteriori  funzioni e altri metodi per la   Classe NodiTris
se li  ritenete utili al fine della risoluzione del compito.

Potete assumere che le configurazioni di gioco rappresentate da griglia siano sempre configurazioni
lecite (vale a dire ottenute dopo un certo numero di mosse a parire dalla griglia vuota).


AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.

ATTENZIONE: i test vengono eseguiti con un timeout globale di 2*N secondi (se il grader esegue N test).
'''

import copy

class NodoTris:
    def __init__(self, griglia):
        self.nome = copy.copy(griglia)
        self.lista_figli = [] #lista dei nodi figli
        self.turno = ''
    def tipo(self):
        '''inserire qui il vostro codice'''
        if checkVictory(self.nome, 'o'): return 'o'
        if checkVictory(self.nome, 'x'): return 'x'
        for i in self.nome:
            if i == '':
                return '?'
        return '-'

    def esiti(self,o=0, x=0, patta=0):
        '''inserire qui il vostro codice'''
        if self.lista_figli == []:
            typeVictory = self.tipo()
            if typeVictory == 'o':
                o+=1

            if typeVictory == 'x':
                x+=1

            if typeVictory == '-':
                patta+=1

        else:
            for el in self.lista_figli:
                patta,o,x= el.esiti(o,x,patta)
        return (patta,o,x)

    def vittorie_livello(self, giocatore, h, level=0,countVictory=0):
        if level == h:
            if self.tipo() == giocatore: return countVictory+1
            else: return countVictory
        else:
            level+=1
            for element in self.lista_figli:
                countVictory = element.vittorie_livello(giocatore,h,level,countVictory)
            return countVictory

    def getStrategiaVincente(self, giocatore):
        if self.lista_figli == []:
            tipo = self.tipo()
            if tipo == giocatore: return 1
            if tipo == '-': return 0
            return -1
        if self.turno != giocatore:
            a = 1
            for child in self.lista_figli:
                a = min(a, child.getStrategiaVincente(giocatore))
        else:
            a = -1
            for child in self.lista_figli:
                a = max(a, child.getStrategiaVincente(giocatore))
        return a

    def strategia_vincente(self,giocatore):
        '''inserire qui il vostro codice'''
        if self.getStrategiaVincente(giocatore) == 1: return True
        return False







#-------------------------------------------------------funzioni check victory----------------------------------------

def checkHorizontal(griglia, simbol):
    if len(set(griglia[0:3])) == 1 and griglia[0] == simbol: return True
    if len(set(griglia[3:6])) == 1 and griglia[3] == simbol: return True
    if len(set(griglia[6:])) == 1 and griglia[6] == simbol:  return True
    return False


def checkVertical(griglia, simbol):
    for i in range(3):
        if griglia[i] == griglia[i+3] == griglia[i+6] == simbol:
            return True
    return False


def checkDiagonal(griglia, simbol):
    """"""
    if griglia[0] == griglia[4] == griglia[-1] == simbol: return True
    if griglia[2] == griglia[4] == griglia[6] == simbol: return True
    return False

def checkVictory(griglia, simbol):
    if checkHorizontal(griglia,simbol): return True
    if checkVertical(griglia, simbol): return True
    if checkDiagonal(griglia, simbol): return True
    return False



#-----------------------------------------------------genera albero----------------------------------------



def gen_tree(griglia):
    grid = changeGrid(griglia)
    return gen(grid)

def changeGrid(grid):
    lst = []
    for y in grid:
        lst+= y
    return lst

def gen(griglia, turnCircle = 0, simbols = ['o','x']):
    Node = NodoTris(griglia)
    Node.turno = simbols[turnCircle%2]
    if checkVictory(Node.nome, simbols[(turnCircle-1) % 2]):
        return Node
    for i in range(len(Node.nome)):
        if Node.nome[i] == '':
            Node.nome[i] = simbols[turnCircle % 2]
            Node.lista_figli.append(gen(Node.nome,turnCircle+1))
            Node.nome[i] = ''

    return Node
