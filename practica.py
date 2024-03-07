# problema 1
fecha_hoy = input("escribe la fecha de hoy: ")
cumpleaños = input("Fecha de tu cumpleaños: ")

if fecha_hoy == cumpleaños:
 print(("es tu cumpeaños"))

elif fecha_hoy < cumpleaños:
  print(("no es tu cumpleaños"))


# problema 2
numero_1 = input("Ingresa un numero : ")
numero_2 = input("Ingresa un segundo numero : ")
if numero_1 > numero_2:
  resultado1 = numero_1 + 2
  print("es igual")
elif numero_1 < numero_2:
  print("es igual")
  resultado1 = numero_1 - 2 


# problema 3
cp = int(input("Ingrese su código postal: "))
if cp <= 50030:
    print("tu codigo postal estás dentro del rango de entrega")
elif 50000 <= cp:
    print("tu código postal no está dentro del rango de entrega 😢")