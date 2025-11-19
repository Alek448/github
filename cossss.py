# Prosta tekstowa gra wyborów (150+ linii)
# Styl: wybierasz gdzie idziesz: miasto/wieś -> wybory -> konsekwencje
# Bardzo łatwa, idealna na poziom 1 klasy liceum
# Uruchom: python gra_wyborow.py

import time

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

# ------------------------------
# FUNKCJE WYBORÓW
# ------------------------------

def wybor_miasto():
    slow("Wchodzisz do dużego, tętniącego życiem miasta...")
    time.sleep(1)
    while True:
        print("\n=== MIASTO ===")
        print("1) Pójść do restauracji")
        print("2) Pójść do kina")
        print("3) Odwiedzić sklep z pamiątkami")
        print("4) Wrócić do głównego wyboru")
        wybor = input("> ")

        if wybor == "1":
            slow("Wchodzisz do eleganckiej restauracji. Kelner podaje ci menu.")
            slow("Zamawiasz pyszną pizzę i sok. Miło spędzasz czas.")
        elif wybor == "2":
            slow("Idziesz do kina. Wybierasz najnowszy film przygodowy.")
            slow("Film był świetny! Czujesz się zrelaksowany.")
        elif wybor == "3":
            slow("Wchodzisz do sklepu z pamiątkami.")
            slow("Kupujesz mały brelok na szczęście.")
        elif wybor == "4":
            return
        else:
            print("Niepoprawny wybór!")


def wybor_wies():
    slow("Wchodzisz do spokojnej, malowniczej wsi...")
    time.sleep(1)
    while True:
        print("\n=== WIEŚ ===")
        print("1) Pójść na pole")
        print("2) Odwiedzić farmę")
        print("3) Przejść się po lesie obok wsi")
        print("4) Wrócić do głównego wyboru")
        wybor = input("> ")

        if wybor == "1":
            slow("Idziesz na pole. Wiatr delikatnie porusza zboże.")
            slow("Czujesz spokój i ciszę.")
        elif wybor == "2":
            slow("Wchodzisz na farmę. Widzisz krowy, kury i konia.")
            slow("Rolnik macha do ciebie wesoło.")
        elif wybor == "3":
            slow("Spacerujesz po lesie. Ptaki śpiewają, a drzewa szumią.")
            slow("Znalazłeś mały strumyk.")
        elif wybor == "4":
            return
        else:
            print("Niepoprawny wybór!")


# ------------------------------
# HISTORIA POBICZNA - OPCJONALNE WYBORY
# ------------------------------

def historia_dodatkowa():
    slow("Zbliża się zachód słońca...")
    while True:
        print("\nCo chcesz zrobić wieczorem?")
        print("1) Zostać w domu i odpocząć")
        print("2) Wyjść na spacer")
        print("3) Uczyć się programowania (polecam!)")
        print("4) Zakończyć dzień")
        wybor = input("> ")

        if wybor == "1":
            slow("Kładziesz się na łóżku, słuchasz muzyki i odpoczywasz.")
        elif wybor == "2":
            slow("Wychodzisz na spokojny wieczorny spacer. Powietrze jest chłodne i przyjemne.")
        elif wybor == "3":
            slow("Otwierasz laptopa i uczysz się programować w Pythonie.")
            slow("Czujesz, że robisz postępy!")
        elif wybor == "4":
            slow("Kończysz swój dzień. Jutro czeka cię kolejna przygoda!")
            return
        else:
            print("Niepoprawny wybór!")

# ------------------------------
# GŁÓWNA PĘTLA GRY
# ------------------------------

slow("Twoja przygoda się zaczyna!")
time.sleep(1)

while True:
    print("\n=== GŁÓWNY WYBÓR ===")
    print("1) Iść do miasta")
    print("2) Iść na wieś")
    print("3) Opcje wieczorne (historia poboczna)")
    print("4) Zakończ grę")

    wybor = input("> ")

    if wybor == "1":
        wybor_miasto()
    elif wybor == "2":
        wybor_wies()
    elif wybor == "3":
        historia_dodatkowa()
    elif wybor == "4":
        slow("Dziękujemy za granie!")
        break
    else:
        print("Niepoprawny wybór!")
