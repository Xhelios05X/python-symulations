def fcfs(processes: list) -> tuple:
    """
    Funkcja implementuje algorytm Fist Come First Served.
    Polega on na obsłudze procesów w miarę ich przybywania

    Parametry:
    [list] processes - ciąg procesów do obsługi
    
    Funkcja zwraca krotkę (tuple) o wartościach:
    [float] averageWaitingTime - średni czas oczekiwania procesu
    [float] averageTurnaroundTime - średni czas obłsugi procesu 
    """
    processes.sort(key = lambda x: x["AT"])
    processesLength = len(processes)

    currentTime = 0
    waitingTime = 0
    turnaroundTime = 0

    for process in processes:
        waitingTime += (currentTime - process["AT"])
        currentTime += process["BT"]
        turnaroundTime += (process["BT"]+waitingTime)
    
    averageWaitingTime = waitingTime / processesLength
    averageTurnauroundTime = turnaroundTime / processesLength

    return averageWaitingTime, averageTurnauroundTime
    