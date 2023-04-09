import pygame

pygame.init()
WIDTH, HEIGHT = 900, 500  # screen size
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
def main():
    run = True
    while run:
        for event in pygame.event.get():#  list of events
            if even.type == pygame.QUIT:
                run = false;

    pygame.quit()