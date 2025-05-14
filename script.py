def konwertuj_na_dziesietny(liczba_str, system_z):
    try:
        return int(liczba_str, system_z)
    except ValueError:
        print("Błąd: Niepoprawna liczba dla tego systemu!")
        return None

def konwertuj_z_dziesietnego(liczba, system_do):
    if system_do == 2:
        return bin(liczba)[2:]
    elif system_do == 8:
        return oct(liczba)[2:]
    elif system_do == 10:
        return str(liczba)
    elif system_do == 16:
        return hex(liczba)[2:].upper()
    else:
        return "Nieobsługiwany system!"

def wybierz_system(tekst):
    print(tekst)
    print("2 - binarny\n8 - ósemkowy\n10 - dziesiętny\n16 - szesnastkowy")
    while True:
        try:
            system = int(input("Wybierz system: "))
            if system in [2, 8, 10, 16]:
                return system
            else:
                print("Wybierz spośród: 2, 8, 10, 16")
        except ValueError:
            print("Wprowadź liczbę!")

def main():
    print("=== Kalkulator systemów liczbowych ===")
    while True:
        system_z = wybierz_system("\nZ jakiego systemu chcesz konwertować?")
        liczba_str = input("Podaj liczbę: ").strip()

        liczba_dziesietna = konwertuj_na_dziesietny(liczba_str, system_z)
        if liczba_dziesietna is None:
            continue

        system_do = wybierz_system("\nNa jaki system chcesz konwertować?")
        wynik = konwertuj_z_dziesietnego(liczba_dziesietna, system_do)

        print(f"\nWynik: {wynik}")

        kontynuuj = input("\nCzy chcesz wykonać kolejną konwersję? (t/n): ").strip().lower()
        if kontynuuj != 't':
            print("Kończę działanie kalkulatora. Do zobaczenia!")
            break

main()
