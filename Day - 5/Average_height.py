# Average Height

student_heights = input(
    "Input a list of student heights ").split()  # Split on space
mylis = list(map(int, student_heights))
average = 0
for i in mylis:
    average += i
print(round(average/len(mylis)))
