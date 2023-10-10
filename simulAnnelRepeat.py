import random
import numpy as np

bestSol = random.uniform(0,100)
temp = 0.2 * bestSol
repetition = 0
itrn = 1
tempUpdated = 0

def getNewSol(sol):
    normalRandom = np.random.normal(0,100/6,1)
    newSol = sol+normalRandom
    while newSol > 100 or newSol < 0:
        normalRandom = np.random.normal(0, 100 / 6, 1)
        newSol = sol + normalRandom
    return newSol

def getFunc(x):
    return 12*(x**5)-975*(x**4)+28000*(x**3)-345000*(x**2)+1800000*x

def accept(oldSol,newSol,temp):
    e = np.exp(1)
    acceptance = e*((newSol - oldSol)/temp)
    accepRef = random.random()
    if accepRef < acceptance:
        return True
    else:
        return False

result = []

for i in range(100):
    bestSol = random.uniform(0, 100)
    temp = 0.2 * bestSol
    repetition = 0
    itrn = 1
    tempUpdated = 0

    while True:
        newSol = getNewSol(bestSol)
        bestFunc = getFunc(bestSol)
        newFunc = getFunc(newSol)

        if bestFunc < newFunc:
            bestSol = newSol
        else:
            if accept(bestSol,newSol,temp):
                bestSol = newSol

        repetition += 1
        print(bestSol,bestFunc)
        if repetition >= 5:
            repetition = 0
            tempUpdated += 1
            temp = 0.5 * temp

        if tempUpdated >= 5:
            print(bestSol)
            break
    result.append(bestSol)

print(result)
print(bestSol,sum(result)/len(result))










