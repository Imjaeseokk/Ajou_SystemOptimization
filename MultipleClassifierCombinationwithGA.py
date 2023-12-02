import random as rd


n = 20

KOSPIlevel = ["BR","ED","EU","BL"]
ClsPerform = [[0.56,0.482,0.49,0.625],
                [0.64,0.536,0.569,0.708],
              [0.48,0.714,0.765,0.5]]

def makeKOSPI(n):
    dataset = []
    for i in range(n):
        dataset.append(rd.random())
    return dataset

def getBasePopulation(n):       # 초기 모집단 생성
    population = []
    for i in range(n):
        gene = []
        for j in range(3):
            clsGene = []
            for k in range(4):
                clsGene.append(rd.random())
            gene.append(clsGene)
        population.append(gene)
    return population


def classifierML(x,cls):        # Machine Learning Classifier Implementation
    rdCorrect = rd.random()
    case = int(x//0.25)
    if (case == cls) and (rdCorrect < ClsPerform[0][case]):
        return 0.9999
    else:
        return rd.random()

def classifierEX(x,cls):
    rdCorrect = rd.random()
    case = int(x//0.25)
    if (case == cls) and (rdCorrect < ClsPerform[1][case]):
        return 0.9999
    else:
        return rd.random()

def classifierUS(x,cls):
    rdCorrect = rd.random()
    case = int(x//0.25)
    if (case == cls) and (rdCorrect < ClsPerform[2][case]):
        return 0.9999
    else:
        return rd.random()

def calZ(w,n,x):
    total = 0
    for i in range(n):
        total += calHR(w,x)
    return total/n

def checkClassifiers(x,realCls,w):
    measuresML = []
    measuresEX = []
    measuresUS = []
    for i in range(4):
        measuresML.append(classifierML(x,i)*w[0][i])
    for i in range(4):
        measuresEX.append(classifierML(x,i)*w[1][i])
    for i in range(4):
        measuresUS.append(classifierML(x,i)*w[2][i])
    if measuresML.index(max(measuresML)) == \
        measuresML.index(max(measuresML)) == \
        measuresML.index(max(measuresML)) == realCls:
        return True
    else:
        return False


def calHR(w,x):       # 가중치랑 실제 class 입력받기
    realCls = int(x//0.25)
    # if 0.9999*3 == (classifierML(x,realCls) + classifierEX(x,realCls) + classifierUS(x,realCls)):         # 모든 case 맞췄을 때
    #     return 1        # 1 출력
    if checkClassifiers(x,realCls,w):
        return 1
    else:
        Ej = calE(w,realCls,x)    # 실제 class에 대한 분류기들 측정 값
        Eall = 0
        for i in range(4):  # 모든 class에 대한 분류기들 측정 값
            Eall += calE(w,i,x)
        return Ej/Eall      # 모든 Class 측정에 대한 실제 Class에 대한 측정의 비율

def calE(w,cls,x):
    E = 0
    E += classifierML(x,cls)*w[0][cls]
    E += classifierEX(x,cls)*w[1][cls]
    E += classifierUS(x,cls)*w[2][cls]
    return E

kospi = makeKOSPI(n)     # KOSPI 예측에 사용되는 data x 집합

# for i in range(10):
#     y = kospi[i]
#     check = []
#     for j in range(4):
#         check.append(classifierML(y,j))
#     idx = check.index(max(check))
#     print(KOSPIlevel[int(y//0.25)],KOSPIlevel[idx])



population = getBasePopulation(n)
print(population[0])
for i in range(n):
    print(calZ(population[i],n,kospi[i]))

