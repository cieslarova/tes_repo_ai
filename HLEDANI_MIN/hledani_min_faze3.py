# HLEDANI_MIN/hledani_min.py

class MinFinder:
    """
    Třída MinFinder slouží k nalezení minimální hodnoty v seznamu čísel.
    V této finální fázi je implementována robustní logika s ošetřením chyb
    a validací vstupních dat.
    """

    def __init__(self, data_list):
        """
        Konstruktor třídy MinFinder.
        Inicializuje instanci s daným seznamem dat.

        :param data_list: Seznam hodnot, ve kterém se bude hledat minimum.
                          Očekává se, že bude obsahovat číselné hodnoty.
        :type data_list: list
        :raises TypeError: Pokud vstupní data_list není seznam.
        """
        # Validace, zda je vstupní parametr skutečně seznam.
        if not isinstance(data_list, list):
            raise TypeError("Vstup musí být seznam (list).")
        self.data = data_list

    def find_minimum(self):
        """
        Metoda pro nalezení minimální hodnoty v seznamu dat.
        Obsahuje robustní logiku s validací dat a ošetřením chyb.

        :return: Minimální hodnota ze seznamu, nebo None, pokud je seznam prázdný.
        :rtype: int | float | None
        :raises ValueError: Pokud seznam obsahuje nečíselné hodnoty.
        """
        # Kontrola, zda je seznam prázdný. Pokud ano, nelze najít minimum.
        if not self.data:
            print("Seznam je prázdný, nelze najít minimum.")
            return None

        # Inicializace proměnné pro uložení minimální hodnoty.
        # Předpokládáme, že první prvek seznamu je prozatím minimum.
        # Je nutné ověřit, zda je první prvek číslo.
        try:
            current_minimum = float(self.data[0]) # Pokus o převod na float pro univerzálnost
        except (TypeError, ValueError):
            raise ValueError(f"První prvek '{self.data[0]}' v seznamu není platné číslo.")

        # Iterace přes zbývající prvky seznamu.
        for i, item in enumerate(self.data[1:]):
            try:
                # Pokus o převod aktuálního prvku na float.
                # To zajistí, že porovnáváme pouze číselné hodnoty.
                numeric_item = float(item)
            except (TypeError, ValueError):
                # Pokud prvek nelze převést na číslo, vyvoláme chybu.
                raise ValueError(f"Prvek na indexu {i+1} ('{item}') v seznamu není platné číslo.")
            
            # Porovnání aktuálního číselného prvku s dosud nalezeným minimem.
            # Pokud je aktuální prvek menší, stane se novým minimem.
            if numeric_item < current_minimum:
                current_minimum = numeric_item
        
        # Vrácení nalezené minimální hodnoty.
        return current_minimum

# Příklad použití
if __name__ == "__main__":
    print("--- Fáze 3: Testování robustní logiky a ošetření chyb ---")

    # Test s běžným seznamem čísel (celá čísla).
    test_data_1 = [10, 5, 20, 15, 3]
    finder_1 = MinFinder(test_data_1)
    min_val_1 = finder_1.find_minimum()
    print(f"V datech {test_data_1} je minimum: {min_val_1}") # Očekává se: 3.0

    # Test s desetinnými čísly.
    test_data_2 = [3.14, 2.71, 1.618, 5.0]
    finder_2 = MinFinder(test_data_2)
    min_val_2 = finder_2.find_minimum()
    print(f"V datech {test_data_2} je minimum: {min_val_2}") # Očekává se: 1.618

    # Test s prázdným seznamem.
    test_data_3 = []
    finder_3 = MinFinder(test_data_3)
    min_val_3 = finder_3.find_minimum()
    print(f"V datech {test_data_3} je minimum: {min_val_3}") # Očekává se: None

    # Test se seznamem obsahujícím pouze jeden prvek.
    test_data_4 = [42]
    finder_4 = MinFinder(test_data_4)
    min_val_4 = finder_4.find_minimum()
    print(f"V datech {test_data_4} je minimum: {min_val_4}") # Očekává se: 42.0

    # Test se seznamem obsahujícím nečíselné hodnoty (včetně prvního prvku).
    test_data_5 = ["abc", 1, 2]
    try:
        finder_5 = MinFinder(test_data_5)
        finder_5.find_minimum()
    except ValueError as e:
        print(f"Očekávaná chyba pro {test_data_5}: {e}") # Očekává se: První prvek 'abc' v seznamu není platné číslo.

    # Test se seznamem obsahujícím nečíselné hodnoty (uprostřed seznamu).
    test_data_6 = [10, 5, "hello", 15]
    try:
        finder_6 = MinFinder(test_data_6)
        finder_6.find_minimum()
    except ValueError as e:
        print(f"Očekávaná chyba pro {test_data_6}: {e}") # Očekává se: Prvek na indexu 2 ('hello') v seznamu není platné číslo.

    # Test s mixem celých a desetinných čísel.
    test_data_7 = [7, 3.5, 12, 1.2, 9.9]
    finder_7 = MinFinder(test_data_7)
    min_val_7 = finder_7.find_minimum()
    print(f"V datech {test_data_7} je minimum: {min_val_7}") # Očekává se: 1.2

    # Test s negativními čísly.
    test_data_8 = [-5, -10, 0, -2]
    finder_8 = MinFinder(test_data_8)
    min_val_8 = finder_8.find_minimum()
    print(f"V datech {test_data_8} je minimum: {min_val_8}") # Očekává se: -10.0

    # Test s neplatným vstupem do konstruktoru (není seznam).
    try:
        finder_9 = MinFinder("toto neni seznam")
        finder_9.find_minimum()
    except TypeError as e:
        print(f"Očekávaná chyba pro 'toto neni seznam': {e}") # Očekává se: Vstup musí být seznam (list).
