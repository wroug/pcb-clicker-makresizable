import pygame


def settings(screen):
    screen.fill((30, 30, 45))
    pygame.draw.rect(screen, "red", (50, 50, 150, 50))

    pygame.draw.rect(screen, (150, 0, 0), (50, 50, 150, 50), border_radius=5)
    pygame.draw.rect(screen, (20, 60, 40), (50, 150, 1160, 60))
    pygame.draw.rect(screen, (20, 40, 60), (50, 230, 1160, 60))
    pygame.draw.rect(screen, (40, 20, 40), (50, 310, 1160, 60))