try:
  sayi = int(input("sayi girin: "))

  order = len(str(sayi))

  sum = 0

  temp = sayi
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10



  if sayi == sum:
     print(sayi,"is an Armstrong number")
  elif sayi < 0:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
  else:
     print(sayi,"is not an Armstrong number")

except ValueError:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")