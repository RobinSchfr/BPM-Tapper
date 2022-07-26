import pygame


class GradientBar:

    def __init__(self):
        self.bar = None
        self.cursor = None
        self.resetBar()

    def update(self, bpm):
        self.resetBar()
        self.cursor = pygame.draw.line(self.bar, pygame.Color('#000000'), (self.calcCursorPos(bpm), 0), (self.calcCursorPos(bpm), self.bar.get_height()), width=3)

    def calcCursorPos(self, bpm):
        return bpm * 0.625    # map bpm to pixel (bar) [250/400]

    def resetBar(self):
        self.bar = pygame.image.load('GradientBar.png')
        self.bar = pygame.transform.scale(self.bar, (250, 10))

    def getBar(self):
        return self.bar