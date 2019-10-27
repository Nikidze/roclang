from threading import Thread


class threads(Thread):
    def __init__(self, name, block):
        Thread.__init__(self)
        self.name = name
        self.block = block

    def run(self):
        self.block.execute()