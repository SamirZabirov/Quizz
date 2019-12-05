import csv
score = 0 
with open('questions.csv', newline='') as questions:
  reader = csv.reader(questions, delimiter=",")
  for row in reader:
    print(row[0])
    print(row[1], row[2], row[3])
    ans = input("Напишите вариант ответа(a, b, c): ")

    if ans == 'a':
      if row[1] == row[4]:
        print("Верно!")
        score += 5 
      else:
        print("Не верно!")
    elif ans == 'b':
      if row[2] == row[4]:
        print("Верно!")
        score += 5
      else:
        print("Не верно")
    elif ans == 'c':
      if row[3] == row[4]:
        print("Верно")
      else:
        print("Не верно")
    else:
      print("Такого варианта ответа не существует!")

if score == 100:
  print("Ваша оценка - A")
elif score >= 95:
  print("Ваша оценка - A")
elif score >= 90:
  print("Ваша оценка - B+")
elif score >= 85:
  print("Ваша оценка - B")
elif score >= 80:
  print("Ваша оценка - B-")
elif score >= 75:
  print("Ваша оценка - C+")
elif score >= 70:
  print("Ваша оценка - С")
elif score >= 65:
  print("Ваша оценка - C-")
elif score >= 60:
  print("Ваша оценка - D")
elif score < 60:
  print("Ваша оценка - F")                                                                 

