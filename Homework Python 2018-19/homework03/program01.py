'''
Abbiamo una immagine  .PNG . 
L'immagine presenta, su uno sfondo nero ( vale a dire di colore (0,0,0)), 
segmenti di colore bianco (vale a dire (255,255,255)) orizzontali e verticali di diversa lunghezza. 
Si veda ad esempio il file f1.png.
I segmenti, in alcuni casi, nell'incrociarsi creano rettangoli. 
Siamo interessati a trovare quei rettangoli di altezza e larghezza almeno 3 
(compreso il bordo, quindi con la parte nera alta e larga almeno 1 pixel)
e che, tranne il bordo completamente bianco, presentano tutti i pixel al loro interno di colore nero. 
A questo scopo vogliamo creare una nuova immagine identica alla prima se non per il 
fatto che questi rettangoli vengono evidenziati. 
Il bordo di questi rettangoli deve essere di colore verde (vale a dire (0,255,0)) e 
i pixel interni devono essere di colore rosso (vale a dire (255,0,0)).
Ad esempio l'immagine che vogliamo ricavare da quella nel file  f1.png e' 
nel file Risf1.png.

Scrivere una funzione es1(fimg,fimg1) che, presi in input gli indirizzi  di due file .PNG, 
legge dal primo l'immagine del tipo descritto sopra e salva nel secondo l'immagine 
con i rettangoli evidenziati. 
La funzione deve infine restituire  il numero di rettangoli che risultano evidenziati.

Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

ATTENZIONE: non sono permesse altre librerie.
'''

import immagini


def inside(img, x, y):
    return 0 <= x < len(img[0]) and 0 <= y < len(img)
def isrettangolo(img, sx, sy, w, h):
    for y in range(sy, sy+h+1):
        for x in range(sx, sx+w+1):
            if ((y == sy or y == sy+h) or (x == sx or x == sx+w)) and img[y][x] != (255, 255, 255):
                return False
            if (not ((y == sy or y == sy+h) or (x == sx or x == sx+w))) and img[y][x] == (255, 255, 255):
                return False
    return True
 
def coloraRettangolo(img, sx, sy, w, h, coloreBordo, coloreInterno):
    for y in range(sy, sy+h+1):
        for x in range(sx, sx+w+1):
            if ((y == sy or y == sy+h) or (x == sx or x == sx+w)):
                img[y][x] = coloreBordo
            else:
                img[y][x] = coloreInterno
    return img
def es1(fimg, fimg1):
    '''scova in fimg i rettangoli da evidenziale, crea una copia dell'immagine 
    in cui questi rettangoli risultano evidenziati (vale a dire hanno bordo  verde e
    interno  rosso) salva l'immagine in fimg1 e restituisce il numero di rettangoli
    evidenziati. '''
    # inserite qui il vostro codice
    NERO = (0, 0, 0)
    BIANCO = (255, 255, 255)
    ROSSO = (255, 0, 0)
    VERDE = (0, 255, 0)
    aS = set()
    aD = set()
    bD = set()
    bS = set()
    img = immagini.load(fimg)
    for y in range(len(img)):
        for x in range(len(img[0])):
            if inside(img, x+1, y) and img[y][x+1] == BIANCO and inside(img, x, y+1) and img[y+1][x] == BIANCO \
            and inside(img, x+1, y+1) and img[y+1][x+1] == NERO:
                aS.add((x, y))
                
            if inside(img, x-1, y) and img[y][x-1] == BIANCO and inside(img, x, y+1) and img[y+1][x] == BIANCO \
            and inside(img, x-1, y+1) and img[y+1][x-1] == NERO:
                aD.add((x, y))
                
            if inside(img, x-1, y) and img[y][x-1] == BIANCO and inside(img, x, y-1) and img[y-1][x] == BIANCO \
            and inside(img, x-1, y-1) and img[y-1][x-1] == NERO:
                bD.add((x, y))
                
            if inside(img, x+1, y) and img[y][x+1] == BIANCO and inside(img, x, y-1) and img[y-1][x] == BIANCO \
            and inside(img, x+1, y-1) and img[y-1][x+1] == NERO:
                bS.add((x, y))
            
    rettangoli = []
    for angoloAS in aS:
        adfiltrati = set(filter(lambda c: c[1] == angoloAS[1] and c[0]>angoloAS[0] , aD))
        if len(adfiltrati)>0:    
            angoloAD = min(adfiltrati)
        else:
            continue
        bsfiltrati = set(filter(lambda c: c[0] == angoloAS[0] and c[1]>angoloAS[1], bS))
        if len(bsfiltrati)>0:
            angoloBS = min(bsfiltrati)
        else:
            continue
        angoloBD = (angoloAD[0], angoloBS[1])
        w = angoloAD[0]-angoloAS[0]
        h = angoloBS[1]- angoloAS[1]
        if angoloBD in bD and isrettangolo(img, angoloAS[0], angoloAS[1], w, h):
            rettangoli.append([angoloAS[0], angoloAS[1], w, h])
    for r in rettangoli:
        img = coloraRettangolo(img, r[0],r[1], r[2], r[3], VERDE, ROSSO)
    immagini.save(img, fimg1)
    return len(rettangoli)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

