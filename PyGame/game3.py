import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect((100, 400, 50, 50))
player2 = pygame.Rect((400, 400, 50, 50))
run = True
while run:
    pygame.draw.rect(screen, (255, 0, 0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    pygame.draw.rect(screen, (0, 0, 255), player2)
    key = pygame.key.get_pressed()
    if key[pygame.K_j] == True:
        player2.move_ip(-1, 0)
    elif key[pygame.K_l] == True:
        player2.move_ip(1, 0)
    elif key[pygame.K_k] == True:
        player2.move_ip(0, 1)
    elif key[pygame.K_i] == True:
        player2.move_ip(0, -1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()