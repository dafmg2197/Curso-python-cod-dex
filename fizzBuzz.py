
for index in range(1, 101):#bucle que recorre los números del 1 al 100.
    divisible_by_three = index % 3 == 0 #comprueba si el número es divisible por 3.
    divisible_by_five = index % 5 == 0 #comprueba si el número es divisible por 5.

    if divisible_by_three and divisible_by_five: #si el número es divisible por 3 y por 5.
        print("fizzbuzz") 
    elif divisible_by_three:#si el número es divisible por 3.
        print("fizz")
    elif divisible_by_five:
        print("buzz")
    else:
        print(index) #si el número no es divisible ni por 3 ni por 5, imprime el número.
