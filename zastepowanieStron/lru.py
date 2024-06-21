class LRU:
    """
    Klasa LRU implementuje algorytm Last Recently Used (LRU)
    dla wymiany stron procesu. Typowanie odbywa się poprzez 
    stos procesów (przy każdym odwołaniu strony jej numer
    jest wyjmowany i umieszczany na szczycie stosu). Przy
    konflikcie o miejsce algorytm usuwa najdawniej używaną
    stronę.

    konstruktor klasy:
    [int] cap - pojemność fizyczna dostępna dla procesów
    """

    def __init__(self, cap: int):
        self.cap = cap

    def algorithm(self, pages: list) -> int:
        """
        Metoda 'algorithm' to zaimplementowany algorytm LRU
        
        Parametry:
        [list] pages - ciąg numerów stron

        Zwraca:
        [int] fault - liczba brakujących stron
        """
        set = []
        fault = 0
        for page in pages:
            if page not in set:
                fault += 1
                if len(set) == self.cap:
                    set.pop(0)
            else:
                set.remove(page)
            set.append(page)
        return fault