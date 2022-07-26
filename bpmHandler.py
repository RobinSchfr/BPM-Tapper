import time


class BPMHandler:
    timeA = 60
    timeB = 0
    state = 0

    def tick(self):
        if self.state == 0:
            self.timeA = time.time()
            self.state = 1
        else:
            self.timeB = time.time()
            self.state = 0

    def calculateBPM_raw(self):
        return round(60 / abs(self.timeA - self.timeB), 1)

    def calculateBPM_formatted(self):
        return str(self.calculateBPM_raw()).zfill(5)