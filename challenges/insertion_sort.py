
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


# Do not change code below this line
list_of_numbers = [45, 16, 33, 4, 551, 76, 20]
print(list_of_numbers)
print(insert_sort(list_of_numbers))
