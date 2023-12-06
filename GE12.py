#Raise error in a name using exceptional handling.
def valid_name():
    try:
        
        name = input("enter name ")
        if not name.isalpha():
            raise ValueError(" invalid name")
        return name
    except ValueError as Error:
        print(f"error{Error}")
        return valid_name()

my_name = valid_name()
print("My name is ", my_name)
    
