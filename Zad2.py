'''
Napisz program który policzy ilość występowania liter w danym tekście i zwróci w postaci słownika:
{‘a’: 12, ‘b’: 12, ‘c’: 34, …, ‘z’: 34}
Tekst do analizy znajduje się w pliku text.txt
Zawartość z pliku tekstowego można wczytać do programu za pomocą funkcji input. Program uruchamiamy w taki sposób:
python main.py < text.txt wtedy cała zawartość tekstu zostanie zapisana w zmiennej do której odwołuje się funkcja input, np.:
text = input(),
pod zmienną text będziemy mieli całą zawartość tekstu.
'''
import string

text = input()
text = text.lower().strip()
for character in [' ', ',', '.']:
    if character in text:
        text = text.replace(character,"")

dictionary = {}

for letter in text:
    if letter in dictionary:
        dictionary[letter] += 1
    else:
        dictionary[letter] = 1

print(dict(sorted(dictionary.items())))


