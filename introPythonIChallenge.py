#introPythonIChallenge.py



# Challenge

#Complete the following either in a python script file or directly in the python interpreter:


# Lists

# Create a list

this_is_a_list = ["this", "is", "a", "list", "I", "see", "brackets", 100, 100, "100", 'This is a list, I see brackets!', 1000]
print(f"This is a list:", this_is_a_list)


# Access list items


accessed_list_item = this_is_a_list[0]
print(f"First accessed list item:", accessed_list_item)

accessed_list_item_end = this_is_a_list[-1]
print(f"Last accessed list item:", accessed_list_item_end)


# Change the value of a list item

this_is_a_list[7] = 1
see_changed_value_of_list = this_is_a_list[7]
print(f"Changed value of list item:", see_changed_value_of_list)


# Loop through a list

for all_the_goodness in this_is_a_list:
    print("This is a loop through a list:", all_the_goodness)


# Check if a list item exists

check_if_list_item_exists = 1 in this_is_a_list
print(f"Check if list item exists:", check_if_list_item_exists)
print(f"Check if list item exists with print:", this_is_a_list[6], "is in index 6 of the list")


# Get the length of a list

length_of_the_list = len(this_is_a_list)
print(f"This is the length of the list:", length_of_the_list)


# Add an item to the end of a list - Can append a string to a list, or concanenate, but insert is for numbers

add_an_item_to_the_end_of_a_list = this_is_a_list + ["this is the end of the list"]
print(f"Added and item to the end of this list:", add_an_item_to_the_end_of_a_list)


# Add an item at a specified index

this_is_a_list.insert(0, 0)
print("Added a 0 to the 0 index of this list:", this_is_a_list)


# Remove an item

this_is_a_list.remove(100)
print("Removed one 100 from this list:",this_is_a_list)


# Remove an item at a specified index

this_is_a_list.pop(0)
print("Removed (popped) the 0 from the 0 index of this list:",this_is_a_list)


# Empty a list

this_is_a_list.clear()
print("This is an empty list after clear:", this_is_a_list)


# Use the list() constructor to make a list

string = "Say what you need to say"
string = list(string)
print("Use the list() constructor to make a list:", type(string), string)


# Dictionaries

# Create a dictionary

dictionary = {0:"This", 1:'is', 2:"a", 3:"dictionary", "wow":(4, 2), 24:("WOW!"), "key":"value (pair <3)"}
print("This is a dictionary:", dictionary)


# Access the items of a dictionary

accessed_dict_item_0 = dictionary[0]
print("This is the first item accessed from the dictionary:", accessed_dict_item_0)


# Change the value of a specific item in a dictionary

dictionary["wow"] = "not so wow"
print("Changed value of a specific item in dictionary:", dictionary["wow"])


# Print all key names in a dictionary, one by one

for k,v in dictionary.items():
    print("All key names in a dictionary, one by one:", k)


# Print all values in a dictionary, one by one

for k,v in dictionary.items():
    print("All vales in a dictionary, one by one:", v)


# Use the values() function to return values of a dictionary

print("Use the value() function to return values of a dictionary:", dictionary.values())


# Loop through both keys and values, by using the items() function

print("Loop through both the keys and values, by using the items() function:", dictionary.items())


# Check if a key exists

def key_check(dictionary, key):

    if key in dictionary.keys():
        print(f'Key "{key}" exists:', dictionary[key])
    else:
        print(f'Key "{key}" does not exist.')

key_check(dictionary, "doesn't exist")
key_check(dictionary, "key")


# Get the length of a dictionary

print("Get the length of a dictionary with len(dictionary), which is:", len(dictionary))


# Add an item to a dictionary

dictionary['new key'] = "new value"

print("Add an item to a dictionary with dictionary['key'] = 'value', like so: dictionary['new key'] = 'new value'", dictionary)


# Remove an item from a dictionary

del dictionary['new key']

print("Remove an item from a dictionary with: 'del dictionary['key']', like so:", dictionary)

# Empty a dictionary

dictionary.clear()

print("Empty a dictionary with 'dictionary.clear(), like so:", dictionary)


# Use the dict() constructor to create a dictionary

dict_construct = dict(new='?', dict='!', witH= 'dict() constructor')

print(dict_construct)


# Tuples

# Create a tuple

issatuple = ("create", "a", "tuple", "with", "(", "and", ")", "around", "data")

print(issatuple)


# Access tuple items

print("Access tuple items like this: 'issatuple[8]':", issatuple[8]) 


# Change tuple values

print("Once a tuple is created you cannot change its values! However, change it to a list :)")

change = list(issatuple)
change[0] = 'change a tuple by making it a list and then turn it back into a tuple :D'
issatuple = tuple(change)

print(issatuple)


# Loop through a tuple

for s in issatuple:
    print("Loop through a tuple:", s)


# Check if a tuple item exists

def tuple_check(toople, item):

    if item in toople:
        print(f'Item "{item}" exists in tuple.')
    else:
        print(f'Item "{item}" does not exist in tuple.')

tuple_check(issatuple, "doesn't exist")
tuple_check(issatuple, "data")


# Get the length of a tuple

print("Get the length of a tuple with 'len(tuplename)', like so:", len(issatuple))


# Delete a tuple

del issatuple

print("Delete a tuple with 'del tuplename' like so: well... now it's deleted")


# Use the tuple() constructor to create a tuple

tuple_construct = tuple('new tuple with tuple() constructor')

print(tuple_construct)


# Sets

# Create a set

issaset = {"make", "a", "new", "set", "with", "{", "and", "}", "around", "data"}
print(issaset)


# Loop through a set

for s in issaset:
    print("Loop through a set:", s)


# Check if an item exists

def set_check(sett, item):

    if item in sett:
        print(f'Item "{item}" exists in set.')
    else:
        print(f'Item "{item}" does not exist in set.')

set_check(issaset, "doesn't exist")
set_check(issaset, "data")


# Add an item to a set

issaset.add('added item')

print("Add an item to a set with setname.add('added item'):", issaset)


# Add multiple items to a set

issaset.update(['multiple items', 'added'])

print("Add multiple items to a set with setname.update(['multiple items', 'added']):", issaset)


# Get the length of a set

print("Get the length of a set with len(setname):", len(issaset))


# Remove an item in a set

issaset.remove('and')

print("Remove an item in a set with setname.remove(item):", issaset, "(removed 'and')")


# Remove an item in a set by using the discard() method

issaset.discard('added')

print("Remove an item in a set with setname.discard(item):", issaset, "(removed 'added')")


# Remove the last item in a set by using the pop() method

issaset.pop()

print("Remove the last item in a set by using setname.pop():", issaset)


# Empty a set

print("Empty a set with setname.clear():", issaset.clear(), "(the set is empty)")


# Delete a set

del issaset

print("Delete a set with 'del setname': the set is now deleted")


# Use the set() constructor to create a set

set_construct = set('new set with set() constructor')

print(set_construct)
