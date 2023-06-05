# I am going to extract data from a Column of Central_Park CSV file so that I can count how many entries
# of Black, gray and cinnamon color are there.
# this task will be done using Pandas Library and after extracting the data I will add it in a New CSV
# file for our record and later use.

import pandas

data = pandas.read_csv("Central_Park_Squirrel_Census_Data.csv")
black = len(data[data["Primary Fur Color"] == "Black"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dic = {
    "Primary Fur Color ": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, Cinnamon, black]
}
data_framework = pandas.DataFrame(data_dic)
data_framework.to_csv("Count.csv")

new_file_data = pandas.read_csv("Count.csv")
print(new_file_data)
