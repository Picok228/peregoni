
import pygame
from car import Player

def start_game():
    window = pygame.display.set_mode((500, 650))
    fps = pygame.time.Clock()


    roket = Player(270, 290, 65, 145, "optimys_prime/автомобіль.png", 7)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        roket.draw(window)

        roket.move()
        pygame.display.flip()
        fps.tick(30)

start_game()