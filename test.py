def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nowcoda')
    strb = "\n\r hello coo \r\n"
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '_'.join(['a','b','c'])
    print 8, strc.split(' ')
    print 9, strc.find('ello')

def demo_buildin_function():
    print 1, max(2,1),min(5,3)
    print 2, len('xxx'),len([1,2,3])
    print 3, abs(-2)    #fabs,Math.fabs
    print 4, range(1,10,3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, chr(97), ord('a')
    print 8, divmod(11,3)

def demo_list():
    lista = [1,2,3] #vector Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0],listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb*2
    print 14, [0]*14
    print 15, lista.append(4)

def demo_dict():
    dicta = {1:1, 2:4, 3:9}
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value:', key, value
    dictb = {'+':add, '-':sub}
    print 4, dictb['+'](1,2)
    print 5, dictb.get('-')(15,3)
    dictb['*'] = 'x'
    print dictb

def demo_set():
    seta = set((1,2,3))
    setb = set((2,3,4))
    print 1, seta
    print 2, setb
    print 3, seta.intersection(setb), seta&setb
    print 4, seta | setb, seta.union(setb)
    print 5, seta - setb


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == '__main__':
    print 'hello nowcoder'
    #demo_string()
    #demo_buildin_function()
    #demo_list()
    #demo_dict()
    demo_set()