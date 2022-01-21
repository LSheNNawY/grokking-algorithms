# quick sort
# 1- take a pivot, then get the numbers before and after in two sub arrays
# 2- run quick sort on these sub arrays and then combine them again

def quick_sort(unsorted_list):
    # base case if array size < 2
    if len(unsorted_list) < 2:
        return unsorted_list

    pivot = unsorted_list[0]
    # less than pivot array

    # loop over array without first number arr[1:]

    # less = []
    # greater = []
    # for i in arr[1:]:
    #     if i <= pivot:
    #         less.append(i)
    #     else:
    #         greater.append(i)

    # shorthand loop

    # less than pivot array
    less = [i for i in unsorted_list[1:] if i <= pivot]
    # greater than pivot array
    greater = [i for i in unsorted_list[1:] if i > pivot]
    # run quick sort on less and greater than again then combine
    return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [22, 7, 30, 15, 8, 22, 40, 44]

print(quick_sort(arr))
