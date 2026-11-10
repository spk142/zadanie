ekwipunek ={ "miecz":{"ilosc":1 , "waga": 5 , "wartosc": 50} , "mikstura": {"ilosc":3 , "waga": 1 , "wartosc": 5} , "zloto":{"ilosc":50 } }
def pokaz(ekwipunek):
  print(ekwipunek)
  return ekwipunek

def dodaj(ekwipunek):


  print("1.Kupno itemow")
  print("2.Sprzedaz itemow")
  wybor = int(input("Co chcesz zrobić:?" ))
  
  if wybor == 1:
    item = input("Co chcesz kupić?: ")
    
    if item in ekwipunek:
      ilosc = int(input("Jaka ilość przedmiotu?: "))
      zlotko = ilosc * ekwipunek[item]["wartosc"]
      if zlotko <= ekwipunek["zloto"]["ilosc"]:
        ekwipunek["zloto"]["ilosc"] -= zlotko
        ekwipunek[item]["ilosc"] += ilosc
      else:
        print("Nie masz wystarczająco złota")
    else:
      iloscd = int(input("Ile chesz kupić?:"))
      wagad = int(input("Ile waży ten przedmiot?:"))
      wartoscd = int(input("Ile wart jest ten przedmiot?:"))
      ekwipunek[item] = {"ilosc": iloscd , "waga": wagad , "wartosc": wartoscd}
  elif wybor == 2:
    item = input("Jaki przedmiot chcesz sprzedać?:")
    ilosc = int(input("Jaka ilość przedmiotu?: "))
    zysk =  ilosc * ekwipunek[item]["wartosc"]
    ekwipunek["zloto"]["ilosc"] += zysk
    ekwipunek[item]["ilosc"] -= 1
    if ekwipunek[item]["ilosc"] == 0:
        del ekwipunek[item]


  return ekwipunek
  
  


def uzyj(ekwipunek):
  uitem = input("Co chcesz użyć?: ")
  if uitem in ekwipunek:
    ekwipunek[uitem]["ilosc"] -= 1
    
def sprawdz(ekwipunek):
  sitem = input("Co chcesz znaleść: ")
  if sitem in ekwipunek:
    print("Posiadasz to w ekwipunku")
    
  else:
    print("Nie posiadasz tego przedmiotu")
    


def gra():
  
  print("MENU:")
  print("1.Pokaż przedmioty")
  print("2.Odwiedź handlarza")
  print("3.Użyj przedmiot")
  print("4.Sprawdź przedmiot")
  print("5.Wyjdź")
  print("")
  


while True:
  gra()
  meni = int(input("Wybierz opcje z menu:"))

  if meni == 1:
   pokaz(ekwipunek)
  if meni == 2:
   dodaj(ekwipunek)
  if meni == 3:
    uzyj(ekwipunek)
  if meni == 4:
    sprawdz(ekwipunek)
  if meni == 5:
    print("Wyjście z gry!")
    break