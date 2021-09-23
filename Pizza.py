import math
import sys

print(sys.argv)

surface_area_1 = math.pow(int(sys.argv[3])/2, 2) * math.pi
if(len(sys.argv)>5):
    surface_area_2 = math.pow(int(sys.argv[5])/2,2) * math.pi
if(len(sys.argv)>7):    
    surface_area_3 = math.pow(int(sys.argv[7])/2,2) * math.pi

# Nazwa pizzeri 1, nazwa pizzy 2, rozmiar pizzy 3, cena pizzy 4
print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[3]}cm, cena: {sys.argv[4]}zł")
if len(sys.argv)>5:
    print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[5]}cm, cena: {sys.argv[6]}zł")
if len(sys.argv)>7:
    print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[7]}cm, cena: {sys.argv[8]}zł")

price_1 = float(sys.argv[4])/surface_area_1
if len(sys.argv)>5 and len(sys.argv)<8:
    price_2 = float(sys.argv[6])/surface_area_2
    if price_1 > price_2:
        print(f"Najbardziej opłaca się kupić: {sys.argv[5]}cm")
    else:
        print(f"Najbardziej opłaca się kupić: {sys.argv[3]}cm")
if len(sys.argv)>7:
    price_2 = float(sys.argv[6])/surface_area_2
    price_3 = float(sys.argv[8])/surface_area_3
    price_list = {price_1, price_2, price_3}
    if min(price_list) == price_1:
        print(f"Najbardziej opłaca się kupić: {sys.argv[3]}cm")
    elif min(price_list) == price_2:
        print(f"Najbardziej opłaca się kupić: {sys.argv[5]}cm")
    else:
        print(f"Najbardziej opłaca się kupić: {sys.argv[7]}cm")

