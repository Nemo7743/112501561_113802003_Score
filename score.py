#print("請輸入一串成績(以空格分隔)：", end="")
grades = input("請輸入一串成績(以空格分隔)：").split()

failedPeople = 0
maxPeople = 0
minPeople = 100

for i in grades:
  if(int(i)<60):failedPeople += 1
  if(int(i)>maxPeople):maxPeople = int(i)
  elif(int(i)<minPeople):minPeople = int(i)
print("不及格數量：", failedPeople)
print("最大值：", maxPeople)
print("最小值：", minPeople)


grades_int = [int(item) for item in grades]
average = sum(grades_int) / len(grades_int)

print("平均值：", average)