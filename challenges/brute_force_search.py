def search(numbers, query_number):
    found_number = False

    for number in numbers:
        if number == query_number:
            found_number = True
            break

    return found_number


# Don't change code below this line
query_number = 3
numbers = [40, 512, 31, 3, 50, 610, 2]
print(search(numbers, query_number))