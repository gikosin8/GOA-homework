A = input("Let's see if you passed the course, are you ready?: ")

point = 70

if A == ('yes'):
    B = int(input("Well, tell me how many points you got: "))
    if B > point:
       print("Congratulations, you have passed the course")
    else:
       print("Sorry, you could not pass the course")
else:
  print("Come back when you're ready")