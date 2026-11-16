def unique_list(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list

my_list = [1, 2, 3, 2, 4, 1, 5]

result = unique_list(my_list)

print("Original list:", my_list)
print("List with distinct elements:", result)
