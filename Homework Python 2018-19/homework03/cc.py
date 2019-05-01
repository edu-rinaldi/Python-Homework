'''
@author: Simone Papandrea
'''

import redbaron, json

redbaron.ipython_behavior = False

class CognitiveComplexity(object):
    
    def evaluate(self,filename):
        '''
        Calcola la Complessità Cognitiva per tutte le funzioni ed i metodi definiri nel file.
        - filename: file python da parsare
        -> torna un dizionario { 'nomeFunzione': cc, 'nomeClasse.nomeMetodo': cc }
        '''
        fns=dict()
        with open(filename) as file:
            red = redbaron.RedBaron(file.read())

            # trova tutte le funzioni e ne costruisce il nome puntato (Class.method...)
            for fn in red.find_all("def"):
                    names = []
                    p = fn
                    while p:
                        names = [p.name] + names
                        p = p.parent_find(['def','class']) # trova funzioni o classi che contengono la funzione
                    name = '.'.join(names)
                #if not fn.parent_find("DefNode"): # FIXME: necessario?
                    cc= self.__sequences(fn)+self.__conditions(fn)+ self.__structures(fn)
                    fns[name]=cc
        return fns
        
    def __sequences(self,func):
        cc=0
        last=None  
        for node in func.find_all("BooleanOperatorNode" ):            
            if last is None or node.value !=last.value or node.parent_find(last) is None:
                cc+=1
            
            if 'not' in [node.value for node in node.find_all("UnitaryOperatorNode")]:
                cc+=1
                
            last=node
        return cc
  
    def __conditions(self,func):
        return len(func.find_all("ElifNode")) + len(func.find_all("ElseNode"))
        
    def __structures(self,func):            
            
        increments= {"IfNode","TernaryOperatorNode","ComprehensionIfNode","ForNode","ComprehensionLoopNode",
                    "WhileNode","ExceptNode"}
        levels=increments.union({"ElseNode","ElifNode","DefNode","LambdaNode"})
        nodes=list()
        
        for node in increments:
            nodes.extend(func.find_all(node))
            
        cc=0
        for node in nodes:
            node=node.parent
            while node!=func.parent:
                name=node.__class__.__name__
                if name in levels and (name!='DefNode' or not self.__is_decorator(node)):
                    cc+=1
                node=node.parent
        return cc     
         
    def __is_decorator(self,func):
        values=[node.__class__.__name__ for node in func.value 
                                        if node.__class__.__name__ not in ['CommentNode','EndlNode']]                
        return len(values)==2 and values[0]=='DefNode' and values[1]=='ReturnNode'

if __name__ == '__main__':    
    import sys
    if len(sys.argv) != 3:
        print("""Syntax:
            python cc.py file_input.py file_output.json
            """)
    else:
        _, file, file_json = sys.argv
    cc=CognitiveComplexity()
    results=cc.evaluate(file)
    maxCC = max(results.values())
    with open(file_json, "w", encoding='utf8') as jf:
        json.dump({'max' : maxCC, 'results': results }, jf)
    print("Cognitive complexity of:", file)
    for name, cc in results.items():
        print('\t{} : {}'.format(name, cc))
    print("Max cognitive complexity:", maxCC)

