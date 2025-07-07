import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 50
player_x = 100
player_y = HEIGHT - player_height
velocity_y = 0
jump = False
gravity = 1

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height
obstacle_speed = 5

# Clock
clock = pygame.time.Clock()
Main game loop
running = True
while running:
    clock.tick(60)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Jumping logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jump:
        jump = True
        velocity_y = -15

    if jump:
        player_y += velocity_y
        velocity_y += gravity
        if player_y >= HEIGHT - player_height:
            player_y = HEIGHT - player_height
            jump = False

    # Obstacle movement
    obstacle_x -= obstacle_speed
    if obstacle_x < 0:
        obstacle_x = WIDTH

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False

    # Draw player and obstacle
    pygame.draw.rect(win, BLACK, player_rect)
    pygame.draw.rect(win, RED, obstacle_rect)

    pygame.display.update()

pygame.quit()