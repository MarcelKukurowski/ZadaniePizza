import math
import sys

print(sys.argv)

price_List = []

m1 = (math.pow(((int(sys.argv[3]))/2),2)*math.pi)
if(len(sys.argv)>5):
    m2 = (math.pow(((int(sys.argv[5]))/2),2)*math.pi)
if(len(sys.argv)>7):    
    m3 = (math.pow(((int(sys.argv[7]))/2),2)*math.pi)

# Nazwa pizzeri 1, nazwa pizzy 2, rozmiar pizzy 3, cena pizzy 4
print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[3]}cm, cena: {sys.argv[4]}zł")
if(len(sys.argv)>5):
    print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[5]}cm, cena: {sys.argv[6]}zł")
if(len(sys.argv)>7):
    print(f"Restauracja: {sys.argv[1]}, pizza: {sys.argv[2]}, rozmiar: {sys.argv[7]}cm, cena: {sys.argv[8]}zł")

p1 = float(sys.argv[4])/m1
if len(sys.argv)>5 and len(sys.argv)<8:
    p2 = float(sys.argv[6])/m2
    if(p1 > p2):
        print(f"Najbardziej opłaca się kupić: {sys.argv[5]}cm")
    else:
        print(f"Najbardziej opłaca się kupić: {sys.argv[3]}cm")
if(len(sys.argv)>7):
    p2 = float(sys.argv[6])/m2
    p3 = float(sys.argv[8])/m3
    price_list = {p1,p2,p3}
    if(min(price_list) == p1):
        print(f"Najbardziej opłaca się kupić: {sys.argv[3]}cm")
    elif(min(price_list) == p2):
        print(f"Najbardziej opłaca się kupić: {sys.argv[5]}cm")
    else:
        print(f"Najbardziej opłaca się kupić: {sys.argv[7]}cm")

