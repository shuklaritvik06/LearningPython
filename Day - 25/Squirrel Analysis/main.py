import pandas
data = pandas.read_csv("Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
mydata = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "count": [grey_squirrel, cinnamon_squirrel, black_squirrel]
}
mydataframe = pandas.DataFrame(mydata)
mydataframe.to_csv("squirrelcount.csv")
