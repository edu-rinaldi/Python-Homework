'''
Si definiscono divisori propri di un numero tutti i suoi divisori tranne l'uno e il numero stesso.
Scrivere una funzione modi(ls,k) che, presa una lista ls di interi  ed un intero
non negativo k:
    1) cancella  dalla lista ls gli interi che non hanno esattamente k divisori propri
    2) restituisce una seconda lista che contiene i soli numeri primi di ls.
NOTA: un numero maggiore di 1 e' primo se ha 0 divisori propri.

ad esempio per ls = [121, 4, 37, 441, 7, 16]
modi(ls,3) restituisce la lista con i numeri primi [37,7] mentre al termine della funzione si avra' che la lista ls=[441,16]

Per altri  esempi vedere il file grade.txt

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def modi(ls,k):
    numPrimi = list(filter(lambda x: primo(x), ls))     #creo una lista con tutti i numeri primi presenti in ls sfruttando la funzione primo()
    for x in reversed(range(len(ls))):      #scorro la lista al contrario così da evitare problemi con l'indice durante l'eliminazione degli elementi
        if nDiv(ls[x])!= k:     #se i divisori propri del numero sono diversi da k, allora vengono eliminati
            ls.remove(ls[x])
    return numPrimi


def primo(num):
    """funzione che dato un numero ti dice se è primo(true) o no(false)"""
    if num==2: return True #se il numero e' due gia e' primo
    if num%2==0: return False #se è pari di sicuro non e' primo
    for div in range(3,int(num**0.5)+1,2):  #controlla per ogni i dispari fino alla radice se e' divisibile
        if num%div==0: return False #se trova un divisore ritorna false
    return True #altrimenti e' primo


# def potenzeFattoriPrimi(num):
#     """funzione che restituisce una lista con le potenze dei vari fattori"""
#     lst, exp = [],[]    #mi creo due liste, una per inserire i fattori primi, una dove calcolerò gli esponenti
#     while num>=2:   #fino a quando il numero non diventa 1
#         if primo(num):  #se il numero d'origine o dopo le divisioni e' primo lo metto nella lista
#             lst.append(num)
#             break   #esco dal ciclo e vado a fare direttamente gli esponenti poiche' non c'e' piu nulla per cui dividere
#         for i in range (2+num%2,num,2): #la i assumera' valori o solo valori pari o solo dispari in base a num cosi da dimezzare le divisioni
#             if num%i==0:    #se e' divisibile per i
#                 num = int(num / i) #fa la divisione e l'append di i e trasforma in int se no avremmo es "5454.0" come risultato
#                 lst.append(i)
#                 break   #esce dal for e rivede ogni condizione fino a quando non diventa primo
#     setFattori = set(lst)   #trasformo la lista in un insieme poiche' prendo un numero una sola volta e lo conto una sola volta nella lista
#     for x in setFattori:
#         count = lst.count(x)
#         exp.append(count)   #faccio l'append del numero che corrispondera' all'esponente
#     return exp


def fattoriPrimi(num,ls=[]):
    if primo(num):  #se il numero d'origine o dopo le divisioni e' primo lo metto nella lista
        ls.append(num)
        return ls   #ed esco dalla funzione poiche non c'e piu nulla per cui dividere
    for x in range(2+num%2,num,2):  #la i assumera' valori o solo valori pari o solo dispari in base a num cosi da dimezzare le divisioni
        if num%x==0:    #se e divisibile per x
            ls.append(x)    #aggiungo x alla lista dei fattori
            num //= x   #divido così da scalare num
            break   #esco dal ciclo
    fattoriPrimi(num,ls)    #faccio la ricorsione della funzione fino a quando num non diventa primo
    return ls


def potenzeFattoriPrimi(num):
    lst, exp = [],[]
    lst = fattoriPrimi(num, lst)    #creo una lista con tutti i fattori primi
    setFattori = set(lst)  # trasformo la lista in un insieme poiche' prendo un numero una sola volta e lo conto una sola volta nella lista
    for x in setFattori:
        count = lst.count(x)    #conto quante volte x compare nella lista dei fattori
        exp.append(count)  # faccio l'append del numero che corrispondera' all'esponente
    return exp



def nDiv(n):
    """funzione che restituisce il numero di divisori propri"""

    if (primo(n)): return 0     #se è primo avrà sempre 0 divisori propri, perchè gli unici divisori sono 1 e se stesso
    lst = potenzeFattoriPrimi(n) #mi creo una lista con tutte le potente dei fattori primi di n

    mul = 1     #variabile da usare per il calcolo del num di divisori , per la moltiplicazione il numero neutro è 1 e inizializzo con questa

    for potenze in lst:     #prendo tutte le potenze conservate
        pot = potenze+1     #e applico la formula (a+1)(b+1)(c+1)etc
        mul = mul*pot       #dove a,b,c sono i vari esponenti salvati
    return mul-2    #tolgo due, così da escludere 1 e se stesso dal calcolo così da avere i divisori propri


