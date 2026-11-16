def multiply_list(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

my_list = [2, 3, 4, 5]
answer = multiply_list(my_list)

print("List:", my_list)
print("Multiplication of all numbers:", answer)
