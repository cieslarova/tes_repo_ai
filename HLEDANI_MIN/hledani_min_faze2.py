# HLEDANI_MIN/hledani_min.py

class MinFinder:
    """
    Třída MinFinder slouží k nalezení minimální hodnoty v seznamu čísel.
    V této fázi je implementována základní funkční logika pro nalezení minima.
    """

    def __init__(self, data_list):
        """
        Konstruktor třídy MinFinder.
        Inicializuje instanci s daným seznamem dat.

        :param data_list: Seznam hodnot, ve kterém se bude hledat minimum.
                          Očekává se, že bude obsahovat číselné hodnoty.
        :type data_list: list
        """
        # Uložení vstupního seznamu dat do atributu instance.
        # V budoucnu zde může být přidána validace vstupních dat.
        self.data = data_list
        # print(f"MinFinder inicializován s daty: {self.data}") # Záchytný bod pro ověření inicializace

    def find_minimum(self):
        """
        Metoda pro nalezení minimální hodnoty v seznamu dat.
        Implementuje základní iterační logiku.

        :return: Minimální hodnota ze seznamu, nebo None, pokud je seznam prázdný.
        :rtype: int | float | None
        """
        # Kontrola, zda je seznam prázdný. Pokud ano, nelze najít minimum.
        if not self.data:
            print("Seznam je prázdný, nelze najít minimum.")
            return None

        # Inicializace proměnné pro uložení minimální hodnoty.
        # Předpokládáme, že první prvek seznamu je prozatím minimum.
        # V budoucnu bude potřeba ošetřit případ, kdy první prvek není číslo.
        current_minimum = self.data[0]

        # Iterace přes zbývající prvky seznamu.
        for item in self.data[1:]:
            # Porovnání aktuálního prvku s dosud nalezeným minimem.
            # Pokud je aktuální prvek menší, stane se novým minimem.
            if item < current_minimum:
                current_minimum = item
        
        # Vrácení nalezené minimální hodnoty.
        return current_minimum

# Příklad použití
if __name__ == "__main__":
    print("--- Fáze 2: Testování základní logiky ---")

    # Test s běžným seznamem čísel.
    test_data_1 = [10, 5, 20, 15, 3]
    finder_1 = MinFinder(test_data_1)
    min_val_1 = finder_1.find_minimum()
    print(f"V datech {test_data_1} je minimum: {min_val_1}") # Očekává se: 3

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
    print(f"V datech {test_data_4} je minimum: {min_val_4}") # Očekává se: 42
