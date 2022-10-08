import pygame
import bpmHandler
import GradientBar

WIDTH = 300
HEIGHT = 100

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('BPM Tool')
font = pygame.font.SysFont('consolas', 30)
handler = bpmHandler.BPMHandler()
bar = GradientBar.GradientBar()
running = True


def draw():
    screen.fill(pygame.Color('#191919'))
    bpmTxt = font.render('BPM: ' + handler.calculateBPM_formatted(), True, pygame.Color('#d3d3d3'))
    screen.blit(bpmTxt, (WIDTH / 2 - bpmTxt.get_width() / 2, 20))
    screen.blit(bar.getBar(), (WIDTH / 2 - bar.getBar().get_width() / 2, 70))
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            handler.tick()
            bar.update(handler.calculateBPM_raw())
    draw()
pygame.quit()