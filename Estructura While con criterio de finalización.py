def main():
  while True:
      entrada = input("Escribe algo: ")
      if entrada.lower() == "quit":
          print("¡Adiós!")
          break
      print(entrada)

if __name__ == "__main__":
  main()