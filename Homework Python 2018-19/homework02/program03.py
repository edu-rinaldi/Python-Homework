'''
Una regione e' stata suddivisa concettualmente in quadrati adiacenti.
Ogni  quadrato della griglia risultante e' univocamente identificato da una 
coppia di interi positivi (x,y) ad indicare che il quadrato appartiene alla x-ma colonna 
e y-ma riga della griglia, CON IL QUADRATO (1,1) SITUATO IN BASSO A SINISTRA (ATTENZIONE!).

Disponiamo di robottini in grado di muoversi tra i quadrati della griglia ma solo in 
orizzontale (da sinistra verso destra) e verticale (dal basso verso l'alto). 
Uno spostamento del robottino viene indicato da un intero A (positivo o negativo). 
Se il robottino si trova nel quadratino di coordinate (x,y):
-  l'intero +A positivo indica uno spostamento in verticale fino al quadrato (x,y+|A|)
-  l'intero -A negativo indica uno spostamento in orizzontale della griglia fino al quadrato (x+|A|,y)
Una sequenza di interi (positivi o negativi) indica dunque un percorso del robottino.
Ad esempio se il robottino e' nel quadrato (1,1), la sequenza 5,-2,-2,2,-4 lo porta nel quadrato (9,8). 

Ci vengono forniti un insieme I di quadrati della griglia indicati dalle loro coordinate (x,y)
e due percorsi di due robottini, che partono entrambi dal quadrato (1,1) e terminano in uno stesso quadrato.
Il primo percorso comincia con un numero positivo, il secondo con un numero negativo 
e il quadrato iniziale e quello finale sono gli unici quadrati che i due percorsi hanno in comune.
Vogliamo sapere quanti dei quadrati dell'insieme I ricadono nella zona circoscritta dai due percorsi. 
Nota che un quadrato (x,y) e' nella zona circoscritta se i due robottini  
attraversano la colonna x della griglia e i quadrati di quella colonna attraversati
dai due robottini  sono rispettivamente (x,y1) ed (x,y2) con y1>y>y2).
(quindi i quadrati di I che si trovano sui percorsi NON vanno contati)

Ad esempio per per l'insieme 
    I={ (11, 2), (8,5), (4,6), (7,1), (2,9), (3,4), (7,6), (6,6), (5,2)}
e i due percorsi: 
    p1 =  5 -2 -2 2 -4
    p2 = -3  2 -5 5
Ovvero (indicando con '+' i movimenti con A positivo, con '-' quelli con A negativo, 
        con '*' i quadrati di I, con 'o' l'origine e con 'X' la destinazione)
    y
    ^
  11|
  10|
   9| *
   8|    +---X
   7|    +   +
   6|+--*-** +
   5|+      *+
   4|+ *     +
   3|+  +-----
   2|+  +*     *
   1|o---  *
    |_______________________>x
              11111111112
     12345678901234567890

la risposta e' 4 perche' gli unici quadrati che ricadono nella zona circoscritta sono
{(3, 4), (6, 6), (7, 6), (8, 5)}

Scrivere una funzione es3(fmappa) che prende in input  il percorso del file di testo contenente 
i percorsi dei due robottini e l'insieme dei quadrati I e restituisce il numero di quadrati 
dell'insieme I che risultano circoscritti dai due percorsi.

I dati sono organizzati  nel file come segue:
- una serie di righe vuote
- il percorso del primo robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- il percorso del secondo  robottino ( ciascuno spostamento del percorso
  separato dal successivo da spazi e il tutto in una o piu' righe consecutive) 
- una serie di righe vuote 
- una sequenza di coppie (x,y) che indicano i quadrati dell'insieme (le coppie separate 
 da virgole e spazi ed in una o piu' righe consecutive)
- una serie di righe vuote

Si veda ad esempio il file mp1.txt

NOTA: il timeout previsto per questo esercizio Ã¨ di 1 secondo per ciascun test.

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
(ad esempio editatelo dentro Spyder)'''
        

def es3(fmappa):
    p1, p2, i = letturaFile(fmappa)
    p1, dizp1 = percorso(p1)
    p2, dizp2 = percorso(p2)
    
    i = i - (p1 | p2)
    i = set(filter(lambda tupla: tupla[0] in dizp1.keys() and tupla[0] in dizp2.keys(), i))
    quadretti = set()
    for t in i:
        y1 = dizp1[t[0]]
        y2 = dizp2[t[0]]
        
        if(y2<t[1]<y1):
            quadretti.add(t)
    return len(quadretti)
def stringAPercorso(p):
    return list(map(lambda elemento: int(elemento), p.split()))
    
def letturaFile(fmappa):
    righe = []
    with open(fmappa, encoding = 'utf-8') as f:
        righe = f.readlines()
    indice = 0
    p1 = []
    p2 = []
    i = set()
    while '\n' == righe[indice]:
        indice += 1
    while '\n' != righe[indice]:
        p1 += stringAPercorso(righe[indice])
        indice += 1
    while '\n' == righe[indice]:
        indice += 1
    while '\n' != righe[indice]:
        p2 += stringAPercorso(righe[indice])
        indice += 1
    while '\n' == righe[indice]:
        indice += 1
    while '\n' != righe[indice]:
        tmp = righe[indice].replace('(',' ').replace(')', ' ').replace(',', ' ').split()

        for j in range(0, len(tmp)-1, 2):
            i.add((int(tmp[j]),int(tmp[j+1])))
        indice += 1
    return p1, p2, i


def percorso(percorso):
    p = [(1,1)]
    diz = {1:1}
    for el in percorso:
        if el >= 0:
            y = p[-1][1] + el
            for coordinataY in range(p[-1][1] +1, y+1):
                p.append((p[-1][0], coordinataY))
                tmpX, tmpY = p[-1]
                if tmpX in diz:
                    diz[tmpX] = max(tmpY, diz[tmpX])
                else:
                    diz[tmpX] = tmpY
        else:
            x = p[-1][0] + abs(el)
            for coordinataX in range(p[-1][0] +1, x+1):
                p.append((coordinataX, p[-1][1]))
                tmpX, tmpY = p[-1]
                if tmpX in diz:
                    diz[tmpX] = max(tmpY, diz[tmpX])
                else:
                    diz[tmpX] = tmpY
        
    return set(p), diz


























        