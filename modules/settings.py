import pygame


def settings(screen):
    screen.fill((30, 30, 40))
    pygame.draw.rect(screen, "red", (50, 50, 150, 50))
    btn_font = pygame.font.Font("Kavoon-Regular.ttf", 40)

    pygame.draw.rect(screen, (150, 0, 0), (50, 50, 150, 50), border_radius=5)
    back_txt = btn_font.render("BACK", True, (200, 200, 200))
    screen.blit(back_txt, (70, 50))
    pygame.draw.line(screen, (100, 100, 100), (50, 220), (1210, 220), 1)
    pygame.draw.line(screen, (100, 100, 100), (50, 300), (1210, 300), 1)
    text_surface = btn_font.render("Select color: Dark green", True, (200, 200, 200))
    screen.blit(text_surface, (70, 155))
    text_surface = btn_font.render("Select color: Dark Blue", True, (200, 200, 200))
    screen.blit(text_surface, (70, 235))
    text_surface = btn_font.render("Select color: Dark Purple", True, (200, 200, 200))
    screen.blit(text_surface, (70, 315))
    pygame.draw.rect(screen, (50, 50, 50), (50, 450, 1160, 60))
    save_text = btn_font.render("SAVE GAME", True, (200, 200, 200))
    screen.blit(save_text, (510, 454))
    pygame.draw.rect(screen, (50, 50, 50), (50, 530, 1160, 60))
    import_text = btn_font.render("IMPORT SAVE", True, (200, 200, 200))
    screen.blit(import_text, (490, 534))