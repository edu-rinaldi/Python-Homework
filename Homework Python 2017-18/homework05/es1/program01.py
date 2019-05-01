'''
Obiettivo dell'esercizio e' sviluppare la strategia di gioco per il gioco del Mastermind. 

Nel gioco del Mastermind un  giocatore (il "decodificatore"), deve indovinare un  codice segreto.
Il codice segreto e' di N cifre decimali distinte (NO RIPETIZIONI, solo 10 possibili simboli per ciascuna posizione).
Il decodificatore cerca di indovinare il codice per tentativi. Strategicamente  nel tentativo 
possono essere presenti anche cifre ripetute pur  sapendo che nel codice non sono presenti ripetizioni. 
In risposta ad  ogni tentativo viene fornito un aiuto producendo una coppia di interi (a,b) dove:

- a e' il numero di cifre giuste al posto giusto,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo al posto giusto.
- b e' il numero di cifre  giuste ma al posto sbagliato,
cioe' le cifre del codice da indovinare che sono effettivamente presenti nel tentativo solo al posto sbagliato.

Ad esempio per il codice
    34670915 e il tentativo
    93375948
la risposta deve essere la coppia (2,3).
Il 2 viene fuori dal contributo delle cifre 7 e 9 del codice da indovinare in quarta e sesta posizione,
il numero 2 e' dovuto alle cifre 3,4,5 che compaiono tra le cifre del tentativo ma mai al posto giusto.

Nella nostra versione di Mastermind il valore di N (lunghezza del codice) puo' essere 6, 7 o 8 e nella coppia data
in  risposta ai tentativi non si vuole rivelare quale delle due due cifre rappresenta il numero di  cifre giuste al posto giusto 
di conseguenza nella coppia di risposta  i valori di a e b possono risultare invertiti.
Ad esempio per il codice 34670915 e il tentativo 93375948 le risposte (2,3) e (3,2) sono entrambe possibili.


Una configurazione del  gioco viene rappresentata come lista di liste (L). 
Il primo elemento di L e' un intero N rappresentante la lunghezza del codice.
Ciascuno degli eventuali altri elementi di L rappresenta un tentativo fin qui
effettuato dal decodificatore e la relativa risposta.
Piu' precisamente  L[i] con i>0, se presente, conterra' una tupla composta da due elementi:
- la lista di N cifre  con il tentativo effettuato dal decodificatore in un qualche passo precedente
- la tupla di interi (a,b) ricevuta in risposta.


Il programma che dovete realizzare contiene la seguente funzione:
 
    decodificatore(configurazione)

che e' l'AI che guida il gioco. La funzione  riceve come input la configurazione attuale del gioco e produce un tentativo (lista di caratteri in '0-9').

Per questo esercizio la valutazione avverra' nel seguente modo: 
avete 150 tentativi e 30 secondi di tempo per indovinare quanti piu' codici possibile.
Il punteggio ottenuto e' dato dal numero di codici che riuscite ad indovinare.

Tutti i vostri elaborati al termine verranno valutati su di uno stesso set di codici,
questa operazione  determinera' una classifica dei vostri elaborati.
Per entrare in classifica bisogna indovinare almeno cinque codici.
La classifica viene suddivisa in 14 fasce che corrispondono ai voti da 18 a 31 ed a 
ciascun programma viene assegnato il voto corrispondente.
Se il numero di valori diversi e' minore di 14 il voto sara' proporzionale alla posizione
nella graduatoria (con il primo che prende 31 e l'ultimo 18)

In allegato vi viene fornito un  simulatore di gioco (simulatore1.py) che vi permettera' di 
autovalutare la vostra strategia. Il simulatore genera  codici casuali e invoca il vostro 
programma per ottenere i vari tentativi. Appena un codice  viene indovinato ne viene 
proposto uno nuovo. Il processo termina quando avete esaurito i vostri 150 tentativi
o sono passati  i 30 secondi.

ATTENZIONE: NON usate lettere accentate ne' nel codice ne' nei commenti
'''

import random 
import itertools


def risposta(codice, proposta):
    ''' restituisce per ogni proposta quanti indovinati al posto giusto (a) e quanti al posto sbagliato (b)'''
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b


def convStringToInt(combinations):
    lists = []
    for l in combinations:
        c = []
        for n in l:
            c.append(int(n))
        lists.append(c)
    return lists


# def genCode(lenC,configurazione):
#
#     if len(configurazione)==1:
#         combinations = list(itertools.combinations('0123456789', lenC))
#         global cmb
#         cmb = convStringToInt(combinations)
#         return cmb[0], False, None
#     else:
#         lastTried = configurazione[-1][0]
#         lastRes = configurazione[-1][1]
#         for el in cmb:
#             resp = risposta(lastTried,el)
#             if not (resp[0]+resp[1] == lastRes[0]+lastRes[1]):
#                 cmb.remove(el)
#         if len(cmb) == 1:
#             global disordedCode
#             disordedCode = cmb[0]
#             return disordedCode, True, len(configurazione)
#             # print(disordedCode)
#
#     return cmb[0], False, None
#
#
# def ordCode(lenC, configurazione, lenConf, combination):
#     if lenConf and len(configurazione) == lenConf:
#         print(lenConf)
#         permutations = list(itertools.permutations(combination, lenC))
#         global permuts
#         permuts = convStringToInt(permutations)
#         return permuts[0]
#     else:
#         lastTried = configurazione[-1][0]
#         lastRes = configurazione[-1][1]
#         for el in permuts:
#             resp = risposta(lastTried, el)
#             if not ((resp[0] == lastRes[0] and resp[1] == lastRes[1]) and (resp[0] == lastRes[1] and resp[1] == lastRes[0])):
#                 permuts.remove(el)
#         if len(permuts) == 1:
#             global ordedCode
#             ordedCode = permuts[0]
#             return ordedCode
#     return permuts[0]


class Decoder:
    def __init__(self):
        self.status = 'gen'
        self.configurazione = None
        self.lenConfigurazione = None
        self.disoderdedComb = None
        self.count = 0
    def genCode(self, lenC, configurazione):

        if len(configurazione) == 1:
            combinations = list(itertools.combinations('0123456789', lenC))
            global cmb
            cmb = convStringToInt(combinations)
            return cmb[0]
        else:
            lastTried = configurazione[-1][0]
            lastRes = configurazione[-1][1]
            for el in range(len(cmb)-1,-1,-1):
                resp = risposta(lastTried, cmb[el])
                if not (resp[0] + resp[1] == lastRes[0] + lastRes[1]):
                    del cmb[el]

        return cmb[0]

    def ordCode(self, lenC, configurazione, combination):
        if self.count == 0:
            permutations = list(itertools.permutations(combination, lenC))
            global permuts
            permuts = convStringToInt(permutations)
            self.count = 1
        lastTried = configurazione[-1][0]
        lastRes = configurazione[-1][1]
        for el in range(len(permuts)-1,-1,-1):
            resp = risposta(lastTried, permuts[el])
            if not ((resp[0] == lastRes[0] and resp[1] == lastRes[1]) or (resp[0] == lastRes[1] and resp[1] == lastRes[0])):
                # permuts.remove(el)
                # print(permuts[el], lastTried)
                del permuts[el]
        # print(permuts)
        return permuts.pop(0)


d = Decoder()


def decodificatore(configurazione):
    d.configurazione = configurazione
    d.lenConfigurazione = configurazione[0]
    if len(configurazione) == 1:
        d.status = 'gen'
        d.count = 0
    else:
        lastRes = configurazione[-1][1]
        if lastRes[0]+lastRes[1] == configurazione[0]:
            d.status = 'ord'
            d.disoderdedComb = cmb[0]
    if d.status == 'gen':
        comb = d.genCode(d.lenConfigurazione, d.configurazione)
    else:
        comb = d.ordCode(d.lenConfigurazione, d.configurazione, d.disoderdedComb)
    return comb





"""[7, ([0, 1, 2, 3, 4, 5, 6], (4, 1)),"""

















    # for _ in range(n):
    #     y=random.choice(x)
    #     risposta+=[int(y)]
    #     x=x.replace(y,'')
    # return risposta

