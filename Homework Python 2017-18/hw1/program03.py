
'''Dato un testo da codificare ed una chiave si propone il seguente schema crittografico:

- dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. 
- di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le occorrenze 
  tranne l'ultima, ottenendo una sequenza DISORDINATA. 
- i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri del testo 
  ad essere codificati ovvero sostituiti nel testo crittografato (gli altri resteranno invariati). 
- la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in corrispondenza 
  con la sequenza DISORDINATA dei caratteri ottenuti al passo precedente.

Come esempio di applicazione  consideriamo la chiave
 "sim sala Bim!"
a seguito delle eliminazioni la chiave produce la sequenza DISORDINATA
 "slaim"
 
I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed 'm'. 
Per sapere con cosa verranno codificati questi caratteri si considera la seguente corrispondenza
tra sequenze:
    "ailms" (sequenza ordinata degli stessi caratteri)
    "slaim" (sequenza disordinata ottenuta dalla chiave)
questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.

Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di sale" si 
 otterra' il seguente testo crittografato:
    "il mare sa di sale"   (testo in chiaro)
    "la isre ms dl msae"   (testo crittografato)

La decodifica del testo crittografato opera sulla stessa chive ma sostituisce le lettere
presenti nella sequenza disordinata con quelle della sequenza ordinata.
Quindi nell'esempio precedente le sostituzioni sono invertite:
 (s, a), (l, i) (a, l), (i, m) ed (m, s)

Per altri esempi vedere il file grade03.txt

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def codifica(chiave, testo):
    """funzione che passato un testo e una chiave, codifica il primo"""
    coppiaChiave = creaCoppieChiave(chiave) #creo le coppie per la codifica
    newText = []    #preparo una lista con il testo nuovo, lista non stringa perche e' mutabile ed e' piu veloce da modficare
    for x in testo: #per ogni carattere del testo
        if x in coppiaChiave:   #se il carattere e' nel testo
            newText.append(coppiaChiave[x]) #lo sostituisco e inserisco nella lista con il caratt. corrispondente
        else:   #altrimenti
            newText.append(x)   #lo inserisco semplicemente nella lista
    return "".join(newText) #finito il for ritorno la lista in stringa con join


def decodifica(chiave, testo):  #funzione analoga alla codifica
    """funzione che passato un testo criptato e la chiave fa una decodifica"""
    coppiaChiave = creaCoppieChiave(chiave,False)
    textCoded = []
    for x in testo:
        if x in coppiaChiave:
            textCoded.append(coppiaChiave[x])
        else:
            textCoded.append(x)
    return "".join(textCoded)

def getSequenzaDisordinata(chiave):
    """funzione che data una chiave ti restituisce la sequenza disordinata"""
    chiaveDisordinata = []  #mi creo una lista dove andra la chiave disord.
    for i in range(len(chiave)-1,-1,-1):    #scorro al contrario la stringa
        if chiave[i] in chiaveDisordinata:    #se il carattere che trova a destra e' gia nella lista passa alla i successiva
            continue
        if not 'a'<= chiave[i] <= 'z':  #se il carattere non e' compreso tra 'a' e 'z' minuscole passa alla i successiva
            continue
        chiaveDisordinata.append(chiave[i]) #se non entra in nessuno dei due if vuol dire che quel carattere non l'ha mai preso
    return list(reversed(chiaveDisordinata))    #ritorna la lista al contrario

def getSequenzaOrdinata(chiave):    #funzione analoga a quella disordinata
    """funzione che data una chiave ti restituisce la sequenza ordinata"""
    chiaveOrdinata = []
    for i in range(len(chiave) - 1, -1, -1):
        if chiave[i] in chiaveOrdinata:
            continue
        if not 'a' <= chiave[i] <= 'z':
            continue
        chiaveOrdinata.append(chiave[i])
    chiaveOrdinata.sort()
    return chiaveOrdinata

def creaCoppieChiave(chiave,codifica=True):
    """funzione che crea le coppie tra chiave disord e ordinata in base all'operazione(che si passa tramite il par. codifica)"""
    dizCoppie = {}  #creo un dizionario
    seqOrd = getSequenzaOrdinata(chiave)    #creo una lista con la seq ordinata
    seqDis = getSequenzaDisordinata(chiave) #creo una lista con la seq disordinata
    lenSeq = len(seqOrd)    #mi salvo la lunghezza di una delle due sequenze(hanno stessa lunghezza)
    for x in range(lenSeq):
        if codifica:    #se bisogna codificare
            dizCoppie[seqOrd[x]] = seqDis[x]    #avro un diz con chiave la seq ord. e attr. la seq disord.
        else:   #se bisogna decodificare
            dizCoppie[seqDis[x]] = seqOrd[x]    #avro un diz con chiave la seq dis. e attr. la seq ord.
    return dizCoppie    #ritorno il dizionario

