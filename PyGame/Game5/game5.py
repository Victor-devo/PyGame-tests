import pygame as pg
pg.init()

#valores iniciais
screen_width = 800
screen_height = 500
run = True

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('RPG battle')

#load images
back_img = pg.image.load('PyGame-tests/PyGame/Game5/img/Background-P.png').convert_alpha()
def draw_bg():
    screen.blit(back_img, (0,0))

while run:
    draw_bg()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()




pg.quit()