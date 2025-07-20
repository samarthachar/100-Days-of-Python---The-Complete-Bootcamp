# #Open in read mode('r')
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# #Opening in write mode(Deletes all previous data)
# with open("my_file.txt",mode="w") as file:
#     file.write("New text.")
#
#
# # Opening a file in Append mode
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
#
# # Creating a new file
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")

with open("../../../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)