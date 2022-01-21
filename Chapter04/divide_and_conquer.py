arr = [22, 11, 10, 7, 8]


# getting the summation of an array using recursion
# base case index = 0 OR -1
def get_array_sum(array, n):
    if n == -1:
        return 0

    return array[n] + get_array_sum(array, n - 1)


print(get_array_sum(arr, len(arr) - 1))


# getting array elements' count
def get_array_count(array):
    if len(array) == 0:
        return 0

    return 1 + get_array_count(array[1:])


print(get_array_count(arr))
