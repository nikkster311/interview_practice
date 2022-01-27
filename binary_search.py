def binary_search(list, target):
    first = 0
    last = len(list) - 1

    # run while first is not 0

    while first <= last:
        #  //2 returns a rounded up result (no dec)
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
            break
        # if target is less than halfway
        elif target < list[midpoint]:
            last = midpoint - 1
        # if target is more than halfway 
        else:
            first = midpoint + 1 

    return None



def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10, 11, 12]

result = binary_search(numbers, 12)
verify(result)