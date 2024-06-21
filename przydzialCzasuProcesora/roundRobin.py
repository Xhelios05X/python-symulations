def roundRobin(processes: list, TQ: float) -> tuple:
    """
    Funkcja roundRobin implementuje algorytm Round Robin
    (algorytm karuzelowy), ktorego zadaniem jest obsluga
    procesow poprzez przydzielanie kwantu czasu poszczególnym
    procesom w pętli aż do ich wykoania.

    Parametry:
    [list] processes - lista procesow do obsluzenia
    [float] TQ - kwant czasu obslugi procesu przez procesor (Time Quantum)

    Funkcja zwraca krotkę (tuple) o wartościach:
    [float] averageWaitingTime - średni czas oczekiwania procesu
    [float] averageTurnaroundTime - średni czas przetwarzania procesu
    """

    processes.sort(key = lambda x: x["AT"])
    processesLength = len(processes)
    supportProcessesLength = processesLength

    currentTime = 0.0
    waitingTime = 0.0
    turnaroundTime = 0.0

    allServed = False
    while supportProcessesLength > 0:
        for process in processes:
            
            if process["BT"] != 0:
                if process["BT"] < TQ:
                    currentTime += process["BT"]
                    waitingTime += (currentTime - process["AT"])
                    turnaroundTime += (process["BT"]+waitingTime)
                    supportProcessesLength -= 1
            
                else:
                    process["BT"] -= TQ
                    currentTime += TQ
                    turnaroundTime += TQ

                    if process["BT"] == 0:
                        waitingTime += (currentTime - process["AT"])
                        turnaroundTime += waitingTime
                        supportProcessesLength -= 1

        if len(processes) == 0:
            allServed = True

    averageWaitingTime = waitingTime / processesLength
    averageTurnaroundTime = turnaroundTime / processesLength

    return averageWaitingTime, averageTurnaroundTime