def number_swapper(number: str, n1, n2):
    number = list(number)

    number[n1], number[n2] = number[n2], number[n1]

    return ''.join(number)


def main():
    number = "12345"

    print(number_swapper(number, 3, 4))


main()
