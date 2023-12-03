import random as rd
import math
n = 40

PASSENGERS = 31433
STATIONS = 118
RUN = 201
# 31433
# 3:59 ~ 22:10
# 118
# 201 운행
# 1회당 156명 탑승

rateofCrossoverOptim = 0.75
rateofMutationOptim = 0.0007

rateofCrossoverWait = 0.75
rateofMutationWait = 0.0005

minNotImprovedOptim = 250
minRepeatationOptim = 750

minNotImprovedWait = 250
minRepeatationWait = 750

psgforStn = []
timeforStn = []
for i in range(STATIONS-1):
    pasforHere = rd.randint(0,int(PASSENGERS/118/201*2))
    psgforStn.append(pasforHere)

    timeforHere = rd.randint(3,13)
    timeforStn.append(timeforHere)

totalPsg = sum(psgforStn)
arrvStn = []
now= 0
for i in range(len(psgforStn)):
    if psgforStn[i] == 0:
        now += timeforStn[i]
        continue
    else:
        for j in range(1,psgforStn[i]+1):
            arrvStn.append(now+(j*(timeforStn[i]/psgforStn[i])))
        now += timeforStn[i]

# print(sum(psgforStn))
# print(timeforStn)
# print(arrvStn)
# # 각 승객이 정류장에 도착한 시간
# print(sum(timeforStn))


def getPopulation(n):
    population = []
    for i in range(n):
        gene = getGene()
        population.append(gene)
    return population

def getGene():
    gene = []
    for i in range(1092):
        gene.append(rd.randint(0,1))
    return gene

def getRunCost(gene):
    numberBus = 54
    runCost = 28424  # 운행 횟수 비용
    runBusCost = 347707  # 운행 대수 비용
    busCost = 121313  # 보유 차량 비용
    posBusRate = 0.05  # 운행 차량 대비 보유 차량 비율
    totalBus = numberBus + math.ceil(numberBus*posBusRate)
    runCount = sum(gene)
    cost = runCount*runCost + runBusCost*numberBus + totalBus*busCost
    return cost
def getWaitCost(gene,arrvStn):
    VOW = 6195.9 * (124.7 / 90.3)                                               # 2022년 기준 대기 시간 가치, 2007 소비자 물가지수 90.3, 2022 소비자 물가지수 124.7
    timetable = []
    waitTime = 0

    for i in range(len(gene)):
        if gene[i]:
            timetable.append(i)
    j = 0
    for t in timetable:
        waitPsg = []
        while j < len(arrvStn) and (arrvStn[j] <= t):
            waitPsg.append(arrvStn[j])
            j += 1
        for w in waitPsg:
            waitTime += t-w
    return math.ceil(waitTime*VOW)

def getZOptimRun(gene,arrvStn,currentMinCost):     # 최적 운행 횟수 결정 시 적합도 표현
    cost = getRunCost(gene)+getWaitCost(gene,arrvStn)
    return math.exp((cost-currentMinCost)/1000000)

def crossover(genes):
    g1,g2 = genes
    point = rd.randint(0,len(g1))
    newG1 = g1[:point] + g2[point:]
    newG2 = g2[:point] + g1[point:]
    return newG1, newG2

def mutation(genes):
    for g in genes:
        for i in range(len(g)):
            rdMutation = rd.random()
            if rdMutation < rateofMutationOptim:
                g[i] = int(not(g[i]))
    return genes

# start
repeated = 0
notImproved = 0

population = getPopulation(n)
populationCosts = []
for p in population:
    cost = getRunCost(p)+getWaitCost(p,arrvStn)
    populationCosts.append([cost,p])
currentMinCost,bestSolution = sorted(populationCosts)[0]
bestZ = getZOptimRun(bestSolution,arrvStn,currentMinCost)

while (repeated < minRepeatationOptim) or (notImproved < minNotImprovedOptim):
    # print("repeated: ",repeated,"notImproved:", notImproved)
    repeated += 1

    populationZ = []
    for p in population:
        z = getZOptimRun(p,arrvStn,currentMinCost)
        populationZ.append([z,p])
    populationZ = sorted(populationZ)

    qCrossover = []
    for z,p in populationZ[1:]:
        rdCrossover = rd.random()
        if rdCrossover < rateofCrossoverOptim:
            qCrossover.append(p)
        else:
            continue

        if len(qCrossover) == 2:
            o1,o2 = crossover(qCrossover)
            population += mutation([o1,o2])
            qCrossover = []

    for p in population:
        z = getZOptimRun(p,arrvStn,currentMinCost)
        populationZ.append([z,p])
    populationZ = sorted(populationZ)

    newPopulationZ = [populationZ[0]]
    selectIDX = 0
    while len(newPopulationZ) < n:
        rdSelection = rd.random()
        if rdSelection < 0.8:
            newPopulationZ.append(populationZ[selectIDX])
        selectIDX = (selectIDX+1)%len(populationZ)

    newPopulationZ = sorted(newPopulationZ)
    population = [p for z,p in newPopulationZ]
    if newPopulationZ[0][0] < bestZ:
        notImproved = 0
        bestZ,bestSolution = newPopulationZ[0]
        currentMinCost = getRunCost(bestSolution)+getWaitCost(bestSolution,arrvStn)
    else:
        notImproved += 1

print("최적 운행 수 도출을 위한 유전 알고리즘 반복 횟수:", repeated)

# 최적 운행 횟수 도출 완료
optRunCount = sum(bestSolution)
optStnTimetable = []

print("최적 운행 횟수:", optRunCount)
print("총 교통 비용(원):", currentMinCost)


for i in range(len(bestSolution)):
    if bestSolution[i] == 1:
        optStnTimetable.append(i)

def getTimeTable(timetable):
    stnTimeGap = [timetable[0]]
    for i in range(1,len(timetable)):
        stnTimeGap.append(timetable[i]-timetable[i-1])
    return stnTimeGap

def getWaitPopulation(n,timeGap):
    population = []
    for i in range(n):
        stnSchedule = [0]
        stnGap = timeGap[:]
        for j in range(1,len(timeGap)+1):
            rdIdx = rd.randint(0,len(stnGap)-1)
            stnSchedule.append(stnSchedule[j-1]+stnGap.pop(rdIdx))
        population.append(stnSchedule[1:])
    return population

def crossoverW(genes):
    g1,g2 = genes
    crossIdx = rd.randint(0,len(genes))
    o1 = g1[:crossIdx] + g2[crossIdx:]
    o2 = g2[:crossIdx] + g1[crossIdx:]
    return [sorted(o1),sorted(o2)]

def mutationW(genes):
    for g in genes:
        for i in range(len(g)):
            rdMutation = rd.random()
            if rdMutation < rateofMutationWait:
                g[i] += rd.randint(0-g[i],1092-g[i])
    return genes


def getZWait(g,arrv,minwt):
    wt = getWaitTime(g,arrv)
    # 적합도 계산
    return math.exp((wt-minwt)/500)

def getWaitTime(g,arrv):
    waitTime = 0
    j = 0
    for t in g:
        waitPsg = []
        while j < len(arrv) and (arrv[j] <= t):
            waitPsg.append(arrvStn[j])
            j += 1
        for w in waitPsg:
            waitTime += t-w
    return waitTime


stnTimeGap = getTimeTable(optStnTimetable)  # 최적 횟수 도출한 Schedule에서 각 도착 시간 간격 도출
population = [optStnTimetable] + getWaitPopulation(n-1,stnTimeGap) # 각 도착 시간 간격 기반으로 초기 집단 생성

repeated = 0
notImproved = 0

populationW = []
for g in population:
    waitTime = getWaitTime(g,arrvStn)
    populationW.append([waitTime,g])
minCurrentWaitTime = sorted(populationW)[0][0]


# start
while (repeated < minRepeatationWait) or (notImproved < minNotImprovedWait):
    # print("repeated:", repeated,"notImproved:", notImproved)
    repeated += 1

    populationZ = []
    for g in population:
        z = getZWait(g,arrvStn,minCurrentWaitTime)
        populationZ.append([z,g])

    qCrossover = []
    offPopulation = []
    populationZ = sorted(populationZ)
    bestZW, bestSolutionW = populationZ[0]
    for z,g in populationZ[1:]:
        rdCrossover = rd.random()
        if rdCrossover < rateofCrossoverWait:
            qCrossover.append(g)
        else:
            continue

        if len(qCrossover) == 2:
            offs = crossoverW(qCrossover)
            offPopulation += (mutationW(offs))
            qCrossover = []

    for ng in offPopulation:
        waitTime = getWaitTime(ng, arrvStn)
        z = getZWait(ng, arrvStn, minCurrentWaitTime)
        populationZ.append([z, ng])

    populationZ = sorted(populationZ)
    newPopulationZ = [populationZ[0]]

    selectIDX = 0
    while len(newPopulationZ) < n:
        rdSelection = rd.random()
        if rdSelection < 0.8:
            newPopulationZ.append(populationZ[selectIDX])
        selectIDX = (selectIDX+1)%len(populationZ)


    newPopulationZ = sorted(newPopulationZ)
    population = [g for z,g in newPopulationZ]

    if bestZW > newPopulationZ[0][0]:
        bestZW,bestSolutionW = newPopulationZ[0]
        minCurrentWaitTime = getWaitTime(bestSolutionW,arrvStn)
        notImproved = 0
    else:
        notImproved += 1



print("승객 최소 대기 시간을 위한 유전 알고리즘 반복 횟수", repeated)
print("알고리즘 전 승객 대기 시간(분):",getWaitTime(optStnTimetable,arrvStn))
print("알고리즘 후 승객 대기 시간(분):",minCurrentWaitTime)












