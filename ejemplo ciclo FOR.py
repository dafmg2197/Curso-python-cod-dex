### for loops

def main ():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
    Print(write_letter(name, "Princess Peach"))

### Al usar 'name', esta palabra se refiere a cada nombre listado, permitiendo 
### recorrer el diccionario y, así mismo, 'imprimirlo' en la misma posición de 'receiver'

### Permite 'iterar' o 'recorrer' los nombres listados en el 'diccionario'; 
### por lo que el ciclo finalizará cuando ya no haya nombres en él.


def write_letter(receiver, sender):
    return f"""
    +------------------------------------------------+
      Dear {receiver},

      You're cordially invited to a ball at Peach's
      Castle this evening, 7:00pm.

       Sincerely,
      {sender}
    +------------------------------------------------+
    """
main ()
### Este será el contenido que llevará la 'carta de invitación' que Peach 
### le hace a cada personaje. Reciever está en la misma posición en el listado
### que los nombres del 'diccionario', y 'Princess Peach' en la misma posición
### que Sender, por eso es que al momento de ejecutar el programa, se concatenan
### los nombres con el contenido de la carta.
