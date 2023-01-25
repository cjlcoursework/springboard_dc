def binary_search(list_of_numbers, query_item):
    # print(f"find {query_item} in {list_of_numbers}")
    # Set index of the first item in the list and an index of the last item in the list
    index_first = 0
    index_last = len(list_of_numbers) - 1
    # Set the found variable to False
    found = False

    while index_first <= index_last and not found:  # Check if the index_first is less than or equal to the index_last
        # print(f"\tseeking in {list_of_numbers[index_first:index_last+1]} from {index_first} to {index_last}")
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


def search_test(test_list, query_element):
    print(binary_search(test_list, query_element))
    print(binary_search(test_list, query_element))


search_test([-3, 1, 3, 9, 11, 14, 22, 123, 302, 304, 434, 501, 1230, 5412, 381923], 13)
search_test( [1, 7, 9, 12, 22, 43, 104], 9)
search_test([-20, -5, 0, 0, 30, 100], 31)
search_test([4, 17, 28, 30, 52, 61, 666, 1001], 666)
