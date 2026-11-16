global_var = 10

def change_global():
    global global_var
    global_var = 20

print("Before changing:", global_var)

change_global()

print("After changing:", global_var)
