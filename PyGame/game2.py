import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect(100, 200, 50, 50)
clock = pygame.time.Clock()
run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(0, 255, 0), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(180)
pygame.quit()