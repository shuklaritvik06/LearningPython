from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Batchmates", ["Anant", "Rahul", "Amit"])
table.add_column("Branch", ["CSE", "CSE", "ECE"])
table.align = "l"
print(table)
