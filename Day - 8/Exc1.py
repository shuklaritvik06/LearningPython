# Prob1

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(test_h,test_w,coverage):
  number_of_cans = (test_w*test_h)/coverage
  print(math.ceil(number_of_cans))
paint_calc(test_h,test_w,coverage)
