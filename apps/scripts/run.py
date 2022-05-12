#!/usr/bin/python

import os
from colorama import Fore

print(Fore.GREEN)
os.system("clear")
print('''   --- Muzik Listesi ---

[1] Gitar
[2] Lvbl c5 - 10 numara
[3] Ben fero - Ferhat Yilmaz
[4] Eminem - Godzilla
[5] Batuflex - Dalga
[6] Abra - Gimme Gimme
[7] Ezhel - Bul Beni
[8] Ibrahim Tatlises - Dua Lipa Dom Dom Kusu
[9] Cem Adrian - Mark Eliyahu Kul
[10] Eminem Criminal
[11] Sertab Erener - Gangster Paradise Vur Yuregim
''')


print(Fore.RED,end="")
music = input("Radyoda çalinacak muzik:")
frequency = input("Frekansi Giriniz (Varsayilan 90.6):")
if frequency == "":
    frequency = 90.6
    
if music == "1":
    music = "music/gitar.wav"
    

elif music == "2":
    music = "music/onnumara.wav"
    
elif music == "3":
    music = "music/benfero.wav"
    
elif music == "4":
    music = "music/eminem.wav"

elif music == "5":
    music = "music/dalga.wav"

elif music == "6":
    music = "music/gimme.wav"

elif music == "7":
    music = "music/bulbeni.wav"

elif music == "8":
    music = "music/domdom.wav"

elif music == "9":
    music = "music/kul.wav"

elif music == "10":
    music = "music/vuryuregim.wav"

elif music == "11":
    music = "music/criminal.wav"

else:
    print("Hatali Seçim Yaptiniz!")


os.system(f"sudo ./fm_transmitter {music} -f {str(frequency)}")