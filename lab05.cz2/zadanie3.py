numList = [5, 8, 6, 21, 13, 17, 3, 1, 5, 10]
numSum = 0

for i in range(len(numList)):
    if i % 2 == 0:
        numSum += numList[i]

print(numSum)

