# Treasure Map

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
a = int(position[1])-1
b = int(position[0])-1
map[a][b] = "X"
row1 = map[0]
row2 = map[1]
row3 = map[2]
print(f"{row1}\n{row2}\n{row3}")
