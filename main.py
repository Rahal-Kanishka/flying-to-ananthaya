# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import sys
import os

worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

# initialize pygame
pygame.init()

width = 1000
height = 800
vel = 10
x = 200
y = 200
moves_count = 0
target_x = width / 2
target_y = height - 50

screen_res = (width, height)

pygame.display.set_caption("Ball-game")
screen = pygame.display.set_mode(screen_res)

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 255)
orange = (255, 100, 0)

Font = pygame.font.SysFont('timesnewroman', 18)
section_header = Font.render("Information", False, orange, yellow)

# defining the ball
# ball_obj = pygame.draw.circle(
#     surface=screen, color=red, center=[100, 100], radius=40)
# moving the ball
speed = [0, 1]

# header
screen.blit(section_header, (width - 22, 0))
# %%

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(black)
    # ball_obj = ball_obj.move(speed)

    # stores keys pressed
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        print('key left')
        # decrement in x co-ordinate
        x -= vel
        moves_count += 1

        # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < width:
        print('key right', x, y)

        # increment in x co-ordinate
        x += vel
        moves_count += 1

        # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        print('key up', x, y)
        # decrement in y co-ordinate
        y -= vel
        moves_count += 1
        # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < height:
        print('key down', x, y)
        # increment in y co-ordinate
        y += vel
        moves_count += 1

    circle = pygame.draw.circle(surface=screen, color=red, center=[x, y], radius=30)

    # target
    target = pygame.draw.rect(screen, yellow, (target_x, target_y, 80, 20))

    collide = pygame.Rect.colliderect(circle,
                                      target)
    game_won = Font.render("Reach target: " + str(collide), False, white, black)

    left_width = Font.render("left space: " + str(x), False, white, black)

    right_width = Font.render("right space: " + str(width - x), False, white, black)

    top_width = Font.render("top space: " + str(y), False, white, black)

    bottom_width = Font.render("bottom space: " + str(height - y), False, white, black)

    moves = Font.render("pixel moves: " + str(moves_count), False, white, black)

    # to target
    left_target = Font.render("left to target: " + str(0 if (x - target_x) < 0 else (x - target_x)), False, white, black)

    right_target = Font.render("right to target: " + str(0 if (target_x - x) < 0 else (target_x - x)), False, white, black)

    current = Font.render("X: "  + str(x) + " Y: " + str(y), False, white, black)

    bottom_width = Font.render("bottom space: " + str(height - y), False, white, black)

    screen.blit(game_won, (width - 200, 20))
    screen.blit(left_width, (width - 200, 40))
    screen.blit(right_width, (width - 200, 60))
    screen.blit(top_width, (width - 200, 80))
    screen.blit(bottom_width, (width - 200, 100))
    screen.blit(moves, (width - 200, 120))
    screen.blit(left_target, (width - 200, 140))
    screen.blit(right_target, (width - 200, 160))
    screen.blit(current, (width - 200, 180))

    # information section
    pygame.display.flip()
# %%
