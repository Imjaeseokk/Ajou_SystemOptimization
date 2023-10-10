import random
import numpy as np
# parameter initialization

currentSol = random.uniform(0,100)
temp = 0.2 * currentSol
repetition = 0
itrn = 1
tempUpdated = 0
bestFunc = 0
bestSol = 0

def getNewSol(sol):
    normalRandom = np.random.normal(0,100/6,1)
    newSol = sol+normalRandom
    while newSol > 100 or newSol < 0:
        normalRandom = np.random.normal(0, 100 / 6, 1)
        newSol = sol + normalRandom
    return newSol

def getFunc(x):
    return 12*(x**5)-975*(x**4)+28000*(x**3)-345000*(x**2)+1800000*x

def accept(oldFunc,newFunc,temp):
    e = np.exp(1)
    acceptance = e*((newFunc - oldFunc)/temp)
    accepRef = random.random()
    if accepRef < acceptance:
        return True
    else:
        return False

while True:
    newSol = getNewSol(currentSol)
    currentFunc = getFunc(currentSol)
    newFunc = getFunc(newSol)

    if currentFunc < newFunc:
        currentSol = newSol
    else:
        if accept(currentFunc,newFunc,temp):
            currentSol = newSol

    if bestFunc < currentFunc:
        bestFunc = currentFunc
        bestSol = currentSol

    repetition += 1
    print(bestSol,bestFunc,itrn)
    if repetition >= 5:
        repetition = 0
        tempUpdated += 1
        temp = 0.5 * temp

    if tempUpdated >= 5:
        print(bestSol)
        break

    itrn += 1










