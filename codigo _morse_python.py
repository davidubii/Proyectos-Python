def codigo_morse(palabra):
  alfabeto = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
  }
  resultado = ""
  for i in range (0, len(palabra)):
      resultado = resultado + alfabeto[palabra[i].upper()]+"/"
  print("la palabra",palabra, "en codigo morse es: ", resultado)
  print(resultado)

palabra_1 = "hija"
codigo_morse(palabra_1)