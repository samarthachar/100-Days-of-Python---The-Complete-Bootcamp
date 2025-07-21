import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = []
fur_color.append(len(data[data["Primary Fur Color"] =="Gray"]))
fur_color.append(len(data[data["Primary Fur Color"] =="Cinnamon"]))
fur_color.append(len(data[data["Primary Fur Color"] =="Black"]))

template = {
    "Fur Color": ["grey","red","black"],
    "Count": fur_color
}

frame = pandas.DataFrame(template)
frame.to_csv("squirrel_count.csv")