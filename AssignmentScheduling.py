import random
import numpy as np

# temp scheduling
# get complete time

TIMETABLE = [13,15,10,21,34,9,25,23,11,8,12,17,30,14,45,27,31,20,6,5]
repetition = 0
itrn = 0
temp = 0
tempUpdated = 0
bestZ = int(1e9)

def getFirstSolution(times):
    jobs = []
    for i in range(len(times)):
        randomJob = random.randint(0,len(times)-1)
        jobs.append(times.pop(randomJob))
    return jobs

def calTotalCompleteTime(schedule):
    readyTime = []
    completeTime = []
    for i in range(len(schedule)):
        if i == 0:
            readyTime.append(0)
            completeTime.append(schedule[i])
            continue
        readyTime.append(readyTime[i-1]+schedule[i-1])
        completeTime.append(readyTime[i]+schedule[i])
    return sum(completeTime)

def getNewSol(oldSol):
    point1 = random.randint(0,len(oldSol)-1)
    point2 = random.randint(0,len(oldSol)-1)
    newSol = oldSol[:]
    newSol[point1], newSol[point2] = newSol[point2],newSol[point1]
    return newSol
def accept(oldZ,newZ,temp):
    e = np.exp(1)
    acceptance = e **((oldZ - newZ)/temp)
    pr_compare = random.random()
    if pr_compare < acceptance:
        return True
    else:
        return False
def getTemperature(currentZ):
    schedules = [0.2, 0.5, 0.5, 0.5, 0.5]
    temperatures = [currentZ * schedules[0]]

    for i in range(1, len(schedules)):
        temperatures.append(temperatures[i - 1] * schedules[i])

    # if updated == 0:
    #     baseTemperature = currentZ
    # else:
    #     baseTemperature = temp
    # tempSchedule = [0.2, 0.5, 0.5, 0.5, 0.5]
    # temp = baseTemperature * tempSchedule[updated]
    return temperatures

currentSol = getFirstSolution(TIMETABLE[:])
tempSchedule = getTemperature(calTotalCompleteTime(currentSol))

while True:
    temp = tempSchedule[tempUpdated]

    newSol = getNewSol(currentSol)
    currentZ = calTotalCompleteTime(currentSol)
    newZ = calTotalCompleteTime(newSol)

    if currentZ > newZ:
        currentSol = newSol
        currentZ = newZ
    else:
        if accept(currentZ,newZ,temp):
            currentSol = newSol
            currentZ = newZ

    if bestZ > currentZ:
        bestZ = currentZ
        bestSol = currentSol

    repetition += 1
    tempUpdated = itrn // 5
    itrn += 1


    if tempUpdated >= 5:
        break

print(bestSol,bestZ)

