import random as rd

n = 10
rc =0.95
rm = 0.05
NotImproved = 0
z = []


def toInt(Gene):
    value = 0
    for i in range(len(Gene)):
        value += (2**i)*Gene[i]
    return value

def getParent():
    parentGene = []
    i = 0
    while len(parentGene) < 10:
        parentGene.append([])
        for j in range(7):
            randG = rd.random()
            if randG < 0.5:
                parentGene[i].append(0)
            else:
                parentGene[i].append(1)
        if toInt(parentGene[i]) > 100:
            parentGene.pop()
        else:
            i += 1

    return parentGene

def getScore(Gene):
    x = toInt(Gene)
    return 12 * pow(x, 5) - 975 * pow(x, 4) + 28000 * pow(x, 3) - 345000 * pow(x, 2) + 1800000 * x

def sortByScore(Genes):
    for g in range(len(Genes)):
        pass

print(getParent())

while NotImproved < 5:
    populations = getParent()


