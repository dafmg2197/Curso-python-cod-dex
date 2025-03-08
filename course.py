#Now i'm using if/elif/else and comparisson symbols.

#First Question
q1 = int(input("Type de number to answer: Do you like 1)Dawn or 2)Dusk?:  "))
if q1 == 1:
  print("Gryffindor and Ravenclaw both get a +1.")
elif q1 == 2:
  print("Hufflepuff and Slytherin both get a +1.")
else :
  print('Wrong input.')

#Second Question
q2 = int(input("When I’m dead, I want people to remember me as: 1)The Good, 2)The Great, 3)The Wise, 4)The Bold: "))
if q2 == 1:
  print('Hufflepuff +2')
elif q2 == 2:
  print('Slytherin +2')
elif q2 == 3:
  print('Ravenclaw +2')
elif q2 == 4:
  print('Gryffindor +2')
else :
  print ("Wrong input")

#Question 3

q3 = int(input("Which kind of instrument most pleases your ear? 1)The violin, 2)The trumpet, 3)The piano, 4)The drum:  "))
if q3 == 1:
  print('Slytherin +4')
elif q3 == 2:
  print('Hufflepuff +4')
elif q3 == 3:
  print('Ravenclaw +4')
elif q3 == 4:
  print('Gryffindor +4')
else :
  print("Wrong input")