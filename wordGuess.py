import random #importamos la librería random.
#random nos permite elegir un elemento aleatorio de una lista.
words = ['python', 'java', 'kotlin', 'javascript'] #banco de palabras para el juego.
word = random.choice(words) #elegimos una palabra al azar del banco de palabras para adivinar.
guessedWord = ['_'] * len(word) #creamos una lista con guiones bajos del mismo tamaño que la palabra a adivinar..
attempts = 10 #cantidad de intentos que tiene el jugador.
print('Welcome to the Word Guessing Game!') 

while attempts > 0: #bucle para que el juego continue hasta que se acaben los intentos.
  print('\nCurrent word: ' + ' '.join(guessedWord))#estado actual de la palabra con letras adivinadas y guiones bajos.

  guess = input('Guess a letter: ').lower()#instrucción para que el jugador ingrese una letra.

  if guess in word: # esto corrobora si la letra ingresada está en algún lado la palabra a adivinar.
    for i in range(len(word)): #bucle para recorrer cada letra de la palabra.
        if word[i] == guess:#si la letra en la posición i es igual a la letra adivinada.
            guessedWord[i] = guess #actualizamos la lista guessedWord en la posición i con la letra adivinada.
        print('Great guess!') #mensaje de acierto.
  else:
    attempts -= 1 #si la letra no está en la palabra, se resta un intento.
    print('Wrong guess! Attempts left: ' + str(attempts))#mensaje de error y muestra los intentos restantes.
  if '_' not in guessedWord:#si no hay guiones bajos en guessedWord, significa que se ha adivinado toda la palabra.
    print('\nCongratulations!! You guessed the word: ' + word)#mensaje de felicitación.
    break #salimos del bucle si se adivina la palabra.

if attempts == 0 and '_' in guessedWord:#si se acaban los intentos y aún hay guiones bajos en guessedWord, significa que no se adivinó la palabra.
  print('\nYou\'ve run out of attempts! The word was: ' + word) #mensaje de derrota y muestra la palabra correcta.