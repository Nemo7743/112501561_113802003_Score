grades = input().split()

maxPeople = 0
minPeople = 100

for i in grades:
  if(int(i)>maxPeople):maxPeople = int(i)
  elif(int(i)<minPeople):minPeople = int(i)
print(maxPeople, minPeople)


grades_int = [int(item) for item in grades]
average = sum(grades_int) / len(grades_int)

print(average)