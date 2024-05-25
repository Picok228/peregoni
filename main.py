
import pygame
from car import Player

def start_game():
    window = pygame.display.set_mode((500, 650))
    fps = pygame.time.Clock()


    roket = Player(270, 290, 65, 135, "optimys_prime/автомобіль.png", 3)
    bacground = pygame.transform.scale(
        pygame.image.load("optimys_prime/дорога.png"), (500, 650)
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        roket.draw(window)

        roket.move()
        pygame.display.flip()
        fps.tick(30)
        window.blit(bacground, (5, 5))

start_game()