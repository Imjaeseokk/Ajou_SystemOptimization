import random

n = 50
rc =0.95
rm = 0.05
NotImproved = 0

conveyer1 = [5,4,3,2,1]
conveyer2 = [10,9,8,7,6]
conveyer3 = [15,14,13,12,11]

readyCost = [
    [0,8,0,0,0,8,2,5,5,1,7,6,4,5,4],
    [0,0,3,0,0,8,6,8,4,5,4,6,2,5,8],
    [0,0,0,6,0,7,0,9,3,1,8,1,2,0,8],
    [0,0,0,0,0,4,5,3,0,3,6,5,2,10,7],
    [0,0,0,0,0,8,0,9,1,4,4,6,6,8,1],
    [8,0,5,7,6,0,6,0,0,0,9,4,7,7,9],
    [9,9,10,3,6,0,0,10,0,0,6,4,6,2,6],
    [2,2,1,5,2,0,0,0,10,0,9,3,2,6,9],
    [6,6,4,9,1,0,0,0,0,5,4,6,0,0,6],
    [9,10,7,9,4,0,0,0,0,0,10,6,9,4,6],
    [5,7,4,5,2,2,8,9,10,1,0,4,0,0,0],
    [1,9,8,6,4,1,4,1,7,7,0,0,7,0,0],
    [7,2,6,5,7,3,1,8,10,4,0,0,0,2,0],
    [10,0,2,9,3,9,5,2,5,3,0,0,0,0,8],
    [7,6,1,1,4,10,4,5,9,8,0,0,0,0,0]
]


def getCar(conv1,conv2,conv3):
    upConv = [conv1,conv2,conv3]
    cars = []
    for i in range(15):
        while True:
            randomForConv = random.randint(0,2)
            selectedConv = upConv[randomForConv]
            if selectedConv:
                nextCar = selectedConv.pop()
                cars.append(nextCar)
                break
    return cars

def calCost(cars):
    cost = 0
    for i in range(len(cars)-1):
        x,y = cars[i],cars[i+1]
        cost += readyCost[x-1][y-1]
    return cost


def getPopulation():
    populations = []
    for i in range(n):
        gene = (getCar(conveyer1[:], conveyer2[:], conveyer3[:]))
        populations.append([gene,calCost(gene)])

    populations = sorted(populations, key=lambda x: x[1])
    populations = [g for g,c in populations]
    return populations

def crossover(parent1,parent2):
    isfeasible = False
    while not isfeasible:
        point = random.randint(1,15)
        reorderGene1 = parent1[point - 1:]
        reorderGene2 = parent2[point - 1:]
        offspring1 = parent1[:point-1]
        offspring2 = parent2[:point-1]
        for i in range(len(parent1)):
            if parent2[i] in reorderGene1:
                offspring1.append(parent2[i])
            if parent1[i] in reorderGene2:
                offspring2.append(parent1[i])
        isfeasible = validation([offspring1,offspring2])
    return offspring1, offspring2


def mutation(offspring1, offspring2):
    isfeasible = False
    Off1mutationPt = random.randint(0,14)
    Off2mutationPt = random.randint(0,14)
    while not isfeasible:
        tempOffs = []
        for o in [offspring1, offspring2]:
            mutationPt = random.randint(0, 14)
            tempo = o[:]
            tempo[Off1mutationPt], tempo[mutationPt] = tempo[mutationPt], tempo[Off1mutationPt]
            tempOffs.append(tempo)

        isfeasible = validation(tempOffs)
    offspring1, offspring2 = tempOffs

    return offspring1, offspring2

def validation(offs):
    isfeasible = True
    for o in offs:
        conv1 = conveyer1[:]
        conv2 = conveyer2[:]
        conv3 = conveyer3[:]
        for c in o:
            if conv1 and conv1[-1] == c:
                conv1.pop()
            elif conv2 and conv2[-1] == c:
                conv2.pop()
            elif conv3 and conv3[-1] == c:
                conv3.pop()
            else:
                isfeasible = False
                break
    return isfeasible


def getNewPopulations(oldPopulations):
    newPopulations = []
    for p in oldPopulations:
        cost = calCost(p)
        newPopulations.append([p,cost])
    newPopulations = sorted(newPopulations, key = lambda x: x[1])
    newPopulations = [g for g,c in newPopulations[:n]]
    return newPopulations

def getOffsprings(parents):
    offsprings = []
    for i in range(0,n,2):
        randomofCrossover = random.random()
        if randomofCrossover < rc:
            off1,off2 = crossover(parents[i],parents[i+1])
        else:
            off1, off2 = parents[i],parents[i+1]
        randomofMutation = random.random()
        if randomofMutation < rm:
            off1,off2 = mutation(off1,off2)
        offsprings.extend([off1,off2])
    return offsprings


populations = getPopulation()
zc = populations[0]

while NotImproved < 10:
    offsprings = getOffsprings(populations)
    populations.extend(offsprings)
    populations = getNewPopulations(populations)
    zn = populations[0]

    if zc == zn:
        NotImproved += 1
    else:
        oldCost = calCost(zc)
        newCost = calCost(zn)
        if oldCost >= newCost:
            zc = zn
            NotImproved = 0
        else:
            NotImproved += 1

    print(f"NotImproved:{NotImproved} 지금까지의 최적해는 {zc}, 최적해의 준비 비용은 {calCost(zc)}입니다.")

print(f"최종해는 {zc}, 준비 비용은 {calCost(zc)}입니다.")


