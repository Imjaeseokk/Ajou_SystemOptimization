import random
def calculateZ(x):
    return 12*(x**5) - 975*(x**4) + 28000*(x**3) - 345000*(x**2) + 1800000*x

def oneBitChange(sol,tabuList):
    newSolutions = []
    for picked in range(0,7):
        beforeSol = convertToBin(sol)
        changedBit = "1" if beforeSol[picked] == "0" else "0"
        beforeSol[picked]

        afterSol = beforeSol[:picked] + changedBit + beforeSol[picked+1:]
        afterSol = int(afterSol,2)
        if (afterSol <= 100) and (afterSol not in tabuList):
            newSolutions.append(afterSol)

    # for i in newSolutions:
    #     print(i,int(i,2))
    return newSolutions

def convertToBin(dec):
    binarySol = ""
    while dec > 1:
        binarySol += str(dec%2)
        dec //= 2
    binarySol += "1"

    for i in range(len(binarySol),7):
        binarySol += "0"
    result = binarySol[::-1]

    return result

def selectedSol(solutions):
    maximum = 0
    nextSol = solutions[0]
    for s in solutions:
        Z = calculateZ(s)
        if Z > maximum:
            nextSol = s
            maximum = Z

    return nextSol


def main():
    currentSol = random.randint(0, 100)
    currentZ = calculateZ(currentSol)
    bestSol = currentSol
    tabuList = []
    NotImproved = 0

    while True:
        if NotImproved >= 3:
            break

        sols = oneBitChange(currentSol,tabuList)     # 주변 해들
        nextSol = selectedSol(sols)         # 가장 높은 해 선정

        if calculateZ(bestSol) < calculateZ(nextSol):
            bestSol = nextSol
            NotImproved = 0
        else:
            NotImproved += 1

        if len(tabuList) < 10:
            tabuList.append(currentSol)
        else:
            tabuList.pop(0)
            tabuList.append(currentSol)
        currentSol = nextSol


    print(currentSol,calculateZ(currentSol))
if __name__ == '__main__':
    for i in range(10):
        main()

