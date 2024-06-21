class FIFO:
    """
    Klasa FIFO implementuje algorytm First In First Out (FIFO)
    dla wymiany stron procesu. Gdy występuje konflikt o
    miejsce w pamięci, algorytm usuwa "najstarszą" stronę

    kontruktor klasy:
    [int] cap - pojemność fizyczna dostępna dla procesów
    """

    def __init__(self, cap: int):
        self.cap = cap
    
    def algorithm(self, pages: list) -> int:
        """
        Metoda 'algorithm' to zaimplementowany algorytm FIFO
        
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
                set.append(page)
        return fault