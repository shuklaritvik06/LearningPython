import pandas
data = pandas.read_csv("Codes.csv")
mydict = {
    row.letter: row.code for index, row in data.iterrows()
}
name = input("Enter the word: ")
result = [mydict[item.upper()] for item in name]
print(result)
