import random
import json

def processesGenerate(Nsequences, Nprocesses):
    """
    Funkcja generuje listę ciągów procesów na postawie
    zadanych parametrów.

    Funkcja przyjmuje dwie zmienne:
    [int] Nsqeuences - liczba ciagow do utworzenia
    [int] Nprocesses - liczba procesow w kazdym ciagu

    Funkcja zapisuje wygenerowane ciągi procesów
    do pliku wyjściowego o rozszerzeniu .json
    """
    ATrange = (1,10,)
    BTrange = (1,20,)

    # generowanie ciagow procesow
    allSequences = []
    for _ in range(Nsequences):
        
        sequence = []
        for i in range(Nprocesses):
            process = {
                "id": str(i),
                "AT": random.randint(ATrange[0], ATrange[1]),
                "BT": random.randint(BTrange[0], BTrange[1])
            }
            sequence.append(process)
        
        allSequences.append(sequence)
    
    with open("generatedProcesses.json", "w") as f:
        json.dump(allSequences, f, indent = 4)

if __name__ == "__main__":
    # Główna funkcja. wywołuje ona funkcję
    # do generowania precesów
    Nsequences = 100
    Nprocesses = 100
    processesGenerate(Nsequences, Nprocesses)