import pygame


def upgrades_menu(screen, my_font, pcb_count, pcb_per_click, auto_solderer_cost):
    screen.fill((25, 25, 35))

    # Show stats at the top
    stats_text = my_font.render(f"PCBs: {pcb_count} | Power: {pcb_per_click}", True, (255, 255, 255))
    screen.blit(stats_text, (50, 20))

    # Auto Solderer Button
    button_rect = pygame.Rect(50, 150, 1180, 80)
    pygame.draw.rect(screen, (60, 60, 60), button_rect, border_radius=10)
    pygame.draw.rect(screen, (100, 100, 100), button_rect, 2, border_radius=10)

    upg_text = my_font.render(f"Auto Solderer | Cost: {auto_solderer_cost} PCBs | +1 PCB/click", True, (200, 200, 200))
    screen.blit(upg_text, (80, 165))

    # Back Button
    pygame.draw.rect(screen, (150, 0, 0), (50, 600, 150, 50), border_radius=5)
    back_txt = my_font.render("BACK", True, (255, 255, 255))
    screen.blit(back_txt, (75, 602))
