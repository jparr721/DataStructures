def any_pal_all_pos(arr):
    return all(i > 0 for i in arr) and all(str(i) == str(i)[::-1] for i in arr)


if __name__ == "__main__":
    print(any_pal_all_pos([1, 2, 3, 4, 5, 16, 22]))
