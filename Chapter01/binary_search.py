def binary_search(search_list, needle):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if search_list[mid] == needle:
            return mid

        if search_list[mid] > needle:
            high = mid - 1
        else:
            low = mid + 1

    return None


nums = [1, 5, 7, 20]

print(binary_search(nums, 15))
