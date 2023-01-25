
def insert_sort(list_of_numbers):
    for index in range(len(list_of_numbers)):

        current_element = list_of_numbers[index]  # Access the current element
        position = index

        # Check if a position is greater than zero AND the previous item is greater than the current element
        while position > 0 and list_of_numbers[position - 1] > current_element:
            list_of_numbers[position] = list_of_numbers[
                position - 1]  # Set the value of the positioned element to the value of the previous element. We are doing this to make space for the new (inserted item)
            position = position - 1  # Move position to one back

        # Set the value of the final positioned item to be the value of the current_element
        list_of_numbers[position] = current_element

    return list_of_numbers


def sort_test(list_of_numbers):
    print(list_of_numbers)
    print(insert_sort(list_of_numbers))
    print("----------------")


sort_test([3, 22, 14, 434, 501, 11, 9, 1230, 304, 123, 5412, 381923, 302, -3, 1])
sort_test([43, 12, 7, 9, 22, 1, 104])
sort_test([100, 0, 0, -20, 30, -5])
sort_test([28, 4, 17, 666, 1001, 52, 61, 30])


