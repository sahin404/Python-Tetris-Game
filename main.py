import pygame, sys
from game import Game

pygame.init()
title_font = pygame.font.Font(None, 40)
#Score Serface
score = title_font.render("Score", True, (255,255,255))
score_rect = pygame.Rect(320,85,170,60)
#Next Shape Sarface
next_shape = title_font.render("Next", True, (255,255,255))
next_shape_rect = pygame.Rect(320,250,170,180)

#Window Color
dark_blue = (44,44,110)

#game Structure
display  = pygame.display.set_mode((500,620))

pygame.display.set_caption("Tetris Game")
clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 150)
#Game Loop 1. Event Handling, 2. Updating position, 3. Drawing Updating position
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                game.score=0
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over==False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over==False:
                game.move_rotation()
        if event.type == GAME_UPDATE and game.game_over==False:
            game.move_down()

    score_update = title_font.render(str(game.score), True, (255,255,255))
    display.fill(dark_blue)

    #Score Title and Rectangle Print
    display.blit(score, (365,50,50,50))
    pygame.draw.rect(display, (59,85,162), score_rect, 0 , 10)

    #Next Shape Title Print
    display.blit(next_shape, (375, 215, 50, 50))

    #Score Print
    display.blit(score_update, score_update.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

    #Next shape Rectangle print
    pygame.draw.rect(display, (59, 85, 162), next_shape_rect, 0, 10)

    game.draw(display)

    pygame.display.update()
    clock.tick(60)

