# Student Score

student_scores = input("Input a list of student scores: ").split()
mylis = list(map(int, student_scores))
print(mylis)
mylis.sort()
print(student_scores)
a = len(student_scores)-1
maxi = student_scores[a]
for i in student_scores:
    if(i > maxi):
        maxi = i
    else:
        pass
print(maxi)
