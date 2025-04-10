import datetime
oceny = {"Paweł": 3, "Kamil": 4, "Wiesiek": 5, "Mariola": 5}

dodaj_oceny = input("Czy chcesz dodać nowe oceny? (tak/nie): ").strip().lower()

if dodaj_oceny == "tak":
    ile_osob = input("Ilu osobom chcesz dodać oceny?: ")
    if ile_osob.isdigit():
        ile_osob = int(ile_osob)
        licznik = 0
        while licznik < ile_osob:
            imie = input(f"Podaj imię osoby nr {licznik + 1}: ").strip()
            ocena = input(f"Podaj ocenę dla {imie} (1-6): ").strip()
            if ocena.isdigit():
                ocena = int(ocena)
                if 1 <= ocena <= 6:
                    oceny[imie] = ocena
                    licznik += 1
                else:
                    print("Ocena musi być z przedziału 1-6.")
            else:
                print("Wprowadź poprawną ocenę (liczba całkowita).")
    else:
        print("Nie podano poprawnej liczby osób.")
else:
    print("Nie dodano nowych ocen.")


zapisz = input("Czy chcesz zapisać oceny w pliku? (tak/nie): ").strip().lower()

if zapisz == "tak":
    nazwa_pliku = input("Podaj nazwę pliku wraz z rozszerzeniem: ").strip()
    sciezka_pulpit = "C:\\Users\\aleks\\OneDrive\\Pulpit\\" + nazwa_pliku

    plik = open(sciezka_pulpit, "w", encoding="utf-8")
    plik.write("="*40 + "\nDziennik ocen uczniów\n" + "="*40 + "\n")
    for uczen, ocena in oceny.items():
        plik.write(f"{uczen}: {ocena}\n")
    data_modyfikacji = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plik.write(f"\nOstatnia modyfikacja: {data_modyfikacji}\n")
    plik.write("Skrypt został utworzony przez: AK i WL\n")
    plik.close()

    print(f"Plik '{nazwa_pliku}' został zapisany na pulpicie.")

    podejrzyj = input("Czy chcesz podejrzeć zapisany plik? (tak/nie): ").strip().lower()
    if podejrzyj == "tak":
        print("\nZawartość pliku:\n" + "-"*30)
        plik = open(sciezka_pulpit, "r", encoding="utf-8")
        zawartosc = plik.read()
        plik.close()
        print(zawartosc)


        suma = 0
        liczba = 0
        for ocena in oceny.values():
            suma += ocena
            liczba += 1
        srednia = suma / liczba
        print(f"\nŚrednia ocen wynosi: {srednia:.2f}")
    else:
        print("Nie wyświetlono zawartości pliku.")
else:
    print("Nie zapisano ocen do pliku.")


input("\nKliknij ENTER, aby zakończyć działanie skryptu.")
print("Działanie skryptu zostało zakończone.")
