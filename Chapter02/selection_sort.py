# a function that get the least number
# returns the index of the smallest number
def get_smallest_number(list_of_numbers):
    smallest_index = 0
    smallest_number = list_of_numbers[0]

    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index] < smallest_number:
            smallest_number = list_of_numbers[index]
            smallest_index = index

    return smallest_index


# selection sort algorithm
def generate_sorted_list_with_selection_sort(unsorted_list):
    sorted_list = []
    for index in range(len(unsorted_list)):
        smallest_index = get_smallest_number(unsorted_list)
        sorted_list.append(unsorted_list.pop(smallest_index))
        print(unsorted_list, 'unsorted list')

    return sorted_list


print(generate_sorted_list_with_selection_sort([22, 0, 7, 8, 2, 19, 8]))
