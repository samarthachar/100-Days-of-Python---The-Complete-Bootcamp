# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
data = pandas.read_csv("weather_Data.csv")
# print(data["temp"])

temp_list = data["temp"].to_list()
# print(data.condition)

#Get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "monday"]
print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F= monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_Data.csv")
print("hii")