def binary_search(list, needle):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if list[mid] == needle:
            return mid

        if list[mid] < needle:
            high = mid - 1
        else:
            low = mid + 1

    return None


nums = [1, 5, 7, 20]

print(binary_search(nums, 15))
