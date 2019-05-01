'''
Un documento HTML può essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero può essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondità
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS è una successione di selettori di tag separati da spazio che serve ad individuare uno o più nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        è il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS è una versione ridottissima che non segue lo standard completo.
In particolare, non è possibile usare più relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)
    elimina_nodi(       fileIn, selettore, fileOut)
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verrà utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse

from copy import copy

def cssSelector(selector, node):
    if selector[0] == '#' and 'id' in node.attr and node.attr['id'] == selector[1:]: return True
    if selector[0] =='.' and 'class' in node.attr and selector[1:] in node.attr['class']: return True
    if selector[0:2] == '@[':
        selector = selector.replace('@[','').replace(']','').replace('"','').split('=')
        if selector[0] in node.attr and node.attr[selector[0]] == selector[1]: return True
    if node.tag == selector: return True
    return False


def countNodes(node, selettore, count, inside=False):
    if node.istext(): return 0  #se il nodo è testo non contarlo
    checkA = cssSelector(selettore[0], node) #verifica la correttezza del nodo
    count=0

    if checkA and not inside:
        del selettore[0]
        if len(selettore)==0:
            return 1
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
    elif not checkA and inside: return 0
    elif checkA and inside:
        inside=False
        del selettore[0]
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
        if len(selettore) == 0:
            return 1
    for el in node.content:
        count += countNodes(el, copy(selettore), count, inside)
    return count


def conta_nodi(fileIn, selettore):
    '''Torna il numero di nodi dell'albero, che soddisfano il selettore CSS.'''
    page = fparse(fileIn)
    count=0
    selettore = selettore.split(' ')
    return countNodes(page, selettore, count)


def delNodes(node, selettore, inside=False):
    if node.istext(): return False  #se il nodo è testo non contarlo
    checkA = cssSelector(selettore[0], node) #verifica la correttezza del nodo

    if checkA and not inside:
        del selettore[0]
        if len(selettore)==0:
            return True
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
    elif not checkA and inside: return False
    elif checkA and inside:
        inside=False
        del selettore[0]
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
        if len(selettore) == 0:
            return True
    for el in node.content:
        if delNodes(el, copy(selettore), inside)==True:
            node.content.remove(el)
    return node




def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    page = fparse(fileIn)
    selettore = selettore.split(' ')
    html = delNodes(page, selettore)
    with open(fileOut, 'wb') as f:
        f.write((html.to_string()).encode('utf8'))



def changeNode(node, selettore, chiave, valore, inside=False):
    if node.istext(): return node
    checkA = cssSelector(selettore[0], node) #verifica la correttezza del nodo

    if checkA and not inside:
        del selettore[0]
        if len(selettore)==0:
            node.attr[chiave] = valore
            return node
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
    elif not checkA and inside: return node
    elif checkA and inside:
        inside=False
        del selettore[0]
        if len(selettore) and selettore[0] == '>':
            inside=True
            del selettore[0]
        if len(selettore) == 0:
            node.attr[chiave] = valore
            return node
    for el in node.content:
        changeNode(el, copy(selettore), chiave,valore, inside)

    return node




def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    page = fparse(fileIn)
    selettore = selettore.split(' ')
    html = ''
    html = changeNode(page, selettore, chiave, valore)
    with open(fileOut, 'wb') as f:
        f.write((html.to_string()).encode('utf8'))









# def countNodes(node,selector, count):
#     if not node.istext():
#         check = cssSelector(selector,node)
#         if check: count+=1
#         for el in node.content:
#             count = countNodes(el,selector,count)
#
#     return count
#
# def countNodesInParent(node, pSel,cSel,count):
#     if not node.istext():
#         # print(node.tag)
#         checkP = cssSelector(pSel,node)
#         if not checkP:
#             for el in node.content:
#                 count = countNodesInParent(el,pSel,cSel,count)
#         if checkP:
#             for el in node.content:
#                 if not el.istext():
#                     count = countNodesInParent(el,pSel,cSel,count)
#                     checkC = cssSelector(cSel,el)
#                     if checkC: count+=1
#     return count
#
#
# def countDescendent(node, aSel,dSel,count):
#     if not node.istext():
#         # print(node.tag,count)
#         checkA = cssSelector(aSel,node)
#         if not checkA:
#             for el in node.content:
#                 if not el.istext():
#                     count = countDescendent(el,aSel,dSel,count)
#         if checkA:
#             if not node.istext():
#                 # print(node.tag,'aa')
#                 count = countNodes(node, dSel,count)
#                 # print(count)
#     return count












# def delNodes(node,selector):
#     if not node.istext():
#         check = cssSelector(selector,node)
#         if check: return True
#         for el in node.content:
#             if delNodes(el,selector) == True:
#                 node.content.remove(el)
#
#     return node
#
# def delNodesInParent(node, pSel,cSel):
#     if not node.istext():
#         checkP = cssSelector(pSel,node)
#         if not checkP:
#             for el in node.content:
#                 print(el.tag)
#                 delNodesInParent(el,pSel,cSel)
#         if checkP:
#             for el in node.content:
#                 if not el.istext():
#                     checkC = cssSelector(cSel,el)
#                     if checkC: node.content.remove(el)
#     return node
#
#
# def delDescendent(node, aSel,dSel):
#     if not node.istext():
#         # print(node.tag,count)
#         checkA = cssSelector(aSel,node)
#         if not checkA:
#             for el in node.content:
#                 if not el.istext():
#                     delDescendent(el, aSel, dSel)
#         if checkA:
#             if not node.istext():
#                 # print(node.tag,'aa')
#                 delNodes(node, dSel)
#                 # print(count)
#     return node




# def changeNode(node,selector, key, value):
#     if not node.istext():
#         check = cssSelector(selector,node)
#         if check: node.attr[key] = value
#         for el in node.content:
#             changeNode(el,selector,key,value)
#     return node
#
# def changeNodesInParent(node, pSel,cSel,key,value):
#     if not node.istext():
#         # print(node.tag)
#         checkP = cssSelector(pSel,node)
#         if not checkP:
#             for el in node.content:
#                 count = countNodesInParent(el,pSel,cSel,count)
#         if checkP:
#             for el in node.content:
#                 if not el.istext():
#                     count = countNodesInParent(el,pSel,cSel,count)
#                     checkC = cssSelector(cSel,el)
#                     if checkC: count+=1
#     return count
#
#
# def changeDescendent(node, aSel,dSel,key,value):
#     if not node.istext():
#         # print(node.tag,count)
#         checkA = cssSelector(aSel,node)
#         if not checkA:
#             for el in node.content:
#                 if not el.istext():
#                     changeDescendent(el,aSel,dSel,key,value)
#         if checkA:
#             if not node.istext():
#                 # print(node.tag,'aa')
#                 changeNode(node, dSel,key,value)
#                 # print(count)
#     return node