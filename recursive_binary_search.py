def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        # if target on upper end
        elif list[midpoint] < target:
            # restart function using a new list, only the upper end of the original list
            return recursive_binary_search(list[midpoint + 1:], target)
        # if target is on lower end
        else:
            # restart function using a new list, only use lower end of original list
            return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("target found at: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 3)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)