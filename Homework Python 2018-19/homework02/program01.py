'''
In enigmistica il crucipuzzle  e' uno schema di parole crociate dove non sono 
presenti le definizioni. E' composto da un elenco di parole ed un diagramma.
Per risolvere il crucipuzzle bisogna ricercare e poi cancellare dal diagramma TUTTE LE
OCCORRENZE (se multiple) delle parole presenti nell'elenco.
Le lettere del diagramma che rimarranno, prese tutte nel loro ordine per righe e per colonne,
formeranno la soluzione del gioco.
Le parole possono comparire  nel diagramma  in orizzontale (da destra verso sinistra, 
o da sinistra verso destra), in verticale  (dall'alto verso il basso o  dal basso verso 
l'alto)  e in diagonale (dall'alto verso il basso oppure dal basso verso l'alto).

Definire una funzione es1(ftesto), che prende l'indirizzo di un file di testo ftesto, 
contenente  diagramma ed elenco di parole di un crucipuzzle e restituisce la stringa 
soluzione del gioco. 
Il file fname  contiene  il diagramma  e, di seguito a questo  l'elenco delle parole.
Una serie di 1 o piu'  linee vuote precede il diagramma, separa il diagramma dall'elenco
delle parole e segue l'elenco delle parole.
Il diagramma e' registrato per righe (una riga per linea e in linee consecutive) gli 
elementi di ciascuna riga sono separati da un singolo carattere tab ('\t').
La lista delle parole occupa linee consecutive, una parola per ciascuna linea. 
Per un esempio si vedano i file di testo cp*.txt.

NOTA: il timeout previsto per questo esercizio è di XXX secondi per ciascun test
(il timeout definitivo verrà indicato non appena avremo generato le altre istanze di test)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)
''' 

def es1(ftesto):
    matrice = getMatrice(ftesto)
    parole = elencoParole(ftesto)
    coordinateDaSaltare = set()
    coordinateMatrice = set()
    #scorro la matrice
    for y in range(len(matrice)):
        for x in range(len(matrice[y])):
            coordinateMatrice.add((y, x))
            coordinateDaSaltare = coordinateDaSaltare | orizzontaleDestra(matrice, y, x, parole) | orizzontaleSinistra(matrice, y, x, parole) | \
            verticaleGiu(matrice, y, x, parole) | verticaleSu(matrice, y, x, parole) | obliquoGiuDestra(matrice, y, x, parole) | \
            obliquoGiuSinistra(matrice, y, x, parole) | obliquoSuDestra(matrice, y, x, parole) | obliquoSuSinistra(matrice, y, x, parole)
    coordinateParola = sorted(coordinateMatrice - coordinateDaSaltare)
    parola = ''
    for y, x in coordinateParola:
        parola += matrice[y][x]
    return parola   
    
                
def getMatrice(ftesto):
    matrice = []
    with open(ftesto, encoding = 'utf-8') as lettere:
        for linea in lettere:
            if linea is not ('\n') and ('\t') in linea:
                matrice.append(linea.split())
    return matrice

def elencoParole(ftesto):
    parole = []
    with open(ftesto, encoding = 'utf-8') as lettere:
        for linea in lettere:
            if linea is not ('\n') and ('\t') not in linea:
                parole.append(linea.split()[0])
        return parole
    
def orizzontaleDestra(m, sy, sx, parole):
    s = ''
    coordinateTemp = set()
    for x in range(sx, len(m[sy])):
        s += m[sy][x]
        coordinateTemp.add((sy, x))
        if s in parole:
            return coordinateTemp
    return set()
        
def orizzontaleSinistra(m, sy, sx, parole):
    s = ''
    coordinateTemp = set()
    for x in range(sx, -1, -1):
        s += m[sy][x]
        coordinateTemp.add((sy, x))
        if s in parole:
            return coordinateTemp
    return set()

def verticaleSu(m, sy, sx, parole):
    s = ''
    coordinateTemp = set()
    for y in range(sy, -1, -1):
        s += m[y][sx]
        coordinateTemp.add((y, sx))
        if s in parole:
            return coordinateTemp
    return set()

def verticaleGiu(m, sy, sx, parole):
    s = ''
    coordinateTemp = set()
    for y in range(sy, len(m)):
        s += m[y][sx]
        coordinateTemp.add((y, sx))
        if s in parole:
            return coordinateTemp
    return set()

def limitiMatrice(m, y, x):
    return 0 <= y < len(m) and 0 <= x < len(m[0]) 


def obliquoGiuDestra(m, sy, sx, parole) :
     s = ''
     coordinateTemp = set()
     while limitiMatrice(m, sy, sx):
         s += m[sy][sx]
         coordinateTemp.add((sy, sx))
         if s in parole:
             return coordinateTemp
         sx += 1
         sy += 1
     return set()
 
def obliquoSuDestra(m, sy, sx, parole) :
     s = ''
     coordinateTemp = set()
     while limitiMatrice(m, sy, sx):
         s += m[sy][sx]
         coordinateTemp.add((sy, sx))
         if s in parole:
             return coordinateTemp
         sx += 1
         sy -= 1
     return set()
         
def obliquoSuSinistra(m, sy, sx, parole) :
     s = ''
     coordinateTemp = set()
     while limitiMatrice(m, sy, sx):
         s += m[sy][sx]
         coordinateTemp.add((sy, sx))
         if s in parole:
             return coordinateTemp
         sx -= 1
         sy -= 1
     return set()     


def obliquoGiuSinistra(m, sy, sx, parole) :
     s = ''
     coordinateTemp = set()
     while limitiMatrice(m, sy, sx):
         s += m[sy][sx]
         coordinateTemp.add((sy, sx))
         if s in parole:
             return coordinateTemp
         sx -= 1
         sy += 1
     return set()   
     
     
     
         
            
            
            
        
     
    
    
    
    
            
            
        
         

