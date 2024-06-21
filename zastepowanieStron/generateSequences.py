import random
import json

def generateSequences(seqNumber: int, seqLength: int, pageNumber: int) -> list:
    """
    Funckja generuje listę ciaągów numerów stron na podstawie zadanych parametrów
    Argumenty funkcji:
    [int] seqNumber - ilosc ciagow stron
    [int] seqLength - ilosc stron w ciagu
    [int] pageNumber - koniec przedzualu numeru stron do wygenerowania

    Zwraca:
    [list] lista sekwencji numerow stron do testowania algorytmow
    """

    seqences = []

    for _ in range(seqNumber):
        pages = []
        for _ in range(seqLength):
            page = {
                "number": random.randint(1, pageNumber)
            }
            pages.append(page)
        seqences.append(pages)
    
    return seqences

if __name__ == "__main__":
    """
    Główna funkcja, wywołująca generowanie ciągów numerów stron.
    Zapisuje ona wygenerowane ciągi do pliku o rozszerzeniu .json
    """
    seqNumber = 100
    seqLength = 100
    pageNumber = 20
    seqences = generateSequences(seqNumber, seqLength, pageNumber)

    with open("generatedSequences.json", "w") as gs:
        json.dump(seqences, gs, indent = 4)
    gs.close()