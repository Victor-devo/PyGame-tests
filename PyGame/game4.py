import pygame as pg
import random

pg.init()

#medidas
screen_width = 600
screen_height = 600
cell_size = 10
direction = 1 #1 é para cima, 2 é para a direita, 3 é para baixo e 4 é para a esquerda
food = [0, 0]
new_food = True
new_piece = [0,0]
game_over = False
click = False
score = 0

#cores
bg =(255, 200, 100)
body_inner = (50, 175, 25)
body_outer = (100, 200, 100)
red = (250, 20, 20)
food_c = (250, 50, 50)

#definição de posições
screen = pg.display.set_mode((screen_width, screen_height))
snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 3])

#framerate, loop condition and caption
pg.display.set_caption('snake')
clock = pg.time.Clock()
run = True
#fonte
font = pg.font.SysFont(None, 40)
#botão
again_rect = pg.Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

def draw_screen():
    screen.fill(bg)
def draw_score():
    score_txt = 'Score: ' + str(score)
    score_img = font.render(score_txt, True, (0, 0, 0))
    screen.blit(score_img, [0,0])
def check_game_over(game_over):
    head_count = 0
    for segment in snake_pos:
        if snake_pos[0] == segment and head_count > 0:
            game_over = True
        head_count += 1
    if snake_pos[0][0] < -2 or snake_pos[0][0] > screen_width + 2 or snake_pos[0][1] < -2 or snake_pos[0][1] > screen_height + 2:
        game_over = True
    return game_over
def draw_game_over():
    over_txt = 'Game Over!'
    over_img = font.render(over_txt, True, (0,0,0))
    pg.draw.rect(screen, red, (screen_width // 2 - 80, screen_height // 2 - 60, 160, 50))
    screen.blit(over_img, (screen_width // 2 - 80, screen_height // 2 - 50))
    again_txt = 'Play again?'
    again_img = font.render(again_txt, True, (0,0,0))
    pg.draw.rect(screen, red, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))

#game loop
while run:
    #proucurando eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w and direction != 3:
                direction = 1
            if event.key == pg.K_d and direction != 4:
                direction = 2
            if event.key == pg.K_s and direction != 1:
                direction = 3
            if event.key == pg.K_a and direction != 2:
                direction = 4
    draw_screen()
    draw_score()
    #desenhando a cobra
    head = 1
    for x in snake_pos:
        if head == 0:
            pg.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pg.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2 , cell_size - 2))
        if head == 1:
            pg.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pg.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2 , cell_size - 2))
            head = 0
    #movendo a cobra
    if game_over == False:
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size
        game_over = check_game_over(game_over)
    else:
        draw_game_over()
        if event.type == pg.MOUSEBUTTONDOWN and click == False:
            click = True
        if event.type == pg.MOUSEBUTTONDOWN and click == True:
            click = False
            pos = pg.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #resetar o jogo
                direction = 1 #1 é para cima, 2 é para a direita, 3 é para baixo e 4 é para a esquerda
                food = [0, 0]
                new_food = True
                new_piece = [0,0]
                game_over = False
                score = 0
                snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
                snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
                snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
                snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 3])



    #gerando a comida
    if new_food == True:
        food[0] = cell_size * random.randint(0, (screen_width // cell_size) - 1)
        food[1] = cell_size * random.randint(0, (screen_height // cell_size) - 1)
        new_food = False
    pg.draw.rect(screen, food_c, (food[0], food[1], cell_size, cell_size))

    #colisão
    if snake_pos[0] == food:
        new_food = True
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 4:
            new_piece[0] += cell_size
        #adicionando o novo pedaço à cobra
        snake_pos.append(new_piece)
        #adicionando score
        score += 1

    #update e framerate
    pg.display.update()
    clock.tick(20)
pg.quit()