import pygame
from modules.settings import settings

# Pygame Setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
my_font = pygame.font.Font("Kavoon-Regular.ttf", 40)
pcb_image = pygame.image.load("pcb.jpg")
pcb_image = pygame.transform.scale(pcb_image, (300, 300))
pcb_rect = pygame.Rect(1280 / 9, 720 / 3, 300, 300)
settings_image = pygame.image.load('Settings.png')
settings_image = pygame.transform.scale(settings_image, (50, 50))
settings_rect = pygame.Rect(1200, 40, 50, 50)
back_rect = pygame.Rect(50, 50, 150, 50)
mint_btn = pygame.Rect(50, 150, 1160, 60)
sky_btn = pygame.Rect(50, 230, 1160, 60)
sand_btn = pygame.Rect(50, 310, 1160, 60)
save_rect = pygame.Rect(50, 450, 1160, 60)
import_rect = pygame.Rect(50, 530, 1160, 60)
save_message_timer = 0
show_save_text = False
menu_open = False
bg_color = (20, 20, 25)  # Initial Dark Color
pcb = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if settings_rect.collidepoint(event.pos):
                menu_open = True

            # Logic while menu is open
            if menu_open:
                if save_rect.collidepoint(event.pos):
                    import json
                    data = {"pcb": pcb, "bg": bg_color}
                    with open("savegame.json", "w") as f:
                        json.dump(data, f)
                    show_save_text = True
                    save_message_timer = 60
                    print("Game saved!")
                if import_rect.collidepoint(event.pos):
                    import json
                    try:
                        with open("savegame.json", "r") as f:
                            data = json.load(f)
                            pcb = data["pcb"]
                            bg_color = tuple(data["bg"])
                        print("Game loaded!")
                    except FileNotFoundError:
                        print("No Save file found")
                if back_rect.collidepoint(event.pos):
                    menu_open = False

                # Update background color based on button clicked
                if mint_btn.collidepoint(event.pos):
                    bg_color = (20, 60, 40)
                if sky_btn.collidepoint(event.pos):
                    bg_color = (20, 40, 60)
                if sand_btn.collidepoint(event.pos):
                    bg_color = (40, 20, 40)

            # Logic while game is active
            else:
                if pcb_rect.collidepoint(event.pos):
                    pcb += 1

    # --- DRAWING ---
    if menu_open:
        settings(screen)
    else:
        screen.fill(bg_color)
        screen.blit(pcb_image, pcb_rect)
        screen.blit(settings_image, settings_rect)

        text_surface = my_font.render(f"{pcb} PCBs", True, (255, 255, 255))
        screen.blit(text_surface, (100, 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()