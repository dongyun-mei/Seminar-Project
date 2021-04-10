# -*- coding:utf-8 -*-
import sys  # Import SYS module
import pygame  # Import the PyGame module

pygame.init()  # Initialize the pygame
size = width, height = 640, 480  # Settings game window
screen = pygame.display.set_mode(size)  # Display window
color = (241, 219, 138)  # Set the color

ball = pygame.image.load("logo.png")  # Loading pictures
background = pygame.image.load("background.png")
ballrect = ball.get_rect()  # Get the rectangular region

speed = [5, 5]  # Set the moving X - axis and Y - axis distance
clock = pygame.time.Clock()  # Set the clock
# Perform an endless loop to make sure the window is always displayed
while True:
    clock.tick(60)  # Performs 60 times per second
    # Check the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If you click to close the window, exit
            sys.exit()

    ballrect = ballrect.move(speed)  # Moving the logo
    # Hitting the left and right edges
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # Hitting the upper and lower edges
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.blit(background, (0, 0))   # Fill in the background
    screen.blit(ball, ballrect)  # Draw the picture on the window
    pygame.display.flip()  # Update all displays

pygame.quit()  # Exit the pygame
