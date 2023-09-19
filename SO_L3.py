import random as rd

n = 10
rc =0.95
rm = 0.05
NotImproved = 0
z = []


def toInt(Gene):
    value = 0
    for i in range(len(Gene)):
        value += (2**i)*Gene[-(i+1)]
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
    Gene = []
    for g in range(len(Genes)):
        value = getScore(Genes[g])
        Gene.append([Genes[g],value])
    sortedGene = sorted(Gene, key = lambda x:(-x[1]))
    delScore = [a for a,b in sortedGene[:10]]
    return delScore

def getOffspring(Genes):    # 부모 유전자로 자식 만들기
    offspring = []
    i = 0
    while len(offspring)< 10:
        p1 = Genes[i]
        p2 = Genes[i+1]
        o1 = [None for _ in range(7)]
        o2 = [None for _ in range(7)]
        for j in range(7):
            if p1[j] == p2[j]:
                o1[j] = p1[j]
                o2[j] = p1[j]
            else:
                for k in [o1,o2]:
                    rand = rd.random()
                    if rand < 0.5:
                        k[j] = 0
                    else:
                        k[j] = 1

        for l in [o1,o2]:
            randForMut = rd.random()
            if randForMut < rm:

                randForBit = rd.randint(0,6)
                l[randForBit] = int(not l[randForBit])
        if (toInt(o1) <= 100) and (toInt(o2) <= 100):
            offspring.extend([o1,o2])
            i +=2
    return offspring


populations = getParent()
print(populations)
populations = sortByScore(populations)
print(populations)        # 적합도로 sorting한 상위 10개


while NotImproved < 999:
    offspring = getOffspring(populations) # 자녀 생성
    print(offspring)
    populations = sortByScore(populations + offspring) # 기존 모집단 + 자녀 합해서 적합도 순으로 정렬

    if z:
        new_z = populations[0]
        z.append(new_z)
        zScore = sortByScore(z)
        high_z = zScore[0]
        if new_z != high_z:
            NotImproved = 0
        else:
            NotImproved +=1
    else:
        new_z = populations[0]
        z.append(new_z) # 내림차순 맨 앞에 있는 최대 유전자
    print(new_z,toInt(new_z))
    print(NotImproved)








