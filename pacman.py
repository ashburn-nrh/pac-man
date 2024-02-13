import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5

# Enemy
enemy_size = 30
enemy_speed = 3
enemy_list = []

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player with arrow keys
    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
    player_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # Keep player within the screen boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # Create enemies
    if random.randint(1, 100) < 5:  # Adjust the probability based on your preference
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = random.randint(0, HEIGHT - enemy_size)
        enemy_list.append([enemy_x, enemy_y])

    # Move enemies
    for enemy in enemy_list:
        enemy[0] += random.randint(-enemy_speed, enemy_speed)
        enemy[1] += random.randint(-enemy_speed, enemy_speed)

        # Keep enemies within the screen boundaries
        enemy[0] = max(0, min(WIDTH - enemy_size, enemy[0]))
        enemy[1] = max(0, min(HEIGHT - enemy_size, enemy[1]))

    # Collision check
    for enemy in enemy_list:
        if (
            player_x < enemy[0] + enemy_size
            and player_x + player_size > enemy[0]
            and player_y < enemy[1] + enemy_size
            and player_y + player_size > enemy[1]
        ):
            print("Game Over!")
            running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
