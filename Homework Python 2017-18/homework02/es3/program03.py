'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa di almeno 1 carattere, composta solo da cifre (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''

def decod(pfile, codice):
    '''funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data'''
    originalWord= []    #lista di parole
    compWord = set()    #insieme finale da restituire
    lenCode_Word = len(codice)  #lunghezza del codice
    with open(pfile,encoding='utf8') as f:
        for line in f:  #per ogni linea nel file
            if len(line)-1 == lenCode_Word: #se la parola -1 (per via del \n) è uguale alla lunghezza del codice
                originalWord.append(line.strip('\n'))   #faccio append e strip su \n
    for word in originalWord:  #per ogni parola
        if checkComp(word,codice): #se è compatibile
            compWord.add(word)  #aggiungi all'insieme
    return compWord #fai return dell'insieme




def checkComp(word,code):
    dizCodeToWord = {}  #dizionario della forma {codice: parola}
    dizWordToCode = {}  #dizionario della forma {parola: codice}

    for i in range(len(code)):
        if word[i] in dizWordToCode and dizWordToCode[word[i]] != code[i]:  #se il chr e' presente come chiave del diz,e se il suo attributo e' diverso dal codice in pos i
            return False    #ritorni falso
        if code[i] in dizCodeToWord and dizCodeToWord[code[i]] != word[i]:  #se il char del codice e' presente come chiave del diz, e se il suo attributo e' diverso dal carattere in pos i
            return False    #ritorni falso
        dizWordToCode[word[i]], dizCodeToWord[code[i]] = code[i], word[i]   #altrimenti se non sono presenti metti attributi per quelle chiavi nei due diz
    stringa_cod = ''    #inizializzo stringa vuota
    for x in word:  #per ogni carattere della parola
        stringa_cod+= dizWordToCode[x]  #append del carattere del codice
    return stringa_cod == code  #return true o false in base alla compatibilità codice parola

### funzione inutile al momento ###
# def pickOneFromWord(word):
#     newWord = ''
#     for c in word:
#         if c not in newWord:
#             newWord+= c
#     return newWord

