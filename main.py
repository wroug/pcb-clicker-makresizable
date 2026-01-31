import pygame
import json
from modules.settings import settings
from modules.upgrades import upgrades_menu

# Pygame Setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
my_font = pygame.font.Font("Kavoon-Regular.ttf", 40)
pcb_image = pygame.image.load("pcb.jpg")
pcb_image = pygame.transform.scale(pcb_image, (300, 300))
pcb_rect = pygame.Rect(1280 / 9, 720 / 3, 300, 300)
upgrades_image = pygame.image.load('Upgrades.png')
upgrades_image = pygame.transform.scale(upgrades_image, (50, 50))
upgrades_rect = pygame.Rect(1050, 50, 50, 50)
settings_image = pygame.image.load('Settings.png')
settings_image = pygame.transform.scale(settings_image, (50, 50))
settings_rect = pygame.Rect(1150, 50, 50, 50)
back_rect = pygame.Rect(50, 50, 150, 50)
back_from_upg = pygame.Rect(50, 600, 150, 50)
mint_btn = pygame.Rect(50, 150, 1160, 60)
sky_btn = pygame.Rect(50, 230, 1160, 60)
sand_btn = pygame.Rect(50, 310, 1160, 60)
save_rect = pygame.Rect(50, 450, 1160, 60)
import_rect = pygame.Rect(50, 530, 1160, 60)
upgrade_1_rect = pygame.Rect(50, 150, 1180, 80)
pcb = 0
pcb_per_click = 1
upg1_owned = 0
bg_color = (20, 20, 25)
menu_open = False
upgrades_open = False
show_save_text = False
save_message_timer = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if upgrades_open:
                if back_from_upg.collidepoint(event.pos):
                    upgrades_open = False

                if upgrade_1_rect.collidepoint(event.pos):
                    if pcb >= 50:
                        pcb -= 50
                        pcb_per_click += 1
                        print("Upgrade Purchased!")
                    else:
                        print("Not enough PCBs.")

            elif menu_open:
                if back_rect.collidepoint(event.pos):
                    menu_open = False

                # Save Functionality
                if save_rect.collidepoint(event.pos):
                    import json

                    data = {
                        "pcb": pcb,
                        "bg": bg_color,
                        "click_power": pcb_per_click
                    }
                    with open("savegame.json", "w") as f:
                        json.dump(data, f)
                    show_save_text = True
                    save_message_timer = 90
                    print("Game saved!")

                # Import Functionality
                if import_rect.collidepoint(event.pos):
                    try:
                        with open("savegame.json", "r") as f:
                            data = json.load(f)
                            pcb = data.get("pcb", 0)
                            pcb_per_click = data.get("click_power", 1)
                            bg_color = tuple(data["bg"])
                        print("Game loaded!")
                    except FileNotFoundError:
                        print("No Save file found")

                # Theme Colors
                if mint_btn.collidepoint(event.pos):
                    bg_color = (20, 60, 40)
                if sky_btn.collidepoint(event.pos):
                    bg_color = (20, 40, 60)
                if sand_btn.collidepoint(event.pos):
                    bg_color = (40, 20, 40)

            # 3. LOGIC FOR MAIN GAME (NO MENUS OPEN)
            else:
                if upgrades_rect.collidepoint(event.pos):
                    upgrades_open = True
                elif settings_rect.collidepoint(event.pos):
                    menu_open = True
                elif pcb_rect.collidepoint(event.pos):
                    pcb += pcb_per_click

    # --- DRAWING ---
    if menu_open:
        settings(screen)
    elif upgrades_open:
        upgrades_menu(screen, my_font, pcb, pcb_per_click)
    else:
        screen.fill(bg_color)
        screen.blit(pcb_image, pcb_rect)
        screen.blit(settings_image, settings_rect)
        screen.blit(upgrades_image, upgrades_rect)

        # Score Display
        text_surface = my_font.render(f"{pcb} PCBs", True, (255, 255, 255))
        screen.blit(text_surface, (100, 50))

        # Save Message Notification
        if show_save_text and save_message_timer > 0:
            msg_surf = my_font.render("GAME SAVED!", True, (0, 255, 100))
            screen.blit(msg_surf, (500, 600))
            save_message_timer -= 1
        elif save_message_timer <= 0:
            show_save_text = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()