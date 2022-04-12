import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])  Series
# print(data) Data-Frame
# print(data["temp"].max())
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()].temp)
# fahr = (9/5)*(data[data.day == "Monday"].temp)+32
# print(fahr)

# Create data-frame from scratch
mydict = {
    "student name": ["Ramesh", "Suresh", "Rajesh"],
    "roll_num": [12, 13, 4]
}
mydata = pandas.DataFrame(mydict)
mydata.to_csv("mydata.csv")
