# This function is supposed to add an item to a list, but it produces unexpected results. Find the bug.

def add_to_list(item, my_list=None):

    if my_list is None:
        my_list = []

    my_list.append(item)
    return my_list

print(add_to_list(2))
print(add_to_list(2))

list1 = ["1"]


list1 = add_to_list( "s", list1)
print(list1)

list1 = add_to_list("h", list1)
print(list1)

list1 = add_to_list("hello world", list1)
print(list1)