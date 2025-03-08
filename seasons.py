month = int(input('Please type a number between 1 and 12: '))

if month in [1, 2, 3]:
    print('Winter 🌨️')
elif month in [4, 5, 6]:
    print('Spring 🌱')
elif month in [7, 8, 9]:
    print('Summer 🌻')
elif month in [10, 11, 12]:
    print('Autumn 🍂')
else:
    print('Invalid')
# The user is asked to input a number between 1 and 12.
# La función 'in' permite comparar si un valor se encuentra en una lista.
# Si el valor ingresado por el usuario se encuentra en la lista, se imprime la estación correspondiente.
