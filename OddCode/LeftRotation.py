"""
Left rotation rotates an array left.
[1, 2, 3, 4, 5, 6, 7] 
After 2 rotations
[3, 4, 5, 6, 7, 1, 2]
d = number of rotations
n = size of array
"""

def left_rotation(array, d, n):
    while d is not 0:
        temp = array[0]
        for i in range(n - 1):
            array[i] = array[i + 1]
        array[n-1] = temp
        d -= 1
    return array

print(left_rotation([1, 2, 3, 4, 5, 6, 7], 2, 7))

