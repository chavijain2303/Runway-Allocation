

maxsize = 20000



def parent(i):
    return i / 2


def lchild(i):
    return 2 * i
def rchild(i):
    return 2*i+1
def shiftup(i):
    while i>1 and priority[i][0]>priority[parent(i)][0]:
        p = parent(i)
        t = priority[i][0]
        priority[i][0] = priority[p][0]
        priority[p][0] = t
        t = priority[i][1]
        priority[i][1] = priority[p][1]
        priority[p][1] = t
        t = priority[i][2]
        priority[i][2] = priority[p][2]
        priority[p][2] = t
def shiftdown(priority,i):
    index = i
    l = lchild(i)
    r=rchild(i)
    if(l<len(priority)):
        if (priority[l][0] > priority[index][0]):
            index = l
    if(r<len(priority)):
        if (priority[r][0] > priority[index][0]):
            index = r

    if index is not i:

        priority[i], priority[index] = priority[index], priority[i]
        shiftdown(priority, index)
def heapify(priority):
    n= len(priority)
    for i in range((n-1)//2,-1,-1):
        shiftdown(priority,i)
def getmax(priority):
    n=len(priority)-1
    query=priority[0]
    priority[0], priority[n] = priority[n],priority[0]
    n=n-1
    return query








