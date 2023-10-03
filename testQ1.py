cars = [1, 11, 12, 6, 2, 3, 13, 7, 14, 4, 8, 5, 15, 9, 10]

conveyer1 = [5,4,3,2,1]
conveyer2 = [10,9,8,7,6]
conveyer3 = [15,14,13,12,11]

def valid(cars):
    for c in cars:
        if conveyer1[-1] == c:
            conveyer1.pop()
        elif conveyer2[-1] == c:
            conveyer2.pop()
        elif conveyer3[-1] == c:
            conveyer3.pop()
        else:
            print("infeasible")