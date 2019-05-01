'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco di una macchinetta che gira su una pista di formula 1.

Il gioco consiste in un percorso di gara, rappresentato da una griglia di caratteri
(' '=vuoto, '#' = ostacolo, 'A....Z' = auto, '|' = traguardo 'O' = buca tutti gli altri caratteri sono ostacoli)
nella quale si trova la macchina del giocatore (un carattere 'A..Z'), che deve:
    correre attorno alla pista per un intero giro senza sbattere contro ostacoli o altre macchine
    raggiungere il traguardo
    fermarsi senza sbattere (vx=vy=0)

Il punteggio di gioco e' il numero di step che sono stati necessari a percorrere la gara e fermarsi senza sbattere.

Ad ogni istante il simulatore della macchinetta conosce:
    x, y:   la posizione della macchina sulla griglia di gioco
    vx, vy: la velocita' corrente della macchina
Ad ogni step della simulazione il giocatore puo' solo:
    incrementare di 1, decrementare di 1 o lasciare come sono i valodi vx, vy della velocita' (-1,0,+1)
corrispondentemente il simulatore:
    somma gli incrementi/decrementi alle due variabili vx,vy
    somma le velocita' vx,vy alla posizione x,y ottenendo la prossima posizione della macchina
    controlla se la nuova posizione e' vuota
        se la nuova posizione e' occupata (da un ostacolo o da un'altra macchina) il gioco termina senza completare la corsa
        se la posizione contiene una buca si slitta di un carattere a caso fino a restare sulla strada o su un ostacolo
        altrimenti si sposta la macchina sulla nuova posizione
    se il traguardo e' stato raggiunto nella direzione giusta e la macchina e' ferma (vx=vy=0) la gara termina
    altrimenti si riesegue un nuovo step (chiedendo alla funzione 'ai' del giocatore cosa fare)

Il programma che dovete realizzare e' l'AI che guida la macchina, che riceve come input:
    la griglia di gioco del passo precedente (comprese le altre macchine)
    la griglia di gioco del passo corrente (comprese le altre macchine)
    la posizione x,y della propria macchina
    la velocita' vx,vy della propria macchina
    il carattere che individua la vostra macchina
    il verso di rotazione (-1= si parte verso sinistra rispetto al traguardo, +1= si parte verso destra rispetto al traguardo)
    la posizione startx,starty di partenza della macchina
e deve produrre in output la coppia:
    ax, ay  variazione della velocita (coppia di valori -1,0,+1)
La simulazione di tutti i 3 percorsi di gara per la qualificazione (senza visualizzazione) deve impiegare al piu' 1 minuto.

In questo esercizio la valutazione avverra' in tre fasi:
    giro di qualificazione: 
        la macchina gira sulla pista di gara da sola, senza altri concorrenti su 3 piste in cui non sono presenti barriere di buche
        superare questa prova da' il punteggio minimo di qualificazione (18)
    giro di premio:
        la macchina gira su una pista di gara simile (ma diversa) da quella "Roma" che contiene barriere di buche
        superare questa prova da' il punteggio di qualificazione 24

    La classifica ottenuta nella qualificazione viene usata per determinare i gironi e poi il torneo di gara della fase successiva
    chi non completa il giro di qualificazione non partecipa al successivo torneo e non e' sufficiente

    Gironi e torneo ad eliminazione:
        (per ogni scontro vengono eseguite due gare, con A a sinistra e B a destra e viceversa)
        viene organizzato un torneo in cui prima si eseguono dei gironi di 4-5 auto
            Le due auto che ottengono il miglior punteggio sul girone partecipano alle eliminatorie successive
            Per ogni gara del girone vengono assegnati:
                3 punti a chi vince la gara
                1 punto per pareggio o scontro
                0 punti a chi perde
                a parita' di punteggio vince la macchina che ha fatto meno incidenti
                a parita' di incidenti viene simulata un'altra gara con una pista con barriere di buche (tipo "roma" per intenderci)

        Le due auto qualificate di ciascun girone partecipano ad una fase eliminatoria a scontro diretto
            l'auto vincente passa il turno (in caso di patta su esegue una gara aggiuntiva con barriere di buche casuali)

    La classifica finale della fase a scontro diretto determina i voti:
        I livelli del torneo ad eliminazione individuano i voti ottenuti, a seconda del numero di partecipanti (per esempio 6 livelli -> 2.1 voti per livello circa)
        Per avere la sufficienza bisogna aver completato almeno il giro di qualificazione sulle diverse piste
        Se una macchina ha ottenuto il voto 24 nella fase di qualificazione, il voto finale dell'esercizio e' almeno 24

COMPORTAMENTO: le auto che usano comportamenti scorrette non superano la qualificazione. Es.
    - precalcolare offline la strategia e inserirla nel programma
    - andare apposta contro l'auto dell'avversario
    - ...

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti

'''

from random     import randint
from copy import copy

class Node:
    def __init__(self, value, point, goal):
        self.value = value
        self.x = point[0]
        self.y = point[1]
        self.G = 0 #distanza dall'inizio
        self.H = abs(self.x - goal[0]) + abs(self.y - goal[0])
        self.status = 2 # 0 = open |  1 = close  | 2 = not checked
        self.parent = None
        self.neighbors = []


    def getWeight(self):
        if self.value == 'O': return 100000000
        else:
            return self.G + self.H

def genNode(grid, goal, car):
    acceptable = [' ','O', car]
    lista_nodi = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in acceptable:
                n = Node(grid[y][x], (x,y), goal)
                lista_nodi.append(n)
    return lista_nodi


def getNodebyCoords(lst , x, y):
    # print(x,y,'aaasdbhwbd')
    for el in lst:
        if el.x == x and el.y == y:
            # print('trovato')
            return el


def getNeighbors(node, lstNodes):
    x,y = node.x , node.y
    comb = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    list = []
    for c in comb:
        n = getNodebyCoords(lstNodes, x+c[0], y+c[1])
        # print(n)
        if n != None:
            list.append(n)
    return list


def copyGrid(grid):
    newG = []
    for x in range(len(grid)):
        line = []
        for y in range(len(grid[0])):
            line += grid[x][y]
        newG.append(line)
    return newG

# def createGrid(grid):
#     newGrid = copyGrid(grid)
#     for x in range(len(newGrid)):
#         for y in range(len(newGrid[x])):
#             if grid[x][y] == ' ' or grid[x][y] == 'O':
#                 newGrid[x][y] = Node(grid[x][y], (x, y))
#     return newGrid

def getCoordsGoal(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '|': return (x,y)

def findGoalCoords(grid, verso):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '|':
                if verso == -1:
                    if grid[y][x + 1] == ' ': return (x+1, y)
                    if grid[y + 1][x + 1] == ' ': return (x+1, y+1)
                    if grid[y - 1][x + 1] == ' ': return (x+1, y-1)
                else:
                    if grid[y][x - 1] == ' ': return (x-1, y)
                    if grid[y + 1][x - 1] == ' ': return (x-1, y+1)
                    if grid[y - 1][x - 1] == ' ': return (x-1, y-1)



def Astar(start, goal, nodesLst):

    start.status = 1
    current = start
    path = []
    condition = False
    while not condition:
        near = getNeighbors(current, nodesLst)
        condition = (current.x == goal.x and current.y == goal.y)
        for n in near:
            if n.status == 0:
                if (n.getWeight() + 1) < n.getWeight():
                    n.parent = current
            elif n.status == 2:
                n.status = 0
                n.parent = current
        # nodesLst = sorted(nodesLst, key= lambda x: (x.G+x.H))
        nodesLst.sort(key= lambda x: x.getWeight())
        nodesPath = [x for x in nodesLst if x.status == 0]
        getNodebyCoords(nodesPath, nodesPath[0].x, nodesPath[0].y).status = 1
        current = nodesPath[0]
    n = goal
    while n:
        path.append((n.x,n.y))
        n = n.parent
    return list(reversed(path))

start = False
path = []
def ai(griglia_corrente, griglia_precedente, x, y, vx, vy, car, verso, startx, starty, laps):
    '''inserite qui il vostro codice'''
    global start
    global path
    if laps>0:
        start = False
        goal = None
        nodes = None
        startNode = None
        goalNode = None
        path = []
        return (-vx, -vy)
    if not start:
        start = True
        goal = findGoalCoords(griglia_corrente, verso)
        nodes = genNode(griglia_corrente,goal, car)
        startNode = getNodebyCoords(nodes, startx, starty)
        goalNode = getNodebyCoords(nodes, goal[0], goal[1])
        path = Astar(startNode, goalNode, nodes)
        # for p in range(1, len(path)):
        #     print(path[p][0]-path[p-1][0], path[p][1]-path[p-1][1])
        path.append(getCoordsGoal(griglia_corrente))
        return (0,0)
    else:
        if len(path) == 0:
            return (-vx, -vy)
        n = path[0]
        del path[0]
        tx, ty = 0,0
        if n[0] < x and vx != -1:
            tx = -1
        if n[0] == x:
            tx = tx-vx
        if n[0] > x and vx != 1:
            tx = 1
        if n[1] < y and vy != -1:
            ty = -1
        if n[1] == y:
            ty = ty-vy
        if n[1] > y and vy != 1:
            ty = 1
        
        return (tx, ty)


