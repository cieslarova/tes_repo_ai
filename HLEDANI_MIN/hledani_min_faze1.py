# HLEDANI_MIN/hledani_min.py

class MinFinder:
    """
    Třída MinFinder slouží k nalezení minimální hodnoty v seznamu čísel.
    V této fázi je implementována pouze základní kostra a inicializace.
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
        print(f"MinFinder inicializován s daty: {self.data}") # Záchytný bod pro ověření inicializace

    def find_minimum(self):
        """
        Metoda pro nalezení minimální hodnoty v seznamu dat.
        V této fázi je pouze záchytným bodem a neobsahuje plnou logiku.

        :raises NotImplementedError: Vždy vyvolá chybu, protože logika není ještě implementována.
        :return: Zatím nic, protože logika není implementována.
        """
        # Zde bude v budoucnu implementována hlavní logika pro nalezení minima.
        # Prozatím vyvoláme chybu, aby bylo jasné, že metoda není dokončena.
        raise NotImplementedError("Logika pro nalezení minima ještě není implementována.")

# Příklad použití (pro testování inicializace)
if __name__ == "__main__":
    # Ukázkový seznam čísel pro testování.
    test_data_1 = [10, 5, 20, 15]
    finder_1 = MinFinder(test_data_1)

    # Pokus o volání metody find_minimum by měl vyvolat NotImplementedError.
    try:
        finder_1.find_minimum()
    except NotImplementedError as e:
        print(f"Očekávaná chyba: {e}")

    # Další ukázkový seznam.
    test_data_2 = [3.14, 2.71, 1.618]
    finder_2 = MinFinder(test_data_2)
