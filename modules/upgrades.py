import pygame


def upgrades_menu(screen, my_font, pcb_count):
    screen.fill((25, 25, 35))  # Dark background

    # Show current balance
    balance_surf = my_font.render(f"PCBs: {pcb_count}", True, (255, 255, 255))
    screen.blit(balance_surf, (50, 20))

    button_rect = pygame.Rect(50, 150, 1180, 80)
    pygame.draw.rect(screen, (60, 60, 60), button_rect, border_radius=10)  # Button fill
    pygame.draw.rect(screen, (100, 100, 100), button_rect, 2, border_radius=10)  # Border

    upg_text = my_font.render("Auto Solderer | Cost: 50 PCBs | +1 PCB/click", True, (200, 200, 200))
    screen.blit(upg_text, (80, 165))

    pygame.draw.rect(screen, (150, 0, 0), (50, 600, 150, 50), border_radius=5)
    back_txt = my_font.render("BACK", True, (255, 255, 255))
    screen.blit(back_txt, (75, 602))