# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#INdexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#Murphy's law: Everything that can go wrong, will eventually go wrong

# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"Key":"Value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
