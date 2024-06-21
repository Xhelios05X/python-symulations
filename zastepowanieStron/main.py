import json
from fifo import FIFO
from lru import LRU

def loadFromFile(name: str) -> list:
    """
    Funkcja otwiera plik z wygenerowanymi
    ciagami numerow stron

    Parametry:
    [string] name - nazwa pliku z danymi

    Funkcja zwraca liste ciagow stron
    """
    with open(name, "r") as gs:
        sequences = json.load(gs)
    gs.close()
    return sequences

def fifoTesting(sequences: list, cap: int) -> float:
    """
    Funkcja testuje algorytm First In First Out (FIFO),
    który usuwa z pamięci najstarszą stronę.

    Parametry:
    [list] sequences - lista ciągów numerów stron
    [int] cap - pojemność ramek pamięci

    Funkcja zwraca:
    [float] - średnia liczba braków stron
    """
    output = 0
    testing = FIFO(cap)
    for sequence in sequences:
        output += testing.algorithm(sequence)
    
    return output/len(sequences)

def lruTesting(sequences: list, cap: int) -> float:
    """
    Funkcja testuje algorytm Least Recently Used (LRU),
    który usuwa z pamięci stronę najdawniej używaną

    Parametry:
    [list] sequences - lista ciągów numerów stron
    [int] cap - pojemność ramek pamięci

    Funkcja zwraca:
    [float] - średnia liczba braków stron
    """
    output = 0
    testing = LRU(cap)
    for sequence in sequences:
        output += testing.algorithm(sequence)
    
    return output/len(sequences)
        

if __name__ == "__main__":
    """
    Główna funkcja programu. Wywołuje ona funkcje testujące
    poszczególne algorytmy z zadanymi wielkościami ramek.
    Zwraca ona wyniki średnich liczb braków stron dla poszczególnych
    algorytmów z zadanymi wielkościami ramek. Wyniki te również
    zapisuje do pliku
    """
    filename = "generatedSequences.json"
    R =[3, 5, 7]
    fifoOutcome = {}
    lruOutcome = {}

    sequences = loadFromFile(filename)

    # wywoływanie funckji testujących algorytmy dla poszczenych
    # wielkości ramek
    for cap in R:
        fifoOutcome[f"{cap}"] = fifoTesting(sequences, cap)
        lruOutcome[f"{cap}"] = lruTesting(sequences, cap)

    # wyświetlanie wyników
    output =  f"""FIFO R: {R[0]} - {fifoOutcome["3"]}
FIFO R: {R[1]} - {fifoOutcome["5"]}
FIFO R: {R[2]} - {fifoOutcome["7"]}
LRU R {R[0]} - {lruOutcome["3"]}
LRU R: {R[1]} - {lruOutcome["5"]}
LRU R: {R[2]} - {lruOutcome["7"]}
"""
    print(output)

    # zapisywanie wyników
    with open("pageReplacement.txt", "w") as pr:
        pr.write(output)
    pr.close()