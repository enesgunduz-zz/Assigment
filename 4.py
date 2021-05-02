sayi = int(input("Please enter a number:"))
sayac = 0
for i in range (2,sayi//2):
    if sayi%i == 0:
       sayac =sayac+1
       if sayac>0 :
           break
if sayac>0:
    print(f" {sayi} is not a prime number")
else:
    print(f" {sayi} is a prime number")        
