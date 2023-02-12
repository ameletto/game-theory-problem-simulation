def factor(x, list):
    for y in range (1,x):
        if (x%(x-y)==0):
            list.append(x-y)
    return list

def reduce(x, alreadywritten):
    helperfactors=[]
    factor(x, helperfactors)
    for y in range (len(helperfactors)):
        if (x%helperfactors[y]==0 and helperfactors[y] not in alreadywritten and helperfactors[y]!=1):
            alreadywritten.append(helperfactors[y])
            return helperfactors[y]

def augment(x, prevSelf, alreadywritten):
    helperfactors=[]
    factor(prevSelf, helperfactors)
    for y in range (len(helperfactors)):
        if (helperfactors[y]%x==0 and helperfactors[y] not in alreadywritten):
            alreadywritten.append(helperfactors[y])
            return helperfactors[y]

alreadywrittentotal=[]
alreadywritteninteration=[]

print("What number does Christina start with: ")
input=int(input())

for n in range (input,input+1):
    exit=0
    a=n
    while(True):  
        if exit==1:
            break
        b=reduce(n, alreadywrittentotal)
        alreadywritteninteration.append(b)
        if b==None:
            print(n, "Christina wins")
            break
        while(True):
            newA=augment(b, a, alreadywritteninteration)
            if newA==None:
                newA=reduce(b, alreadywritteninteration)
            if newA==None:
                print(n, "Ava wins")
                exit=1
                break
            if newA==None:
                break
            newB=augment(newA, b, alreadywritteninteration)
            if newB==None:
                newB=reduce(newA, alreadywritteninteration)
                if newB==None:
                    alreadywritteninteration=[]
                    break
    alreadywrittentotal=[]

#realized that A can also sabotage