import datetime
with open(r"C:\Users\aleks\OneDrive\Pulpit\Python\daily_sales.txt", "r") as file:
    daily_sales = file.read()

suma_kwot = 0.0
yellow = 0
red = 0
black = 0
green = 0
purple = 0
white = 0
blue = 0

lista = daily_sales.split("\n")

for a in lista:
    podzielone = a.split(";,;")
    for a in podzielone:
        if "$" in a:
            cena_str = a.strip().replace('$', '').replace(',', '').strip()
            cena = float(cena_str)
            suma_kwot += cena
        if "yellow" in a.lower():
            yellow += 1
        if "red" in a.lower():
            red += 1
        if "black" in a.lower():
            black += 1
        if "green" in a.lower():
            green += 1
        if "purple" in a.lower():
            purple += 1
        if "white" in a.lower():
            white += 1
        if "blue" in a.lower():
            blue += 1
def najlepszy_najgorszy_kolor(yellow, red, black, green, purple, white, blue):
    ubrania = {'yellow': yellow, 'red': red, 'black': black, 'green': green, 
             'purple': purple, 'white': white, 'blue': blue}
    najlepszy = max(ubrania, key=ubrania.get)
    najgorszy = min(ubrania, key=ubrania.get)
    return najlepszy, najgorszy
najlepszy, najgorszy = najlepszy_najgorszy_kolor(yellow, red, black, green, purple, white, blue)
czas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
result = f'='*50 + '\n           Podsumowanie dnia:\n' + '='*50 
result += f'\nDziś sprzedano towar o łącznej kwocie: {suma_kwot:.2f}$\n' + '='*50
result += f"\nUbrań o kolorze yellow sprzedano: {yellow}\n"
result += f"Ubrań o kolorze red sprzedano: {red}\n"
result += f"Ubrań o kolorze black sprzedano: {black}\n"
result += f"Ubrań o kolorze green sprzedano: {green}\n"
result += f"Ubrań o kolorze purple sprzedano: {purple}\n"
result += f"Ubrań o kolorze white sprzedano: {white}\n"
result += f"Ubrań o kolorze blue sprzedano: {blue}\n\n" + '='*50
result += f"\nNajlepiej sprzedający się kolor: {najlepszy}"
result += f"\nNajgorzej sprzedający się kolor: {najgorszy}\n" + '='*50
result += f"\n\nRaport wygenerowano o: {czas}\n"
result += f'Przygotował: Aleksandra Kmiecik, Wiktoria Lizoń'
with open(r"C:\Users\aleks\OneDrive\Pulpit\Python\new_daily_sales_report.txt", "w") as new_file:
    new_file.write(result)

print(result)
