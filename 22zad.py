import datetime

with open(r"C:\Users\aleks\OneDrive\Pulpit\Python\daily_sales.txt", "r") as file:
    dzienne_sprzedaze = file.read()

daily_sales_replaced = dzienne_sprzedaze.replace(";,;", "*")
daily_transactions = daily_sales_replaced.split("\n")

daily_transactions_split = [transaction.split("*") for transaction in daily_transactions]
transaction_clean = [[clean.strip() for clean in transaction if clean.strip()] for transaction in daily_transactions_split]


kwota = []
klient = []
kolor = []

for transaction in transaction_clean:
    for clean in transaction:
        if "$" in clean:  
            cena_str = clean.replace('$', '').replace(',', '').strip()
            kwota.append(float(cena_str))
        elif " " in clean and clean.lower() not in ['yellow', 'red', 'black', 'green', 'purple', 'white', 'blue']:  # Klient
            klient.append(clean.strip())
        else: 
            kolor.append(clean.strip().lower())

def oblicz_sume_dochodow(kwota):
    return sum(kwota)

indywidualne_kolory = []
for color in kolor:
    indywidualne_kolory.extend(color.split('&')) 

def policz_sprzedaz_po_kolorze(kolor, indywidualne_kolory):
    return indywidualne_kolory.count(kolor.lower())

def najlepszy_sprzedajacy_sie_kolor(indywidualne_kolory):
    liczba_kolorow = {kolor: indywidualne_kolory.count(kolor) for kolor in set(indywidualne_kolory)}
    return max(liczba_kolorow, key=liczba_kolorow.get)

file_name = input("Podaj nazwę pliku z rozszerzeniem: ")

czas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
total_sales = oblicz_sume_dochodow(kwota)
best_color = najlepszy_sprzedajacy_sie_kolor(indywidualne_kolory)

result = '=' * 50 + '\n           Podsumowanie dnia:\n' + '=' * 50
result += f'\nDziś sprzedano towar o łącznej kwocie: {total_sales:.2f}$\n' + '=' * 50
result += f"\nUbrań o kolorze yellow sprzedano: {policz_sprzedaz_po_kolorze('yellow', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze red sprzedano: {policz_sprzedaz_po_kolorze('red', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze black sprzedano: {policz_sprzedaz_po_kolorze('black', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze green sprzedano: {policz_sprzedaz_po_kolorze('green', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze purple sprzedano: {policz_sprzedaz_po_kolorze('purple', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze white sprzedano: {policz_sprzedaz_po_kolorze('white', indywidualne_kolory)}\n"
result += f"Ubrań o kolorze blue sprzedano: {policz_sprzedaz_po_kolorze('blue', indywidualne_kolory)}\n" + '=' * 50
result += f"\nNajlepiej sprzedający się kolor: {best_color}\n" + '=' * 50
result += f"\n\nRaport wygenerowano o: {czas}\n" 
result += f"Przygotował: Aleksandra Kmiecik, Wiktoria Lizoń"

with open(f"C:\\Users\\aleks\\OneDrive\\Pulpit\\Python\\{file_name}", "w") as new_file:
    new_file.write(result)
print(result)
