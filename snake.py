from pygame.locals import *
from random import randint
import pygame
import time
import random
from SnakeClass import *
from Food import *
from tkinter import *
from tkinter import messagebox


pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.SysFont("arial",24)
clock = pygame.time.Clock()
game_over = False
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
kwadrat = 15
spawn_food = False
width = 800
height = 600
Window = pygame.display.set_mode((width, height))
snake = Snake()
food = Food()
score = 0

myfont = pygame.font.SysFont("Comic Sans MS", 30)

label = myfont.render("Press Y to restart,Q to exit", True, white)
def ster():
    current_time = time.time()
    while time.time() - current_time < 0.3:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.old_dir != 'right':
                    snake.dir = 'left'
                elif event.key == pygame.K_RIGHT and snake.old_dir != 'left':
                    snake.dir = 'right'
                elif event.key == pygame.K_UP and snake.old_dir != 'down':
                    snake.dir = 'up'
                elif event.key == pygame.K_DOWN and snake.old_dir != 'up':
                    snake.dir = 'down'
restart = True
if restart == False:
        response = messagebox.askquestion("Restart?","Restart?")
        if response == "yes":
            restart == True
            snake = Snake()
            food = Food()
        else:
            pass
reset_flag = False
while restart == True:

    Window.fill(black)
    pygame.draw.line(Window, white, (0, 0), (0, 600), 5)
    pygame.draw.line(Window, white, (0, 0), (800, 0), 5)
    pygame.draw.line(Window, white, (800,0), (800, 600), 5)
    pygame.draw.line(Window, white, (0,600), (800, 600), 5)
    if(reset_flag):
        Window.blit(label,(200,200))
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_y):
                    reset_flag = False
                if (event.key == pygame.K_q):
                    quit(0)
        pygame.display.update()
        clock.tick(5)
        continue
    ster()
    snake.move()
    score_label = myfont.render(f"score:{score}", True, white)
    Window.blit(score_label, (10, 10))
    if snake.collision() or snake.collision_with_snake():
        snake = Snake()
        food = Food()
        reset_flag = True
        score = 0
    if_eat =snake.eat(food)
    if (if_eat):
        score+=1
    pygame.draw.rect(Window, red, (food.wspX * kwadrat-1, food.wspY * kwadrat-1, kwadrat-2, kwadrat-2))
    for i in range(len(snake.wspX)):
        pygame.draw.rect(Window, blue, (snake.wspX[i] * kwadrat-1, snake.wspY[i] * kwadrat-1, kwadrat-2, kwadrat-2))
    pygame.display.update()
    clock.tick(10)
