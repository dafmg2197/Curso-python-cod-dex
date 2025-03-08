#En este caso, el metodo range(6) genera una lista de 0 a 5, es decir, 6 elementos en total.
#Por lo tanto, el bucle for se ejecutara 6 veces, imprimiendo los valores de i desde 0 hasta 5.

#Range siempre retorna una secuencia de numeros, comenzando desde 0 por defecto,
#y se incrementa en 1 (por defecto), y termina en un numero especificado.

for i in range(6):
  print(i)


#Para imprimir/escribir 100 veces lo mismo, se puede hacer de la siguiente manera:
for i in range(100):
  print("Hola Mundo") 
  
#Se mostrará lo que se describé en el interior del print, la i solo es 
#para que se repita 100 veces lo mismo