###############################
###   Mehmet Kahya - 2024   ###
###      Kelime oyunu       ###
##          Python          ###
###############################

# Kelimeler TDK'nin sitesinden alınmıştır. 
# Kelimeler.txt dosyası içerisinde 41342 adet kelime bulunmaktadır.

import random 
import time
import os
from colorama import Fore

print(Fore.BLUE + r"""
###############################
###   Mehmet Kahya - 2024   ###
###      Kelime oyunu       ###
##          Python          ###
###############################

# Kelimeler TDK'nin sitesinden alınmıştır. 
# Kelimeler.txt dosyası içerisinde 41342 adet kelime bulunmaktadır.
""" + Fore.RESET)
      



if os.path.isfile("kelimeler.txt"):
    with open("kelimeler.txt", "r") as dosya:
        data = dosya.readlines()
        secim = random.choice(data).strip().lower()  
else:
    print("dosya bulunamadı")
    exit()

print("\n- en fazla 15 hakkın var!\n- 1 tane Joker hakkın var! [Jokeri kullanmak için joker yaziniz]")

adam = [r"""
   +---+
   |   |
       |
       |
       |
 1     |
--------""", r"""
   +---+
   |   |
   O   |
       |
       |
 2     |
--------""", r"""
   +---+
   |   |
   O   |
   |   |
       |
 3     |
--------""", r"""
   +---+
   |   |
   O   |
  /|   |
       |
 4     |
--------""", r"""
   +---+
   |   |
   O   |
  /|   |
  /    |
 5     |
--------""", r"""
   +---+
   |   |
   O   |
  /|   |
  / \  |
 6     |
--------""", r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
 7     |
--------""", r"""
   +---+
       |
   O   |
  /|\  |
  / \  |
 8     |
--------""", r"""
   +---+
       |
       |
   O   |
  /|\  |
9 / \  |
--------""", r"""
   +---+
       |
       |
   O   |
  /|\  |
10/ \  |
--------""", r"""
    +---+
        |
        |
   O    |
  /|\   |
11      |
--------""", r"""
   +---+
       |
       |  
       |
    O  |
12 /|\ |
--------""", r"""
   +---+
       |
       |  
       |
    O  |
13 /|  |
--------""", r"""
   +---+
       |
       |  
       |
   O   |
14  |  |
--------""", r"""
   +---+
       |
       |  
       |
       |
15  O  |
--------"""]
def kontrol(secim,harf):
  dizi = []
  sayac = 0

  for i in secim:
    if i == harf:
      dizi.append(sayac)
    sayac += 1 

  if len(dizi) == 0:
    return False
  else:
    return dizi  

for i in range(len(secim)):
  print("_ ",end="")
print("")

hak = 15
hata = 0
tahmin_edilen = []
joker_used = False

while hak > 0:
  tahmin = input("Tahmin et: ").lower()  # Convert input to lower-case
  if tahmin == "joker" and not joker_used:
    joker_used = True
    kelime = list(secim)
    while True:
      joker_index = random.randint(0, len(kelime) - 1)
      if joker_index not in tahmin_edilen:
        tahmin_edilen.append(joker_index)
        print("Jokerin: {}".format(kelime[joker_index]))
        print("Joker hakkın bitti.")
        break
    continue

  ans = kontrol(secim,tahmin)

  if ans == False:
    print(adam[hata])
    hata += 1
    hak -= 1
    print("Yapılan Hata: {}".format(hata))
    print("Kalan Hak: {}".format(hak))

    if hata == 15:
      print("\nKAYBETTİN!")
      print("Kelime: {}".format(secim))
      print("5 saniye sonra kod otomatik olarak kapanıyor..")
      time.sleep(5)
      print("kapandı")
      exit()

  else:
    for i in ans:
      tahmin_edilen.append(i)

    for i in range(len(secim)):
        if i in tahmin_edilen:
            print(secim[i] + " ",end="")
        else:
          print("_ ",end="")
    print("")

  if len(tahmin_edilen) == len(secim):
      print("KAZANDIN!")
      print("5 saniye sonra kod otomatik olarak kapanıyor..")
      time.sleep(5)
      print("kapandı")
      exit()