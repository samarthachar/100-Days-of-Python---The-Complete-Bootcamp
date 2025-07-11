# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")


# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? the loop is going to print "You got it" when i == 20
# 2. When is the function meant to print "You got it"? when i == 20
# 3. What are your assumptions about the value of i?i will never be == 20, as the loop iterates 19 times

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()