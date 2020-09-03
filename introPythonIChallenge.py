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

dictionary = {0:"This", 1:'is', 2:"a", 3:"dictionary", "wow":(4, 2), 24:("WOW!"), ("this is a 'set' key!"):"this value says woah!", "key":"value (pair <3)"}
print("This is a dictionary:", dictionary)

# Access the items of a dictionary

accessed_dict_item_0 = dictionary[0]
print("This is the first item accessed from the dictionary:", accessed_dict_item_0)

# Change the value of a specific item in a dictionary



# Print all key names in a dictionary, one by one
# Print all values in a dictionary, one by one
# Use the values() function to return values of a dictionary
# Loop through both keys and values, by using the items() function
# Check if a key exists
# Get the length of a dictionary
# Add an item to a dictionary
# Remove an item from a dictionary
# Empty a dictionary
# Use the dict() constructor to create a dictionary


# Tuples

# Create a tuple
# Access tuple items
# Change tuple values
# Loop through a tuple
# Check if a tuple item exists
# Get the length of a tuple
# Delete a tuple
# Use the tuple() constructor to create a tuple


# Sets

# Create a set
# Loop through a set
# Check if an item exists
# Add an item to a set
# Add multiple items to a set
# Get the length of a set
# Remove an item in a set
# Remove an item in a set by using the discard() method
# Remove the last item in a set by using the pop() method
# Empty a set
# Delete a set
# Use the set() constructor to create a set
