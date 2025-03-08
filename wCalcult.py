#Código hecho por mi c : David Martínez.

# Write code below 💖

wEarth = float(input('Please type your weight on Earth: '))
planetNumber = int(input("Choose the planet number you're visiting: "))

#el ciclo lleva consigo el método. Por eso la operación lógica se hace en su interior.
if planetNumber == 1:
  mercuryWeight = wEarth * 0.38
  print(f"Your weight on Mercury is: {mercuryWeight:.2f}")

elif planetNumber == 2:
  venusWeight = wEarth * 0.91
  print(f"Your weight on Venus is: {venusWeight:.2f}")

elif planetNumber == 3:
  marsWeight = wEarth * 0.38
  print ("your weight on Mars is: " + str(marsWeight))

elif planetNumber == 4:
  jupiterWeight = wEarth * 2.53
  print ("your weight on Jupiter is: " + str(jupiterWeight))

elif planetNumber == 5:
  saturnWeight = wEarth * 1.07
  print ("your weight on Saturn is: " + str(saturnWeight))

elif planetNumber == 6:
  uranusWeight = wEarth * 0.89
  print ("your weight on Uranus is: " + str(uranusWeight))
  
elif planetNumber == 7:
  neptuneWeight = wEarth * 1.14
  print ("your weight on Neptune is: " + str(neptuneWeight))
else:
  print ('Invalid planet number, try again')
