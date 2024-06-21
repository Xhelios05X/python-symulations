#!/bin/python3

import json
import fcfs
import roundRobin
import sjf

def fcfsTesting(processesList: list) -> tuple:
    """
    Funkcja testuje algorytm FCFS za pomocą listy
    procesów

    Parametry:
    [list] processesList - lista ciągów procesów do obsługi

    Funkcja zwraca krotkę (tuple) o wartościach:
    [float] generalAverageWaitingTime - średnia z uzyskanych średnich czasów oczekiwana
    [float] generalAverageTurnaroundTime - średnia z uzyskanych średnich czasów obsługi
    """
    averageWaitingTimes = []
    averageTurnaroundTimes = []
    avW, avT = 0, 0
    for processes in processesList:
        avW, avT = fcfs.fcfs(processes)
        averageTurnaroundTimes.append(avT)
        averageWaitingTimes.append(avW)
    
    averageWaitingTimesLength = len(averageWaitingTimes)
    averageTurnaroundTimesLength = len(averageTurnaroundTimes)

    try:
        generalAverageWaitingTime = sum(averageWaitingTimes)/averageWaitingTimesLength
        generalAverageTurnaroundTime = sum(averageTurnaroundTimes)/averageTurnaroundTimesLength
        return generalAverageWaitingTime, generalAverageTurnaroundTime
    except:
        return 0, 0
    
def roundRobinTesting(processesList: list, TQ: float) -> tuple:
    """
    Funkcja testuje algorytm Round Robin za pomocą listy
    procesów

    Parametry:
    [list] processesList - lista ciągów procesów do obsługi
    [float] TQ - kwat czasu do obsługi procesu

    Funkcja zwraca krotkę (tuple) o wartościach:
    [float] generalAverageWaitingTime - średnia z uzyskanych średnich czasów oczekiwana
    [float] generalAverageTurnaroundTime - średnia z uzyskanych średnich czasów obsługi
    """
    averageWaitingTimes = []
    averageTurnaroundTimes = []
    avW, avT = 0, 0
    for processes in processesList:
        avW, avT = roundRobin.roundRobin(processes, TQ)
        averageTurnaroundTimes.append(avT)
        averageWaitingTimes.append(avW)
    
    averageWaitingTimesLength = len(averageWaitingTimes)
    averageTurnaroundTimesLength = len(averageTurnaroundTimes)

    try:
        generalAverageWaitingTime = sum(averageWaitingTimes)/averageWaitingTimesLength
        generalAverageTurnaroundTime = sum(averageTurnaroundTimes)/averageTurnaroundTimesLength
        return generalAverageWaitingTime, generalAverageTurnaroundTime
    except:
        return 0, 0
    
def sjfTesting(processesList: list) -> float:
    """
    Funkcja testuje algorytm SJF za pomocą listy
    procesów

    Parametry:
    [list] processesList - lista ciągów procesów do obsługi

    Funkcja zwraca krotkę (tuple) o wartościach:
    [float] generalAverageWaitingTime - średnia z uzyskanych średnich czasów oczekiwana
    [float] generalAverageTurnaroundTime - średnia z uzyskanych średnich czasów obsługi
    """
    averageWaitingTimes = []
    averageTurnaroundTimes = []
    avW, avT = 0, 0
    for processes in processesList:
        avW, avT = sjf.sjf(processes)
        averageTurnaroundTimes.append(avT)
        averageWaitingTimes.append(avW)
    
    averageWaitingTimesLength = len(averageWaitingTimes)
    averageTurnaroundTimesLength = len(averageTurnaroundTimes)

    try:
        generalAverageWaitingTime = sum(averageWaitingTimes)/averageWaitingTimesLength
        generalAverageTurnaroundTime = sum(averageTurnaroundTimes)/averageTurnaroundTimesLength
        return generalAverageWaitingTime, generalAverageTurnaroundTime
    except:
        return 0, 0

if __name__ == "__main__":
    """
    Główna funkcja programu testowania algorytmów
    przydziału czasu procesora. Wywołuje ona 
    funkcje do testowania poszczególnych algorytmów
    """

    # otwieranie pliku z wygenerowanymi procesami
    with open("generatedProcesses.json", "r") as file:
        sequences = json.load(file)
    file.close()
    
    # testowanie poszczególnych algorytmów
    fcfsTestingOutput = fcfsTesting(sequences)
    roundRobin05testingOutput = roundRobinTesting(sequences, 3.0)
    roundRobin3testingOutput = roundRobinTesting(sequences, 3.0)
    roundRobin5testingOutput = roundRobinTesting(sequences, 5.0)
    sjfTestingOutput = sjfTesting(sequences)

    # zwracanie wyników
    generalOutput = f"""FCFS - średni czas oczekiwania: {fcfsTestingOutput[0]}, średni czas przetwarzania {fcfsTestingOutput[1]}
Round Robin TQ: 0.5 - średni czas oczekiwania: {roundRobin05testingOutput[0]}, średni czas przetwarzania {roundRobin05testingOutput[1]}
Round Robin TQ: 3 - średni czas oczekiwania: {roundRobin3testingOutput[0]}, średni czas przetwarzania {roundRobin3testingOutput[1]}
Round Robin TQ: 5 - średni czas oczekiwania: {roundRobin5testingOutput[0]}, sredni czas przetwarzania {roundRobin5testingOutput[1]}
SJF - średni czas oczekiwania: {sjfTestingOutput[0]}, średcatni czas przetwarzania {sjfTestingOutput[1]}
    """
    print(generalOutput)

    # zapis wyników do pliku 'DPUallcoationTime.txt'
    with open("CPUallocationTime.txt", "w") as f:
        f.write(generalOutput)
    f.close()