with open("./Input/Names/invited_names.txt") as file:
    mylis = file.readlines()
for item in mylis:
    with open("./Input/Letters/starting_letter.txt") as file:
        mycontent = file.read()
    content = item.strip()
    mycontent = mycontent.replace("[name]", content)
    with open(f"./Output/ReadyToSend/letter_for_{content}.txt", "w") as file:
        file.write(mycontent)
