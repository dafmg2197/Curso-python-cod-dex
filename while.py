# iterar significa repetir
# Uso del ciclo while 
# Each lap is one iteration! A car will iterate over and over again until it can't do so anymore.

#while condition:
  # code inside

#la notación != significa diferente de, en este caso es diferente de 6. 
# Mientras el valor de guess sea diferente de 6, el ciclo se repetirá.

while guess != 6 and tries < 3:
  guess = int(input('Guess the number:  '))
  tries = tries + 1
# tries + 1 hace que el valor de tries aumente en 1 cada vez que se repita el ciclo,
# es decir, cada vez que el usuario ingrese un número equivocado.
if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')