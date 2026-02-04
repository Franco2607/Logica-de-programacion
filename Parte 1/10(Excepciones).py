try:    
    print(10/0)
    print([1,2,3,4,5][4])
except Exception as e:
    print(f"El error es: {e} (tipo: {type(e).__name__})")


while True:
    try:
        num = int(input("Ingrese un numero: "))
        print(f"El numero es: {num}")
        break
    except ValueError:
        print("El numero debe ser un entero (no texto ni decimal).")
    except Exception as e:
        print(f"El error es: {e}")
  