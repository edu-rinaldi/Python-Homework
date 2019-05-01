'''
Diciamo che un dizionario d rappresenta un albero (e lo indichiamo come dizionario-albero)
se ciascuna chiave di d e' un identificativo di un nodo dell'albero  e l'attributo della chiave e' la lista
(eventualmente vuota) degli identificativi dei  figli del nodo. Gli identificativi dei nodi
all'interno delle liste sono in ordine lessicografico crescente.



Ecco un esempio di dizionario d che rappresenta un dizionario-albero

d={
'a':['b'],
'b':['c','d'],
'c':['i'],
'd':['e','l'],
'e':['f','g','h'],
'f':[],
'g':[],
'h':[],
'i':[],
'l':[]
}

L'albero rappresentato da d e'

                             'a'
                              |
                _____________'b'____________
               |                            |
              'c'                  ________'d'_______
               |                  |                  |
              'i'         _______'e'_______         'l'
                         |        |        |
                        'f'      'g'      'h'


Implementare le seguenti funzioni:

1)
la funzione genera_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

produce   il  dizionario-albero che rappresenta   il sottoalbero  radicato
nell'identificativo x che si ottiene dal dizionario-albero d.
Il dizionario-albero ottenuto va registrato nel file fout.
Se l'identificativo x non e' tra i nodi di d allora  il dizionario-albero prodotto
deve essere vuoto.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
genera_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'f': [], 'g': [], 'h': [], 'e': ['f', 'g', 'h'], 'l': [], 'd': ['e', 'l']}



2)
la funzione cancella_sottoalbero(fnome,x,fout) che, presi:

- il nome di un file json contenente un dizionario-albero  d (fonome)
- un identificativo x
- il nome di un file json (fout)

ricava  da d il sottoalbero radicato in x e lo salva nel file fout.
Se x non e' presente tra le chiavi di  d allora  il dizionario-albero d non viene modificato.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
cancella_sottoalbero(fname,'d',fout)
il file fout conterra' il dizionario
{'a': ['b'], 'b': ['c'], 'c': ['i'], 'i':[]}


3)
la funzione dizionario_livelli(fnome, fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- il nome di un file json (fout)

costruisce il  dizionario che ha come  chiavi i livelli del dizionario-albero d. L'attributo di una
chiave di valore x e' la lista degli identificativi  dei nodi che si trovano a livello x  nell'albero rappresentato da d.
La lista è ordinata lessicograficamente ed in modo crescente.
Il dizionario cosi' costruito va registrato nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
dizionario_livelli(fname,fout)
il file fout conterra' il dizionario
{0: ['a'], 1: ['b'], 2: ['c', 'd'], 3: ['e','i','l'], 4: ['f', 'g', 'h']}

4)
la funzione dizionario_gradi_antenati(fnome,y,fout) che, presi:
- il nome di un file json contenente un dizionario-albero  d (fonome)
- un intero y
- il nome di un file json (fout)

costuisce  il dizionario che ha come chiavi gli identificativi dei nodi dell'albero
rappresentato dal dizionario-albero d, Attributo di una chiave di valore x e' il numero
di antenati di grado y che ha il nodo con identificativo x nell'albero.
Registra il dizionario costruito nel file fout.

Ad esempio se fnome contiene il dizionario-albero d allora dopo l'esecuzione di
dizionario_gradi_antenati(fnome,2,fout)
il file fout conterra' il dizionario
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'l': 2}

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate; non
importare moduli che non sono nella libreria standard.
'''




import json


                                    #genera sottoalbero


def subTree(tree,x,newTree={}):

    if tree[x]:
        newTree[x] = []
        for i in tree[x]:
            newTree[x].append(i)
            subTree(tree, i, newTree)
    if tree[x] == []:
        newTree[x] = []
    return newTree

def genera_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''

    d = json.load(open(fnome)) #mi carico il dictionary
    newTree = {}
    newTree = subTree(d,x, newTree)
    with open(fout,'w') as f:
        json.dump(newTree, f)



                                        # cancellla_sottoalbero


def delSubTree(tree, x):

    if tree[x] == []:
        tree.pop(x)
    else:
        for i in tree[x]:
            delSubTree(tree, i)
        tree.pop(x)

    return tree

def cancella_sottoalbero(fnome,x,fout):
    '''inserire qui il vostro codice'''
    d = json.load(open(fnome))  # mi carico il dictionary
    newTree = delSubTree(d, x)
    for i in newTree:
        if x in newTree[i]:
            newTree[i].remove(x)
    with open(fout, 'w') as f:
        json.dump(newTree, f)



def getRoot(tree):
    setVal = set()
    for el in tree:
        for i in tree[el]:
            setVal.add(i)
    for k in tree:
        if not k in setVal:
            return k




def genLevels(tree, newTree, index = None, counter = -1):
    if tree[index]:
        counter+= 1
        if not counter in newTree:
            newTree[counter] = []
        newTree[counter].append(index)
        for i in tree[index]:
            genLevels(tree, newTree, i, counter )
    if tree[index] == []:
        counter +=1
        if not counter in newTree:
            newTree[counter] = []
        newTree[counter].append(index)
    return newTree

def ordTree(tree):
    for i in tree:
        tree[i].sort()

def dizionario_livelli(fnome,fout):
    d = json.load(open(fnome))  # mi carico il dictionary
    root = getRoot(d)
    newTree = genLevels(d, {}, root)
    ordTree(newTree)
    with open(fout, 'w') as f:
        json.dump(newTree, f)




                            #dizionario gradi antenati

def getGrade(tree,node):
    return len(tree[node])


def parentsTree(tree, newTree, index, grade, counter=0):
    if getGrade(tree, index) == grade:
        newTree[index] = counter
        counter += 1
        for i in tree[index]:
            newTree[i] = counter
            parentsTree(tree, newTree, i, grade, counter)
    else:
        newTree[index] = counter
        for i in tree[index]:
            newTree[i] = counter
            parentsTree(tree, newTree, i, grade, counter)
    return newTree




def dizionario_gradi_antenati(fnome,y,fout):
    '''inserire qui il vostro codice'''
    d = json.load(open(fnome))
    root = getRoot(d)
    newTree = parentsTree(d, {}, root, y)
    with open(fout, 'w') as f:
        json.dump(newTree, f)