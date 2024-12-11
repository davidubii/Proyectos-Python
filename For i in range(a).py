def main():
  numero = int(input("Da un número: "))
  suma = sum(range(numero))  # Suma de todos los números desde 0 hasta (n-1)
  print("La suma fue:", suma)

if __name__ == "__main__":
  main()