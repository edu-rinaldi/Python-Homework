def _es5(p):
    ls = [p]
    if len(p)==1:
        return ls
    for i in range(len(p)):
        tmp = list(p)
        del tmp[i]
        newp = "".join(tmp)
        ls.extend(es5(newp))
    return ls

def isCrescente(p):
    return list(p)==sorted(p)

def es5(parola):
    setW = set(filter(lambda w: isCrescente(w),_es5(parola)))
    return sorted(setW)
print(es5("zanzara"))
