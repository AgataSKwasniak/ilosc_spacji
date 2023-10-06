a = input("Wpisz dowolny tekst ")

print("Ilość znaków: ")
print(len(a))

ileZnakow = len(a)
print(f"Znakow jest: {ileZnakow}")

print("Ilosc spacji: ")
print(a.count(" "))

ileSpacji = a.count(" ")
print(f"Spacji (I) jest: {ileSpacji}")

aBezSpacji = a.replace(" ","")
ileZnakowTxtBezSpacji = len(aBezSpacji)

ileSpacji_II = ileZnakow - ileZnakowTxtBezSpacji
print(f"Soacji (II) jest: {ileSpacji_II}")







