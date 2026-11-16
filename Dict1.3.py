my_dict = {
    "name": "Raj",
    "age": 18,
    "city": "Mumbai",
    "course": "Data Science"
}
my_dict.pop("age")

print("Dictionary after removing key:", my_dict)

print("All key-value pairs:")

for key, value in my_dict.items():
    print(key, ":", value)

search_key = "name"

if search_key in my_dict:
    print(search_key, "exists in the dictionary")
else:
    print(search_key, "does not exist in the dictionary")
