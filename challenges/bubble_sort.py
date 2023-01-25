def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):  # run N times, where N is number of elements in a list
        # Last i elements are already in place
        # It starts at 1 so we can access the previous element
        for j in range(1, len(list_of_numbers) - i):  # N-i elements
            if list_of_numbers[j - 1] > list_of_numbers[j]:  # check if previous element is bigger than the current element
                # Swap code from the instructors notes:
                # print(f"compare index: {j-1} - {j}:  values: {list_of_numbers[j - 1]} - {list_of_numbers[j]}")
                temp = list_of_numbers[j - 1]
                list_of_numbers[j - 1] = list_of_numbers[j]
                list_of_numbers[j] = temp

    return list_of_numbers


# Do not change code below this line
unsorted_list = [20, 31, 5, 1, 591, 1351, 693]
print(unsorted_list)
print(bubble_sort(unsorted_list))
