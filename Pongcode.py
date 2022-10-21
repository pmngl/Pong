#First you establish basics fundamental python pygame logic
#which means importing and initializing pygame and the running time(update)
#then we can create a main window, which is called display window
#Now we can create the vars for the player and ball size and where they are placed inside the display window
#we create two colours vars for later
#then we draw the rectangles with the Rect function and the ball with the elipse
#we create this in the while loop so the programm always does update our code
#be cautionaus to always choose the right reverted hierarchy to display your shapes on the display
#we create now the speed variables for our animations and movement
#to create an animation we need to continously update our code with the new variables
#the ball moves now, but out of frame so we need to create borders
#Our borders are created in a way that the ball will change momentum once it reaches
#either the side or the bottom or top of the screen and then revert mov * -1
#the same is true for our player models
#to keep track we will seperate the function the ball function into a seperate one for easier access


#imported packages / sys because of VS code
import sys
import pygame
import random

#general setup
pygame.init()
clock = pygame.time.Clock()

#we want to move the ball in the while loop by the amount we set as a var
#we do this like this:
#we put this var then into the while loop like the "for" indentation otherwise the ball would only update once we mouve the mouse
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

#to create borders for our game lets define these
#this variable below checks if the ball is outside of the frame and if so changes the speed of the ball to the var -1 in either x or y
#watch out to not use == since this would interfere with the screen and would create a bug. Use <=
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
        
#now we can add the collision to the characters
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
        
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
    
#setting main window up
screen_width = 1280
screen_height = 960
#display surface, window we play in
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#You have regular surface display surface
#we dra a rectangle now (rect) around an shape
#Top left is = x,y 0

#Ball is 30 pixel wide and heigth
#Ball is placed in the middle of the screen 
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)

#Player is middle of right side / ITS ALWAYS X THEN Y
player = pygame.Rect(screen_width - 20, screen_height / 2, 10, 140 )

#Opponent is  
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

#Color are RGB valued, Red/Green/Blue = Pure Red = 255, 0, 0
#Color can also be defined as a Object pygame.color("name") = name is red or green or blue 
bg_color = pygame.Color("gray12")
light_grey = (200, 200, 200)

#Variables for movement
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

#Its important to call our drawings in the while loop to update our screens

while True:
#Handling the input / Pygame calls every user input an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#1. Declare player speed variable
#2. add this speed to the player on every frame
#3. if no button is pressed, nothing happens
#4. button pressed = player speed becomes positiv or negativ
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    ball_animation()
    player_animation()
    opponent_ai()   
    
#Its very important to arrange the elements in the a reverted hierarchy so that the
#things that should be drawn the last are at the top
#do update the background continously we fill the screen with a colour
    screen.fill(bg_color)
#For drawing you need a surface, color and rect pygame.draw(surface, color, rect)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
#we can also use ellipse for round shapes / ellpise is okay because our sides are all the same lenght and width
    pygame.draw.ellipse(screen, light_grey, ball)
#drawing a line in the middle
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

#Update window
    pygame.display.flip()
#clock = times the computer runs the update per second
    clock.tick(60)
    
