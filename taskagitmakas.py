#taş kağıt makas oyunu, mustafa buyukdereli 2022

#Kağıt taşı sarar, makas kağıdı keser ve taş makası ezer!

import random

#oyunda seçenekler

el = ["taş", "kağıt", "makas"]

tas = el[0]

kagit = el[1]

makas = el[2]

#bilgisayarın seçimi

bil_sec = random.choice(el)

#bizim seçim

print("taş, kağıt ya da makas seçiniz: \n")

siz_sec = input("Seçiminiz nedir: ")

siz_sec = siz_sec.lower()

#bizim seçimimizi yazdıralım

print(siz_sec)

#bilgisayarın seçimini yazdıralım

print(bil_sec)

#seçimlere göre kazananın belirlenmesi

if siz_sec == bil_sec:
    print("Beraberlik!")
    
if siz_sec == "taş" and bil_sec == kagit:
    print("Bilgisayar kazandı.")
    
if siz_sec == "taş" and bil_sec == makas:
    print("Siz kazandınız.")
    
if siz_sec == "kağıt" and bil_sec == tas:
    print("Siz kazandınız.")
    
if siz_sec == "kağıt" and bil_sec == makas:
    print("Bilgisayar kazandı.")
    
if siz_sec == "makas" and bil_sec == tas:
    print("Bilgisayar kazandı.")
    
if siz_sec == "makas" and bil_sec == kagit:
    print("Siz kazandınız.")
