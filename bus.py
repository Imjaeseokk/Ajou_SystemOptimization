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

rateofCrossover = 0.75
rateofMutationOptim = 0.0007
rateofMutationWait = 0.0005
minNotImprovedOptim = 250
minRepeatationOptim = 750

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

print(sum(psgforStn))
print(timeforStn)
print(arrvStn)          # 각 승객이 정류장에 도착한 시간
print(sum(timeforStn))


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
    cost = 0

    cost += runCount*runCost
    cost += runBusCost*numberBus
    cost += totalBus*busCost

    return cost

def getWaitCost(gene,arrvStn):
    VOW = 6195.9 * (124.7 / 90.3)  # 2022년 기준 대기 시간 가치
                                    # 2007 소비자 물가지수 90.3
                                    # 2022 소비자 물가지수 124.7
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
# repeated = 0
# notImproved = 0
#
# population = getPopulation(n)
# populationCosts = []
# for p in population:
#     cost = getRunCost(p)+getWaitCost(p,arrvStn)
#     populationCosts.append([cost,p])
# currentMinCost,bestSolution = sorted(populationCosts)[0]
# bestZ = getZOptimRun(bestSolution,arrvStn,currentMinCost)
#
# while (repeated < minRepeatationOptim) or (notImproved < minNotImprovedOptim):
#     print("repeated: ",repeated,"notImproved:", notImproved)
#     repeated += 1
#
#     populationZ = []
#     for p in population:
#         z = getZOptimRun(p,arrvStn,currentMinCost)
#         populationZ.append([z,p])
#     populationZ = sorted(populationZ)
#
#
#     waitCrossover = []
#     for z,p in populationZ[1:]:
#         rdCrossover = rd.random()
#         if rdCrossover < rateofCrossover:
#             waitCrossover.append(p)
#         else:
#             continue
#
#         if len(waitCrossover) == 2:
#             o1,o2 = crossover(waitCrossover)
#             population += mutation([o1,o2])
#             waitCrossover = []
#
#     for p in population:
#         z = getZOptimRun(p,arrvStn,currentMinCost)
#         populationZ.append([z,p])
#     populationZ = sorted(populationZ)
#
#     newPopulationZ = [populationZ[0]]
#     selectIDX = 0
#     while len(newPopulationZ) <= n:
#         rdSelection = rd.random()
#         if rdSelection < 0.8:
#             newPopulationZ.append(populationZ[selectIDX])
#         selectIDX = (selectIDX+1)%len(populationZ)
#
#     population = [p for z,p in newPopulationZ]
#     if newPopulationZ[0][0] < bestZ:
#         notImproved = 0
#         bestZ,bestSolution = newPopulationZ[0]
#         currentMinCost = getRunCost(bestSolution)+getWaitCost(bestSolution,arrvStn)
#     else:
#         notImproved += 1
#
#     print(len(population))
#     print(len(populationZ))
#
# print(bestSolution)
# print(sum(bestSolution))
#
# # 최적 운행 횟수 도출 완료
# optRunCount = len(bestSolution)
# optStnTimetable = []
#
#
#
# for i in range(len(bestSolution)):
#     if bestSolution[i] == 1:
#         optStnTimetable.append(i)
#
# print(optStnTimetable)

print("최소 대기")

optStnTimetable = [19, 25, 36, 43, 54, 59, 87, 91, 101, 107, 124, 132, 136, 140, 146, 151, 157, 175, 181, 187, 191, 193, 198, 202, 211, 215, 226, 232, 246, 250, 257, 261, 266, 273, 277, 284, 289, 302, 303, 316, 354, 370, 376, 394, 400, 404, 419, 435, 450, 451, 455, 459, 464, 468, 505, 507, 511, 516, 524, 527, 540, 563, 569, 576, 581, 586, 592, 617, 624, 629, 632, 638, 641, 645, 650, 656, 662, 669, 683, 691, 695, 699, 713, 717, 731, 758, 760, 765, 772, 776, 780, 787, 795, 799, 801, 803, 816, 830, 837, 841, 846, 851, 856, 863, 877, 895, 926, 1061, 1075]


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

stnTimeGap = getTimeTable(optStnTimetable)  # 최적 횟수 도출한 Schedule에서 각 도착 시간 간격 도출
print("time",stnTimeGap)
population = getWaitPopulation(n,stnTimeGap) # 각 도착 시간 간격 기반으로 초기 집단 생성















