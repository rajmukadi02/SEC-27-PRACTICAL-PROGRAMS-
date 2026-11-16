def check_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

n = int(input("Enter a number: "))
start = int(input("Enter range starting number: "))
end = int(input("Enter range ending number: "))

if check_range(n, start, end):
    print("Number is within the range.")
else:
    print("Number is outside the range.")
