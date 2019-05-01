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
            ls.pop(x)
    return numPrimi


def primo(num):
    """funzione che dato un numero ti dice se è primo(true) o no(false)"""
    for div in range(2,(int(num**0.5))+1):
        if num%div==0: return False     #se è divisibile per almeno un numero che va da 2 a NUM allora non è primo
    return True     #altrimenti lo è


def nDiv(n):
    """funzione che restituisce il numero di divisori propri"""

    if (primo(n)): return 0     #se è primo avrà sempre 0 divisori propri, perchè gli unici divisori sono 1 e se stesso

    lst = potenzeFattoriPrimi(n)

    mul = 1     #variabile da usare per il calcolo del num di divisori , per la moltiplicazione il numero neutro è 1 e inizializzo con questa

    for potenze in lst:     #prendo tutte le potenze conservate
        pot = potenze+1     #e applico la formula (a+1)(b+1)(c+1)etc
        mul = mul*pot       #dove a,b,c sono i vari esponenti salvati

    return mul-2    #tolgo due, così da escludere n e se stesso dal calcolo così da avere i divisori propri

def potenzeFattoriPrimi(num):
    """funzione che restituisce una lista con le potenze dei vari fattori"""

    lst= []
    for x in range(2, num):         # faccio la scomposizione
        if primo(x) and num%x==0:   # in fattori primi dividendo per
            exp_count = 0           # i numeri primi che sono divisori di n
            while num%x==0:
                exp_count+=1
                num = num/x
            lst.append(exp_count)   #salvo in una lista il numero e la sua potenza
            if(num==1): break
        continue
    return lst