def even_numbers():
    even_list = []

    for i in range(100, 151):
        if i % 2 == 0:
            even_list.append(i)

    return even_list

result = even_numbers()

print("Even numbers between 100 and 150:")
print(result)
