def contains_integer(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False

# Example usage
test_string = "Hello123World"

if contains_integer(test_string):
    print("The string contains at least one integer.")
else:
    print("The string does not contain any integers.")
    #helo