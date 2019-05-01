'''
Un  file di compiti contiene  informazioni su un insieme  di compiti da eseguire.
Esistono  due tipologie di compiti:
- compiti che possono essere eseguiti indipendentemente dagli altri.
- compiti da svolgere  solo al termine di un compito preliminare.
I compiti del primo tipo sono codificati nel file mediante una linea che contiene
in sequenza le due sottostringhe "comp" ed "N" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
Compiti del secondo tipo sono codificati nel file mediante due linee di codice.
-- la prima  linea,  contiene in sequenza le due sottostringhe "comp" ed "N" 
(senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "N" e' l'ID del compito (un numero positivo).
-- la seconda linea (immediatamente successiva nel file) contiene 
in sequenza le due sottostringhe "sub" ed "M" (senza virgolette) eventualmente inframmezzate, 
precedute e/o seguite da  spazi. "M" e' l'ID del compito preliminare.

il seguente file di compiti contiene informazioni su 4 compiti (con identificativi 1,3,7 e 9). 
I compiti con identificativi 1 e 9 possono essere svolti indipendentemente dagli altri mentre i compiti 
con identificativo 3 e 7 hanno entrambi un compito preliminare.

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

Scrivere la funzione pianifica(fcompiti,insi,fout) che prende in input:
- il percorso di un file (fcompiti) 
- un insieme  di ID di compiti da cercare (insi)
- ed il percorso di un file (fout) 
e che salva in formato JSON nel file fout un dizionario (risultato).

Il dizionario (risultato) dovra' contenere come chiavi gli identificativi (ID) dei compiti 
presenti in fcompiti e richiesti nell'insieme insi.
Associata ad ogni ID x del dizionario deve esserci una lista contenente  gli identificativi (ID) dei compiti 
che bisogna eseguire prima di poter eseguire il compito x richiesto
(ovviamente la lista di un ID di un compito che non richie un compito preliminare risultera' vuota ). 
Gli (ID) devono comparire nella lista nell'ordine di esecuzione corretto, dal primo fino a quello precedente a quello richiesto 
(ovviamente il primo ID di una lista non vuota corripondera' sempre ad un compito che non richiede un compito preliminare). 


Si puo' assumere che:
 - se l' ID di un compito che richieda un compito preliminare e' presente  in fcompiti 
    allora anche l'ID di quest'ultimo e' presente in fcompiti
 - la sequenza da associare al compito ID del dizionario esiste sempre
 - non esistono cicli (compiti che richiedono se' stessi anche indirettamente)


Ad esempio per il file di compiti  fcompiti contenente:

comp 3
 sub 9
        comp1
comp              9
    comp 7
sub3

al termine dell'esecuzione di  pianifica(fcompiti,{'7','1','5'}, 'a.json')
il file 'a.json' deve contenere il seguente dizionario
{'7':['9','3'],'1':[]}


Per altri esempi vedere il file grade02.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

import re
import json
from os.path import getsize

def pianifica(fcompiti,insi,fout):
    '''funzione che fa il dump in json'''
    b = bytearray(getsize(fcompiti))
    diz = {}
    with open(fcompiti,'rb',buffering=64000) as f:   #apro il file
        f.readinto(b)   #metto ogni byte in b
    listCompiti = b.decode(encoding='utf8').splitlines()    #decode e splitto per ogni riga cosi da avere una lista di compiti
    dizCompSubb = dizCompSub(listCompiti)   #creo un diz della forma {comp:sub}
    setID = set(map(lambda x: getHwID(x),listCompiti))  #mi creo un insieme con tutti gli ID
    insiemeID = insi.intersection(setID)    #intersezione tra tutti gli id e quelli richiesti come parametro, così da lavorare su una quantita ridotta di id

    for id in insiemeID:    #per ogni id
        diz[id] = dizCompSubList(dizCompSubb,id)    #dizionario della forma {id compito: [tutti i compiti precedenti] }


    with open(fout,'w',encoding='utf8') as f:
        json.dump(diz,f)  #dump del json

def checkNextSub(compiti,index):
    """funzione che controlla se il compito successivo e' sub o comp(true or false)"""
    try:
        return 'sub' in compiti[index+1]   #se 'sub' è presente nella riga successiva ritorna true se no falso
    except IndexError:  #se l'indice sfora stiamo all'ultima posizione da controllare
        return 'sub' in compiti[-1]    #quindi vedo direttamente a -1


def getHwID(compiti):
    """funzione che ritorna l'id del compito/sub"""
    return re.findall('\d+', compiti )[0]

def dizCompSub(compiti):
    """funzione che ritorna un dizionario con il comp e il suo sub {comp:sub}"""
    diz = {}    #inizializzo un dizionario vuoto
    for x in range(len(compiti)):   #per ogni compito
        if checkNextSub(compiti, x):    #controlla se il successivo e' sub, se lo e'
            try:
                diz[getHwID(compiti[x])] = getHwID(compiti[x+1])    #prova a mettere come chiave il comp, e come attr. il sub
            except: #se controlla sull'ultimo
                diz[getHwID(compiti[-2])] = getHwID(compiti[-1])    #prendi la pos. -2 e -1 e fai la stessa cosa di sopra
    return diz


def dizCompSubList(dizSub,id):
    lst = []    #inizializzo una lista vuota
    while id in dizSub:  #finche' l'id e' nel dizionario del tipo {comp:sub}
        id = dizSub[id] #cambia l'id del comp con quello del suo sub
        lst.insert(0,id)    #inseriscilo nella lista
    return lst






