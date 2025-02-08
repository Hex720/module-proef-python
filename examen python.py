import json
import re


# start programma
menu()

# Functie om te controleren of een telefoonnummer geldig is (bijv. alleen cijfers en juiste lengte)
def validate_phone(phone):
    if re.match(r'^\d{10}$', phone):
        return True
    else:
        print("Ongeldig telefoonnummer. Het moet uit 10 cijfers bestaan.")
        return False

# Functie om te controleren of een geboortedatum geldig is
def validate_date(birth_date):
    try:
        day, month, year = map(int, birth_date.split('-'))
        # Controleer of de geboortedatum een redelijke datum is
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2025:
            return True
        else:
            print("Ongeldige geboortedatum.")
            return False
    except ValueError:
        print("Ongeldig formaat voor geboortedatum. Gebruik dd-mm-yyyy.")
        return False

# Functie om lidmaatschapsnummer automatisch toe te wijzen
def generate_membership_number():
    return f"LID{str(int(len(get_all_members()) + 1)).zfill(4)}"

# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om nieuwe leden toe te voegen
def add_new_member(name, birth_date, phone, address):
    if not validate_phone(phone):
        return

    if not validate_date(birth_date):
        return

    # Maak een nieuw lid aan
    new_member = {
        "lidmaatschapsnummer": generate_membership_number(),
        "naam": name,
        "geboortedatum": birth_date,
        "telefoon": phone,
        "adres": address
    }

    # Haal bestaande leden op
    members = get_all_members()
    members.append(new_member)

    # Sla de ledenlijst op in leden.json
    with open('leden.json', 'w') as file:
        json.dump(members, file, indent=4)

    print(f"Nieuw lid toegevoegd: {name}, lidmaatschapsnummer: {new_member['lidmaatschapsnummer']}")

# Voorbeeld van hoe je het toevoegt
if __name__ == "__main__":
    print("Voer de gegevens van het nieuwe lid in:")
    name = input("Naam: ")
    birth_date = input("Geboortedatum (dd-mm-yyyy): ")
    phone = input("Telefoonnummer (10 cijfers): ")
    address = input("Adres: ")

    add_new_member(name, birth_date, phone, address)


# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om gegevens van een lid bij te werken
def update_member_data(membership_number, new_phone=None, new_address=None):
    members = get_all_members()

    # Zoek het lid op met het lidmaatschapsnummer
    member = next((m for m in members if m['lidmaatschapsnummer'] == membership_number), None)

    if member is None:
        print(f"Lid met nummer {membership_number} niet gevonden.")
        return

    # Werk de gegevens bij
    if new_phone:
        member['telefoon'] = new_phone
    if new_address:
        member['adres'] = new_address

    # Sla de bijgewerkte ledenlijst op in leden.json
    with open('leden.json', 'w') as file:
        json.dump(members, file, indent=4)

    print(f"Gegevens van lid {membership_number} zijn bijgewerkt.")

# Functie om een lid op te zoeken en te bewerken via de gebruikersinvoer
def edit_member():
    membership_number = input("Voer het lidmaatschapsnummer van het lid in dat je wilt bewerken: ")

    # Vragen voor de te bewerken gegevens
    new_phone = input("Voer het nieuwe telefoonnummer (laat leeg om niet te bewerken): ")
    new_address = input("Voer het nieuwe adres (laat leeg om niet te bewerken): ")

    # Roep de update functie aan
    update_member_data(membership_number, new_phone if new_phone else None, new_address if new_address else None)

# Voorbeeld van hoe je het bewerken aanroept
if __name__ == "__main__":
    print("Bewerk een lid:")
    edit_member()

# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om een lid te verwijderen
def remove_member(membership_number):
    members = get_all_members()

    # Zoek het lid op met het lidmaatschapsnummer
    member = next((m for m in members if m['lidmaatschapsnummer'] == membership_number), None)

    if member is None:
        print(f"Lid met nummer {membership_number} niet gevonden.")
        return

    # Bevestiging vragen voor verwijderen
    confirm = input(f"Ben je zeker dat je het lid met nummer {membership_number} wilt verwijderen? (ja/nee): ").lower()
    if confirm == 'ja':
        # Verwijder het lid
        members = [m for m in members if m['lidmaatschapsnummer'] != membership_number]

        # Sla de bijgewerkte ledenlijst op in leden.json
        with open('leden.json', 'w') as file:
            json.dump(members, file, indent=4)

        print(f"Lid met nummer {membership_number} is verwijderd.")
    else:
        print("Verwijdering geannuleerd.")

# Functie om een lid te verwijderen via de gebruikersinvoer
def delete_member():
    membership_number = input("Voer het lidmaatschapsnummer van het lid in dat je wilt verwijderen: ")
    remove_member(membership_number)

# Voorbeeld van hoe je het verwijderen aanroept
if __name__ == "__main__":
    print("Verwijder een lid:")
    delete_member()

# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om leden te zoeken op naam of lidmaatschapsnummer
def search_member(search_term):
    members = get_all_members()

    # Zoek op lidmaatschapsnummer of naam
    found_members = [m for m in members if search_term.lower() in m['lidmaatschapsnummer'].lower() or search_term.lower() in m['naam'].lower()]

    if not found_members:
        print(f"Geen leden gevonden voor zoekterm: {search_term}")
        return

    # Resultaten weergeven
    print(f"\nGevonden leden voor zoekterm '{search_term}':\n")
    for member in found_members:
        print(f"Lidmaatschapsnummer: {member['lidmaatschapsnummer']}")
        print(f"Naam: {member['naam']}")
        print(f"Geboortedatum: {member['geboortedatum']}")
        print(f"Telefoon: {member['telefoon']}")
        print(f"Adres: {member['adres']}")
        print("-" * 40)

# Functie voor zoekfunctie via gebruikersinvoer
def find_member():
    search_term = input("Voer een zoekterm in (naam of lidmaatschapsnummer): ")
    search_member(search_term)

# Voorbeeld van hoe je de zoekfunctie aanroept
if __name__ == "__main__":
    print("Zoek een lid:")
    find_member()


# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om leden te sorteren en weer te geven
def display_all_members(sort_by="lidmaatschapsnummer"):
    members = get_all_members()

    if not members:
        print("Geen leden gevonden.")
        return

    # Sorteer leden op basis van de gekozen parameter (lidmaatschapsnummer of naam)
    if sort_by == "naam":
        members.sort(key=lambda x: x['naam'].lower())
    elif sort_by == "lidmaatschapsnummer":
        members.sort(key=lambda x: x['lidmaatschapsnummer'])
    else:
        print("Ongeldige sorteermethode. Gebruik 'naam' of 'lidmaatschapsnummer'.")
        return

    # Leden overzicht weergeven
    print(f"\nLijst van alle leden, gesorteerd op {sort_by}:")
    print("-" * 40)
    for member in members:
        print(f"Lidmaatschapsnummer: {member['lidmaatschapsnummer']}")
        print(f"Naam: {member['naam']}")
        print(f"Geboortedatum: {member['geboortedatum']}")
        print(f"Telefoon: {member['telefoon']}")
        print(f"Adres: {member['adres']}")
        print("-" * 40)

# Functie om een lijst van alle leden weer te geven via gebruikersinvoer
def show_all_members():
    sort_by = input("Wil je sorteren op 'naam' of 'lidmaatschapsnummer'? ").lower()
    display_all_members(sort_by)

# Voorbeeld van hoe je de lijst van alle leden weergeeft
if __name__ == "__main__":
    print("Toon alle leden:")
    show_all_members()



# Functie om leden op te halen uit leden.json
def get_all_members():
    try:
        with open('leden.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Functie om nieuwe leden toe te voegen
def add_new_member(name, birth_date, phone, address):
    if not validate_phone(phone):
        return

    if not validate_date(birth_date):
        return

    new_member = {
        "lidmaatschapsnummer": generate_membership_number(),
        "naam": name,
        "geboortedatum": birth_date,
        "telefoon": phone,
        "adres": address
    }

    members = get_all_members()
    members.append(new_member)

    with open('leden.json', 'w') as file:
        json.dump(members, file, indent=4)

    print(f"Nieuw lid toegevoegd: {name}, lidmaatschapsnummer: {new_member['lidmaatschapsnummer']}")

# Functie om leden te zoeken
def search_member(search_term):
    members = get_all_members()
    found_members = [m for m in members if search_term.lower() in m['lidmaatschapsnummer'].lower() or search_term.lower() in m['naam'].lower()]

    if not found_members:
        print(f"Geen leden gevonden voor zoekterm: {search_term}")
        return

    print(f"\nGevonden leden voor zoekterm '{search_term}':\n")
    for member in found_members:
        print(f"Lidmaatschapsnummer: {member['lidmaatschapsnummer']}")
        print(f"Naam: {member['naam']}")
        print(f"Geboortedatum: {member['geboortedatum']}")
        print(f"Telefoon: {member['telefoon']}")
        print(f"Adres: {member['adres']}")
        print("-" * 40)

# Functie om leden te sorteren en weer te geven
def display_all_members(sort_by="lidmaatschapsnummer"):
    members = get_all_members()

    if not members:
        print("Geen leden gevonden.")
        return

    if sort_by == "naam":
        members.sort(key=lambda x: x['naam'].lower())
    elif sort_by == "lidmaatschapsnummer":
        members.sort(key=lambda x: x['lidmaatschapsnummer'])
    else:
        print("Ongeldige sorteermethode. Gebruik 'naam' of 'lidmaatschapsnummer'.")
        return

    print(f"\nLijst van alle leden, gesorteerd op {sort_by}:")
    print("-" * 40)
    for member in members:
        print(f"Lidmaatschapsnummer: {member['lidmaatschapsnummer']}")
        print(f"Naam: {member['naam']}")
        print(f"Geboortedatum: {member['geboortedatum']}")
        print(f"Telefoon: {member['telefoon']}")
        print(f"Adres: {member['adres']}")
        print("-" * 40)

# Functie om een lid te verwijderen
def remove_member(membership_number):
    members = get_all_members()
    member = next((m for m in members if m['lidmaatschapsnummer'] == membership_number), None)

    if member is None:
        print(f"Lid met nummer {membership_number} niet gevonden.")
        return

    confirm = input(f"Ben je zeker dat je het lid met nummer {membership_number} wilt verwijderen? (ja/nee): ").lower()
    if confirm == 'ja':
        members = [m for m in members if m['lidmaatschapsnummer'] != membership_number]
        with open('leden.json', 'w') as file:
            json.dump(members, file, indent=4)

        print(f"Lid met nummer {membership_number} is verwijderd.")
    else:
        print("Verwijdering geannuleerd.")

# Functie om gegevens van een lid bij te werken
def update_member_data(membership_number, new_phone=None, new_address=None):
    members = get_all_members()
    member = next((m for m in members if m['lidmaatschapsnummer'] == membership_number), None)

    if member is None:
        print(f"Lid met nummer {membership_number} niet gevonden.")
        return

    if new_phone:
        member['telefoon'] = new_phone
    if new_address:
        member['adres'] = new_address

    with open('leden.json', 'w') as file:
        json.dump(members, file, indent=4)

    print(f"Gegevens van lid {membership_number} zijn bijgewerkt.")

# Functie om het menu weer te geven en acties uit te voeren
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Voeg een nieuw lid toe")
        print("2. Zoek leden")
        print("3. Toon alle leden")
        print("4. Verwijder een lid")
        print("5. Bewerk ledengegevens")
        print("6. Verlaat menu")

        keuze = input("Kies een optie (1-6): ")

        if keuze == "1":
            name = input("Naam: ")
            birth_date = input("Geboortedatum (dd-mm-yyyy): ")
            phone = input("Telefoonnummer (10 cijfers): ")
            address = input("Adres: ")
            add_new_member(name, birth_date, phone, address)
        elif keuze == "2":
            search_term = input("Voer een zoekterm in (naam of lidmaatschapsnummer): ")
            search_member(search_term)
        elif keuze == "3":
            sort_by = input("Wil je sorteren op 'naam' of 'lidmaatschapsnummer'? ").lower()
            display_all_members(sort_by)
        elif keuze == "4":
            membership_number = input("Voer het lidmaatschapsnummer van het lid in dat je wilt verwijderen: ")
            remove_member(membership_number)
        elif keuze == "5":
            membership_number = input("Voer het lidmaatschapsnummer van het lid in dat je wilt bewerken: ")
            new_phone = input("Nieuwe telefoon (laat leeg om niet te bewerken): ")
            new_address = input("Nieuw adres (laat leeg om niet te bewerken): ")
            update_member_data(membership_number, new_phone if new_phone else None, new_address if new_address else None)
        elif keuze == "6":
            print("Het menu wordt verlaten.")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

