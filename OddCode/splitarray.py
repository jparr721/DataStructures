"""
Split an array in such a way that 
both sides are equal in value. If this
is not possible, return -1
"""

def splitArr(array):
    total = 0
    leftSubArr = []
    rightSubArr = []
    for i in range(len(array)):
        total += array[i]

    target = total / 2
    leftSum = 0
    lastLeft = 0
    for i in range(len(array)):
        if leftSum < target:
            leftSum += array[i]
            leftSubArr.append(array[i])
        else:
            lastLeft = i
            break
    
    rightSum = 0
    for j in range(lastLeft, len(array)):
        if rightSum < target or j == len(array):
            rightSum += array[j]
            rightSubArr.append(array[j])
        else:
            break

    if leftSum == rightSum:
        print(leftSubArr)
        print(rightSubArr)
        return True

    return False

print(splitArr([1, 6, 4, 3]))
print(splitArr([1, 4, 6, 3]))
print(splitArr([1, 2, 3, 4, 5, 5]))
