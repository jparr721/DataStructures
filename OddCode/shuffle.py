# List of ints/numbers, shuffle and return shuffled version

# rand() => [0, 1)
# rand() => 0.2
# rand() => 0.0
# rand() => 0.99 etc...
# shuffle([1, 3, 5, 2, 8]) => [3, 1, 5, 8, 2]
import math


def shuffle(int_list):
  list_length = len(int_list) # 5
  new_list = []
  for i in range(list_length):
    random_index = math.floor(list_length * rand())
    while new_list[random_index] is not None:
      random_index = math.floor(list_length * rand())
    new_list[random_index] = int_list[i]


def shuffle_2(int_list):
  list_length = len(int_list) # 5

  for i in range(list_length):
    width = list_length - i
    random_index = math.floor(width * rand())

    key = int_list[i]
    swap = int_list[random_index + i]

    int_list[random_index] = key
    int_list[i] = swap

