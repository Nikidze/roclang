from .Threads import threads

class ThreadStatement:
    def __init__(self, threads):
        self.threads = threads

    def execute(self):
        names = self.threads.keys()
        for name in names:
            th = threads(name, self.threads[name])
            th.start()

