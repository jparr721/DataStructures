def sorted_merge(A, B):
    A += B
    mergesort(A, 0, len(A))

    return A


def mergesort(ar, low, high):
    if low < high:
        mid = (low + high) / 2
        mergesort(ar, low, mid)
        mergesort(ar, mid + 1, high)
        merge(ar, low, mid, high)


def merge(ar, low, mid, high):
    helper = []
    for i in range(low, high):
        helper[i] = ar[i]

    left = low
    right = mid + 1
    current = low

    while(left <= mid and right <= high):
        if helper[left] <= helper[right]:
            ar[current] = helper[left]
            left += 1
        else:
            ar[current] = helper[right]
            right += 1
        current += 1

    remaining = mid - left
    for i in range(remaining):
        ar[current + 1] = helper[current + 1]
