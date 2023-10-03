
check = []
for i in range(int(input())):
    check.append(list(map(int,input().split())))



def valid(cars):
    flag = True
    for cars in check:
        conveyer1 = [5, 4, 3, 2, 1]
        conveyer2 = [10, 9, 8, 7, 6]
        conveyer3 = [15, 14, 13, 12, 11]
        for c in cars:
            if conveyer1 and conveyer1[-1] == c:
                conveyer1.pop()
            elif conveyer2 and conveyer2[-1] == c:
                conveyer2.pop()
            elif conveyer3 and conveyer3[-1] == c:
                conveyer3.pop()
            else:
                print("infeasible")
                flag = False
                break
        if flag:
            print("yes")
        else:
            print("end")
            break


valid(check)

# -----------------------------------



# o1 = [2,1,4,3]
# o2 = [1,2,4,3]
#
# for o in [o1,o2]:
#     conv1 = [1, 2]
#     conv2 = [3, 4]
#     for c in o:
#         print(c)
#         if conv1 and conv1[-1] == c:
#             conv1.pop()
#         elif conv2 and conv2[-1] == c:
#             conv2.pop()
#         else:
#             print("nope")
#             break
#     print("yeah")

# --------------------------------
#
# offspring1 = list(map(int,input().split()))
# offspring2 = list(map(int,input().split()))
#
# conveyer1 = [5, 4, 3, 2, 1]
# conveyer2 = [10, 9, 8, 7, 6]
# conveyer3 = [15, 14, 13, 12, 11]
# def mutation(offspring1, offspring2):
#     isfeasible = True
#     while isfeasible:
#         for o in [offspring1, offspring2]:
#             point1 = random.randint(0, 14)  # 1번째 원소부터 15번째 원소 중 하나 선택
#             point2 = random.randint(0, 14)
#             o[point1], o[point2] = o[point2], o[point2]
#         isfeasible = validation([offspring1, offspring2])
#
#     return offspring1, offspring2
#
#
# def validation(offs):  # crossover 후 2개씩 검증, mutation 후 2개씩 검증
#     isfeasible = True
#     for o in offs:
#         conv1 = conveyer1[:]
#         conv2 = conveyer2[:]
#         conv3 = conveyer3[:]
#         for c in o:
#             if conv1 and conv1[-1] == c:
#                 conv1.pop()
#             elif conv2 and conv2[-1] == c:
#                 conv2.pop()
#             elif conv3 and conv3[-1] == c:
#                 conv3.pop()
#             else:
#                 print("infeasible")
#                 isfeasible = False
#                 break
#
#     return isfeasible
#
# print(*mutation(offspring1,offspring2))

