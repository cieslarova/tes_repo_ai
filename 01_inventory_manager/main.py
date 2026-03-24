# inventory_manager.py - Fáze 1: Základní struktura pro správu inventáře
# Tento modul definuje základní třídy pro reprezentaci položek a inventáře.
# Cílem je vytvořit kostru, na kterou se bude v dalších fázích nabalovat logika.

class Item:
    """
    Třída Item reprezentuje jednu položku v inventáři.
    Každá položka bude mít název a množství.
    V této fázi pouze definujeme atributy a základní inicializaci.
    """
    def __init__(self, name: str, quantity: int):
        # Inicializace nové položky.
        # name: Název položky (např. "Jablko", "Meč").
        # quantity: Počet kusů této položky. Předpokládáme kladné celé číslo.
        self.name = name
        self.quantity = quantity

    def __str__(self):
        # Metoda pro textovou reprezentaci objektu Item.
        # Bude použita pro snadné zobrazení položky.
        # Vrátí formátovaný řetězec, např. "Jablko (5 ks)".
        return f"{self.name} ({self.quantity} ks)"

class Inventory:
    """
    Třída Inventory spravuje kolekci položek.
    Bude obsahovat metody pro přidávání, odebírání a zobrazování položek.
    V této fázi pouze inicializujeme prázdný inventář.
    """
    def __init__(self):
        # Inventář je reprezentován slovníkem, kde klíčem je název položky (string)
        # a hodnotou je objekt Item. To umožňuje rychlé vyhledávání a aktualizaci.
        self.items = {} # Slovník pro uložení položek: {název_položky: objekt_Item}

    def add_item(self, item_name: str, quantity: int):
        """
        Metoda pro přidání nové položky nebo aktualizaci existující.
        Zatím bez implementace logiky, pouze placeholder.
        item_name: Název položky k přidání/aktualizaci.
        quantity: Množství k přidání.
        """
        # Logika pro přidání nebo aktualizaci položky bude implementována v další fázi.
        pass

    def remove_item(self, item_name: str, quantity: int):
        """
        Metoda pro odebrání položky nebo snížení jejího množství.
        Zatím bez implementace logiky, pouze placeholder.
        item_name: Název položky k odebrání.
        quantity: Množství k odebrání.
        """
        # Logika pro odebrání položky bude implementována v další fázi.
        pass

    def list_items(self):
        """
        Metoda pro zobrazení všech položek v inventáři.
        Zatím bez implementace logiky, pouze placeholder.
        """
        # Logika pro výpis položek bude implementována v další fázi.
        pass

# Hlavní spouštěcí blok programu.
# V této fázi pouze pro testování inicializace a základní struktury.
if __name__ == "__main__":
    print("Spouštění systému správy inventáře (Fáze 1)...")
    # Vytvoření instance inventáře.
    my_inventory = Inventory()
    print("Prázdný inventář byl úspěšně inicializován.")

    # Ukázka vytvoření objektu Item (zatím bez přidání do inventáře).
    sample_item = Item("Meč", 1)
    print(f"Vytvořena ukázková položka: {sample_item}")

    print("\nFáze 1 dokončena. Čeká se na implementaci logiky.")
