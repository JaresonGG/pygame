import pygame
import sys

pygame.init()

WIDTH, HEIGTH = 800, 600
PLAYER_SIZE = 50
PLATFORM_SIZE = 100
PLAYER_COLOR = (255, 0, 0)
PLATFORM_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
GRAVITY = 1
JUMP_HEIGTH = 15

screen = pygame.display.set_mode((WIDTH, HEIGTH))

player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2 - PLAYER_SIZE // 2, PLAYER_SIZE // 2 - PLAYER_SIZE // 2, PLAYER_SIZE)
player_speed = 5
player_y_speed = 0

platforms = [
    pygame.Rect(WIDTH // 2 - PLAYER_SIZE, 400, PLATFORM_SIZE, 15),
    pygame.Rect(600, 400, PLATFORM_SIZE, 15),
    pygame.Rect(600, 400, PLATFORM_SIZE, 15)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
