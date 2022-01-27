def binary_search(list, target):
    first = 0
    last = len(list) - 1
    index = last/2

    # run while first is not 0

    while first < 0:
        if list[index] == target:
            return index
            break
        # if target is less than halfway
        elif target < list[index]:
            index = index/2
        # if target is more than halfway 
        elif target > list[index]:
            index += index/2 