# new_Dict = {
#     new_key: new_value for key, value in dict.items() if test
# }

import random
student_name = ['Ritvik', 'Mahendra', 'Rajesh']
student_score = {
    key: random.randint(50, 99) for key in student_name
}
print(student_score)
passed_students = {
    key: 'Passed' for key, value in student_score.items() if value > 60
}
print(passed_students)
