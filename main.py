age = int(input("Yoshingizni kiriting: "))

if age <= 4 or age > 65:
 print("Chipta narxi bepul")
elif 5 <= age <= 12:
 print("15000 so'm") 
elif 13 <= age <= 65:
 print("20000 so'm")
else:
 print("Noma'lum yosh")


havo = int(input("Havo haroratini kiriting: "))

if havo <= 0: 
 print('Havo harorati juda sovuq')
elif havo > 30:
 print('Havo harorati juda issiq')
else:
 print('Havo harorati qulay')

baho = int(input("Bahoni kiriting: "))

if baho > 90:
 print("A'lo")
elif baho > 80:
  print('Yaxshi')
elif baho > 70:
    print('Qoniqarli')
else:
    print('Yomon')