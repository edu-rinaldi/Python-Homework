'''
Abbiamo immagini in formato png ottenute inserendo su di uno sfondo monocolore rettangoli 
di vari colori i cui assi sono sempre parallei agli assi dell'immagine.

Vedi ad esempio l'immagine Img1.png

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Scrivere una  funzione quadrato(filename, C) che prende in input:
- il percorso di un file (filename) che contine un immagine in formato png della  tipologia appena descritta.
- una tupla C che rappresenta un colore in formato RGB (3 valori interi tra 0 e 255 compresi)

La funzione deve restituire nell'ordine:
- la lunghezza del lato del quadrato pieno di dimensione massima e colore C interamente visibile nell'immagine. 
- le coordinate  (x,y)  del pixel dell'immagine che corrisponde alla posizione 
all'interno dell'immagine del punto in alto a sinistra del quadrato. 

In caso ci siano più quadrati di dimensione massima, va considerato quello il cui punto 
in alto a sinistra occupa la riga minima  (e a parita' di riga la colonna minima) all'interno dell' immagine. 

Si può assumere che nell'immagine e' sempre  presente almeno un pixel del colore cercato.

Per gli esempi vedere il file grade01.txt

ATTENZIONE: Il timeout è impostato a 10*N secondi (con N numero di test del grader).
'''

from immagini import *


def righe(img) : return len(img)

def colonne(img) : return len(img[0])

def convToBit(img, color,row,column):
    return [[1 if img[y][x] == color else 0 for x in range(column)] for y in range(row)]

def countCell(img, x, y,counter,column,row,maxinum,cordinates):
    if img[y][x] != 0:
        counter[y][x] = 1 + min(counter[y][x+1],counter[y+1][x+1],counter[y+1][x]) if x < column -1 and y< row -1 else 1
    if maxinum <= counter[y][x]:
        return counter[y][x], (x,y)
    return maxinum , cordinates


def quadrato(filename, c):
    img = load(filename)
    row, column = righe(img), colonne(img)
    img = convToBit(img,c,row,column)
    grid = [[0]*column for x in range(row)]
    maxSquare, cord = 0, (0,0)
    reversedRow= reversed(range(row))

    for y in reversedRow:
        for x in reversed(list(range(column))):
            maxSquare, cord = countCell(img,x,y,grid,column,row,maxSquare,cord)
    return maxSquare,cord

