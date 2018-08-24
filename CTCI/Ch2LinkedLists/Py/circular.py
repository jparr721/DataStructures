def cirular_list(ll):
    temp = ll.head
    compare = []

    while temp is not None:
        if temp in compare:
            return temp
        compare.push(temp)
        temp = temp.next
