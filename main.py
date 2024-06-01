from random import randint

import pygame
from car import Player
from car_bot import CAR


def start_game():
    window = pygame.display.set_mode((500, 650))
    fps = pygame.time.Clock()


    roket = Player(270, 290, 58, 128, "optimys_prime/автомобіль.png", 1)
    bacground = pygame.transform.scale(
        pygame.image.load("optimys_prime/дорога.png"), (500, 650)
    )

    car1 = []
    for i in range(1):
        car1.append(CAR(randint(36, 36), randint(-800, -200), 58, 128, "optimys_prime/автомобіль_бот.png", 4))
        car1.append(CAR(randint(107, 107), randint(-200, -200), 58, 128, "optimys_prime/автомобіль_бот_2.png", 4))
        car1.append(CAR(randint(185, 185), randint(-600, -200), 58, 128, "optimys_prime/автомобіль_бот.png", 4))
        car1.append(CAR(randint(419, 419), randint(-400, -200), 58, 128, "optimys_prime/автомобіль_бот_2.png", 4))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        roket.draw(window)
        for car in car1:
            car.draw(window)
            car.move()
        roket.move()
        pygame.display.flip()
        fps.tick(30)
        window.blit(bacground, (5, 5))

start_game()