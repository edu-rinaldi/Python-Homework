
from  random import choice, randint
from time import time
from  program01 import *
#from  program01MiaSoluzione import *
import testlib

def genera_codice(n):
    x='0123456789'
    codice=[]
    for i in range(n):
        y=choice(x)
        x=x.replace(y,'')   # elimino la cifra estratta a caso da quelle usate per il resto del codice
        codice+=[int(y)]
    return codice

def risposta(codice, proposta):
    ''' restituisce per ogni proposta quanti indovinati al posto giusto (a) e quanti al posto sbagliato (b)'''
    a=0
    ins=set(codice)
    for i in range(len(codice)):
        if codice[i]==proposta[i]: a+=1
    b=len(ins & set(proposta))-a    # cifre del codice in comune con il tentativo, meno quelle azzeccate esattamente
    return a,b
       
def esecutore():
    ''' genera i codici e propone le configurazioni al decodificatore '''
    tot_tentativi=150
    tot_tempo=30
    tentativi=0
    vinte=0
    testlib.emptyLog('grade01.csv')
    start=time()
    fine=start+tot_tempo
    while tentativi<tot_tentativi and time()<fine:
        n=choice([6,7,8])
        codice=genera_codice(n)
        configurazione=[(n)]
        pvinta=False
        count=0
        while not pvinta and tentativi < tot_tentativi and time()<fine:
            tentativi+=1
            ris= decodificatore(configurazione)
            assert len(ris) == n, "Il tentativo non è di lunghezza {}.".format(n)
            a,b= risposta(codice, ris)
            coppia=a,b
            if choice([0,1]): coppia=b,a
            count+=1
            print('\n           tentativo',str(count).rjust(2),': ', ris,coppia)
            configurazione+=[(ris,coppia)]
            if a==n:
                vinte+=1 
                print('\n Partita numero:', vinte,'vinta in ', count, 'tentativi')
                pvinta=True
                testlib.log([('found', 1)],'grade01.csv')
    if time()> fine: tempo=30 
    else: tempo=round(time()-start,3)
    print('\n\n' + str(vinte).rjust(2) + ' Codici indovinati con '+  str(tentativi).rjust(3) + ' tentativi e in tempo ' + str(tempo) +'\n\n\n' )


if __name__ == '__main__':
    esecutore()
    
  
