#!/bin/bash

class CoalMine:

    """Represents a coal mine whose output is dependent
    on the number of workers assigned to the mine, with
    diminishing returns when the number of workers exceed
    a specific number
    
    BASE_WORKER_OUTPUT, the base output of a single worker
    WORKER_THRESHOLD, the number of workers which can work in the mine
    DR_THRESHOLD, the threshold for workers before diminishing returns occur
    DR_EFFICIENCY, the efficiency of each worker after diminishing returns occur

    The property output calculates output based on number
    of workers and the constants
    """

    BASE_WORKER_OUTPUT = 15
    WORKER_THRESHOLD = 10

    DR_THRESHOLD = 5
    DR_EFFICIENCY = 0.8

    def __init__(self, workers=0) -> None:
        self.workers=workers

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        if value < 0:
            self._workers = 0
        elif value <= self.WORKER_THRESHOLD:
            self._workers = value
        else:
            self._workers = self.WORKER_THRESHOLD

    @property
    def output(self):
        output = 0
        for i in range(self.workers):
            output += self.BASE_WORKER_OUTPUT * (1 if i < self.DR_THRESHOLD else self.DR_EFFICIENCY)
        return output

def main():
    cm = CoalMine(workers=7)
    print(cm.output)

if __name__ == "__main__":
    main()
