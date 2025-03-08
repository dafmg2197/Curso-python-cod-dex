# Programa corregido con chatgpt

# Solicitar datos del usuario
wEarth = float(input("Please type your weight on Earth: "))
planetNumber = int(input("Choose the planet number you're visiting (1-7): "))

# Diccionario con los factores de conversión
planetWeights = {
    1: ("Mercury", 0.38),
    2: ("Venus", 0.91),
    3: ("Mars", 0.38),
    4: ("Jupiter", 2.53),
    5: ("Saturn", 1.07),
    6: ("Uranus", 0.89),
    7: ("Neptune", 1.14)
}

# Verificar si el número es válido
if planetNumber in planetWeights:
    planetName, gravityFactor = planetWeights[planetNumber]
    weight = wEarth * gravityFactor
    print(f"Your weight on {planetName} is: {weight:.2f}")
else:
    print("Invalid planet number, try again.")
