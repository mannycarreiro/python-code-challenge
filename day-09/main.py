# Best Pratice to cap off the dictionary by leaving a comma "," at the end
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# GET AN ITEM FROM DICTIONARY
#print(programming_dictionary["Bug"])  # 'BUG IS THE KEY'

# ADDING/MODIFYING ITEM ON DICTIONARY
programming_dictionary["Loop"] = "The action of doing something over and over again"
#print(programming_dictionary)

# CREATE AN EMPTY DICTIONARY
#programming_dictionary_2 = {}

# WIPE AN ENTIRE DICTIONARY
#programming_dictionary_2 = {}

# LOOP TROUGH A DICTIONARY TO GET KEY
for key in programming_dictionary:
    print(key)

# LOOP TROUGH A DICTIONARY TO GET KEY AND VALUE
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])