import random

cinema_Name = input("Sinema adını gir: ")
movie_Name = input("Film adını gir: ")
customer_Name = input("Müşterinin adını gir: ")

price_Ticket = float(input("Bilet ücretini gir: "))
amount = int(input("Kaç adet: "))

money = float(input("Müşterinin verdiği ücreti gir: "))

total_Price = price_Ticket * amount
change = money - total_Price

receipt_Number = random.randint(10000,99999)

print("\n===================")
print("Sinema",cinema_Name)
print("Bilet No: ",receipt_Number)
print("===================")

print(movie_Name)
print("Sayın",customer_Name)
print("Bilet Fiyatı",price_Ticket)
print("Bilet Adeti",amount)


print("\n-----------------------")
print("TOPLAM: ",total_Price)
print("ALINAN PARA: ",money)
print("PARA ÜSTÜ: ",change)
print("-----------------------")

print("İYİ SEYİRLER!")