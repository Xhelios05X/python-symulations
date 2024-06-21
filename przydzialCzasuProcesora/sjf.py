def sjf(processes:list) -> tuple:
    """
    Funckcja implementuje algorytm Shortest Job First (SJF),
    polegający na obsłudze procesów z najktórszym czasem
    wykonania.

    Parametry:
    [list] processes - lista procesów do obsługi

    Funkcja zwraca krotkę (tuple) z wartościami:
    [float] averageWaitingTime - średni czas oczekiwania procesu
    [float] averageTurnaroundTime - średni czas przetwarzania procesu
    """

    processes.sort(key = lambda x: (x["AT"], x["BT"]))
    processesLength = len(processes)
    processesRemaind = processesLength

    currentTime = 0
    waitingTime = 0
    turnaroundTime = 0
    queue = []

    while processesRemaind > 0:
        while processes and processes[0]["AT"] <= currentTime:
            toQueue = processes.pop(0)
            queue.append(toQueue)

        if len(queue) != 0:
            queue.sort(key = lambda x: x["BT"])
            process = queue.pop(0)

            waitingTime += (currentTime - process["AT"])
            currentTime += process["BT"]
            turnaroundTime += (process["BT"] + waitingTime)
            processesRemaind -= 1
        else:
            currentTime += 1
    
    averageWaitingTime = waitingTime / processesLength
    averageTurnaroundTime = turnaroundTime / processesLength

    return averageWaitingTime, averageTurnaroundTime