numbers = [1,2,3]

#For Loop Method:
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)


#Optimized Method
new_list = [n + 1 for  n in numbers]

name = "Angela"

new_string = [letter for letter in name]
print("Works for Python Sequences like list, dict, string, tuple, range")

#Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
big_names = [name.upper() for name in names if len(name) > 5]
print(big_names)


#Dictionary Comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#Looping through a list
students_score = {name:random.randint(1,100) for name in names}
print(students_score)

#Looping through a dict
passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
print(passed_students)


#Iterating through a pandas DataFrame
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through rows od a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student =="Angela":
        print(row.score)

#or
# {new_key:new_value for (index,row) in df.iterrows()}