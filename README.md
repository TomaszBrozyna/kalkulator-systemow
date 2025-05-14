
# 🧮 Jak działa kalkulator systemów liczbowych w Pythonie?

## 🧠 Główna idea
Program umożliwia konwersję liczby między systemami:
- binarnym (2)
- ósemkowym (8)
- dziesiętnym (10)
- szesnastkowym (16)

Działa w pętli, aż użytkownik zdecyduje zakończyć.

---

## 1. `konwertuj_na_dziesietny()`
Zamienia liczbę tekstową (np. `"1A"`) na liczbę dziesiętną (`26`), używając `int(..., system)`.  
Jeśli wpis jest błędny (np. litera w systemie binarnym), zgłasza błąd i zwraca `None`.

---

## 2. `konwertuj_z_dziesietnego()`
Zamienia liczbę dziesiętną na:
- binarny → `bin()`
- ósemkowy → `oct()`
- szesnastkowy → `hex()`

Usuwa przedrostki (`0b`, `0x`, `0o`) i zwraca wynik.

---

## 3. `wybierz_system()`
- Wyświetla listę dostępnych systemów.
- Pyta użytkownika o wybór.
- Sprawdza, czy wybór to jedna z wartości: `2`, `8`, `10`, `16`.

---

## 4. `main()`
Program wykonuje się w nieskończonej pętli `while True`:

1. Użytkownik wybiera system wejściowy i podaje liczbę.
2. Program konwertuje ją na system dziesiętny.
3. Użytkownik wybiera system wyjściowy.
4. Program wyświetla wynik.
5. Pojawia się pytanie: **"Czy chcesz kontynuować?"**  
   Jeśli nie → program się kończy.

---

## ✅ Przykład działania

```
Wejście:  liczba = "1A", system_z = 16
Wyjście: system_do = 2
Wynik:   "11010"
```

---

## 🛠️ Technologie i składnia
- `int(str, base)` do konwersji z dowolnego systemu do dziesiętnego
- `bin()`, `oct()`, `hex()` do konwersji z dziesiętnego
- `input()`, `print()`, `try/except`, pętle, funkcje
