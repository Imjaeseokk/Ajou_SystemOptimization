import random
import numpy as np

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
    random1 = random.randint(0,len(oldSol)-1)
    random2 = random.randint(0,len(oldSol)-1)
    point1 = min(random1,random2)
    point2 = max(random1,random2)
    subtour = oldSol[point1:point2+1]
    subtour.reverse()
    newSol = oldSol[:point1] + subtour + oldSol[point2+1:]

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

    return temperatures

TIMETABLE = [13,15,10,21,34,9,25,23,11,8,12,17,30,14,45,27,31,20,6,5]
repetition = 0
itrn = 1
tempUpdated = 0

currentSol = getFirstSolution(TIMETABLE[:])
currentZ = calTotalCompleteTime(currentSol)
bestZ = currentZ
tempSchedule = getTemperature(currentZ)

while tempUpdated < 5:
    print(tempUpdated, itrn)
    temp = tempSchedule[tempUpdated]

    newSol = getNewSol(currentSol)
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


print(bestSol,bestZ)
