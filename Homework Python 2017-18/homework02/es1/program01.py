'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il prossimo post 
o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).

L'insieme restituito (risultato) dovra' contenere gli identificativi (ID) dei post 
che contengono almeno una parola dell'inseme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

import re

def post(fposts,insieme):
    risultato = set()   #inizializzo l'insieme che restituiro' alla fine

    insieme = allLower(insieme) #ogni elemento dell'insieme parametro avra' caratteri minuscoli

    with open(fposts, 'r', encoding='utf-8') as f:
        fileText = f.read().lower() #apro il file, lo leggo, rendo ogni carattere minuscolo

    fileText = delNotAlpha(fileText)    #cancello ogni carattere != a-z , A-Z, 0-9 e caratteri utili come '< > \n' facendo un replace con lo spazio

    postList = fileText.split('<post>') #splitto il testo per ogni post

    dizPostID =  createIDPOSTSDict(postList)    #mi creo un dizionario del tipo { id : {insieme parole del post}}

    for x in dizPostID:
        if dizPostID[x].intersection(insieme):  #se l'intersezione avviene, aggiungo l'id all'insieme risultato
            risultato.add(str(x))

    return risultato


def delNotAlpha(txt):
    """funzione che passato un testo ogni carattere != a-z , A-Z, 0-9 e caratteri utili come '< > \n'"""
    # for c in range(len(txt)):
    #     if not (txt[c].isalnum() or txt[c] in ['<','>','\n']):
    #        txt = txt.replace(txt[c],' ')
    return re.sub(r'[^a-zA-Z0-9<>\n]', ' ',txt) #con regex ( regular expression) velocizzo il processo di replace


def getPostID(post):
    """funzione che ritorna l'id di un post"""
    id=''   #inizializzo la variabile id

    for x in post:  #scorro il post
        if x.isdigit(): #se x e' un numero
            id+= x  #faccio l'append
        elif id != '':  #se id non e' vuoto e x.digit() == false allora
            break   #interrompo il ciclo
    try:
        return int(id)
    except:
        return None


def createIDPOSTSDict(post):
    """funzione che ritorna un dizionario della forma {id: {lista parole post}}"""
    diz = {}    #inizializzo un dizionario vuoto
    for x in post:  #per ogni post
        diz[getPostID(x)] = set(x.split())  #uso come chiave l'id del post, e assegno un insieme delle parole del post
    return diz

def allLower(ins):
    """funzione che passato un insieme ritorna lo stesso con tutte le lettere minuscole"""
    finalIns = set()
    for x in ins:
        finalIns.add(x.lower())
    return finalIns


