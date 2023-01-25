
def binary_search(list_of_numbers, query_item):
    print(f"find {query_item} in {list_of_numbers}")
    # Set index of the first item in the list and an index of the last item in the list
    index_first = 0
    index_last = len(list_of_numbers) - 1
    # Set the found variable to False
    found = False

    while index_first <= index_last and not found:  # Check if the index_first is less than or equal to the index_last
        print(f"\tseeking in {list_of_numbers[index_first:index_last+1]} from {index_first} to {index_last}")
        middle_index = (index_last + index_first) // 2  # using index_first and index_last find the middle index

        if list_of_numbers[middle_index] == query_item:  # Check if the middle element is equal to the query_item
            found = True
            break
        else:
            if query_item < list_of_numbers[middle_index]:
                index_last = middle_index - 1  #  If the query_item is less than the middle item, use the index_last to eliminate the upper part of the list
            else:
                index_first = middle_index + 1

    # Return the found boolean variable
    return found


# Do not change code below this line
test_list = [4, 13, 22, 28, 34, 117, 943, 1032, 4222]
print(binary_search(test_list, 4222))
print(binary_search(test_list, 33))