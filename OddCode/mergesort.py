def mergesort(array):
    subarr = []
    return mergesort_r(array, subarr, 0, len(array) - 1)

def mergesort_r(array, helper, low, high):
    if (low < high):
        middle = (low + high) / 2
        mergesort_r(array, helper, low, middle)
        mergesort_r(array, helper, middle + 1, high)
        merge(array, helper, low, middle, high)

def merge(array, helper, low, middle, high):
    for i in range(array):
        helper[i] = array[i]

    helperLeft = low
    helperRight = middle + 1
    current = low

    while (helperLeft <= middle and helperRight <= high):
        if helper[helperLeft] <= helper[helperRight]:
            array[current] = helper[helperLeft]
            helperLeft += 1
        else:
            array[current] = helper[helperRight]
            helperRight += 1
        current += 1

    remaining = middle - helperLeft
    for i in range(remaining):
        array[current + i] = helper[helperLeft + i]
