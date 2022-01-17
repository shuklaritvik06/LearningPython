# Sum of even Numbers in a given range

total = 0
for i in range(1,101):
  if(i%2==0):
    total+=i
print(total)