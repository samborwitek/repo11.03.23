class Mieszkanie:
    def __init__(self, adres, metraz, liczba_pokoi, cena, liczba_mieszkancow, kolor_scian):
        self.adres = adres
        self.metraz = metraz
        self.liczba_pokoi = liczba_pokoi
        self.cena = cena
        self.liczba_mieszkancow = liczba_mieszkancow
        self.kolor_scian = kolor_scian

    def __str__(self):
        return f"Mieszkanie: {self.adres}, Metraż: {self.metraz} m², Liczba pokoi: {self.liczba_pokoi}, Cena: {self.cena} zł, Liczba mieszkańców: {self.liczba_mieszkancow}, Kolor ścian: {self.kolor_scian}"

    def dodaj_mieszkanca(self):
        self.liczba_mieszkancow += 1

    def usun_mieszkanca(self):
        if self.liczba_mieszkancow > 0:
            self.liczba_mieszkancow -= 1

# Przykład użycia klasy Mieszkanie
moje_mieszkanie = Mieszkanie("ul. Kwiatowa 123, Warszawa", 80, 3, 2500, 2, "biały")
print(moje_mieszkanie)

moje_mieszkanie.dodaj_mieszkanca()
print(f"Liczba mieszkańców po dodaniu: {moje_mieszkanie.liczba_mieszkancow}")

moje_mieszkanie.usun_mieszkanca()
print(f"Liczba mieszkańców po usunięciu: {moje_mieszkanie.liczba_mieszkancow}")
