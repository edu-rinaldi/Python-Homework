''' In determinate occasioni ci capita di dover scrivere i numeri in lettere,
ad esempio quando dobbiamo compilare un assegno.
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8.
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto,
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...),
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno,
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc...,
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000,
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    """funzione che passato un numero ti restituisce la stringa con il valore del numero scritto a lettere"""
    nMilaMilioniMiliardi = ['','mila','milioni','miliardi','mille','unmilione','unmiliardo']    #lista per xyzmila/milioni/miliardi
    terzine = dividiTerzine(n)      #creo le terzine del numero
    numero = ''     #inizializzo la stringa da restituire creando una stringa vuota
    for x in range(len(terzine)):
        if terzine[x] == 1 and x>0:     #se il numero corrisponde a 1000/1000000/1000000000
            numero = nMilaMilioniMiliardi[x+3] + numero     #metti 'mille'/'unmilione'/'unmiliardo'
        else:
            numero = creaCentinaia(terzine[x])+nMilaMilioniMiliardi[x]+numero #altrimenti metti la terzina a parole+il peso numerico(mila,milioni,miliardi)
    return numero   #ritorna la stringa


def dividiTerzine(n):
    """funzione che dato un numero restituisce una lista con il numero diviso ogni 3 es: 33458 --> ['33','458']"""
    num = str(n)[::-1]      #trasforma in stringa il numero e ne fa il reverse
    # terzine = [num[i:i+3] for i in range(0,len(num),3)]
    terzine = list(map(lambda i: num[i:i+3] ,range(0,len(num),3)))      #prende i numeri con un range di 3 ogni 3 numeri
    for x in range(len(terzine)):
        terzine[x] = int(terzine[x][::-1])      #rimette in ordine gli elementi della lista
    return terzine

def creaCentinaia(n):
    """funzione che dato un numero ti restituisce a parole il valore del numero fino a 999"""
    unita_dieci = ['uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove','dieci',
                   'undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','']
    decine = ['venti', 'trenta', 'quaranta', 'cinquanta', 'sessanta', 'settanta', 'ottanta', 'novanta', '', '']
    #mi creo due liste con decine e unita+10:19
    numText = ''    #creo una stringa vuota dove mettero il numero in formato XYZ

    nString = '0'*abs(len(str(n)) - 3)+str(n)   #converto i numeri in formato xyz aggiungendo degli 0 dove mancano

    nList = list(map(lambda x: int(x),nString))     #con una f. lambda metto in una lista i 3 numeri separatamente e li converto in int
    if(n>99):   #se il numero e' maggiore di 99
        if(nList[0] == 1): numText= 'cento' #controllo se come valore delle centinaia ha 1 se si metto cento
        else:
            numText = unita_dieci[nList[0]-1]+'cento' #altrimenti (se è 199<n<1000) metto il numero corrispondente+'cento'
        if(nList[1] == 8):  #se alle decine ha l'8 rimpiazzo cento con cent
           numText = numText.replace('cento','cent')
    if(len(nString) > 1):   #se il numero>9
        if int(nString[1:]) < 20 :  #controllo se e' inferiore a 20
            numText+= unita_dieci[int(nString[1:])-1]   #se si allora uso unita_dieci per il valore
        elif nList[2] == 1 or nList[2] == 8:    #altrimenti se e' maggiore di 20 e ha come valori alle unita 1 o 8
            numText+= decine[nList[1]-2][:-1]+unita_dieci[nList[2]-1]   #taglio l'ultimo carattere della decina
        else:
            numText += decine[nList[1] - 2]+unita_dieci[nList[2] - 1] #altrimenti scrivo decina+unita' normalmente
    return numText  #ritorna il numero XYZ a parole

