import queue
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.proc = dict(procs_map)