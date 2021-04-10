import pygame
import sys
import random

class Bird(object):
    """Define a class bird"""
    def __init__(self):
        """Define the initialization method"""
        self.birdRect = pygame.Rect(65, 50, 50, 50) # rectangular for the bird
        # Defines a list of three states for the bird
        self.birdStatus = [pygame.image.load("assets/1.png"),
                            pygame.image.load("assets/2.png"),
                            pygame.image.load("assets/dead.png")]   
        self.status = 0     # Default flight condition
        self.birdX = 120    # The bird's X-axis, that's how fast it's going to the right             
        self.birdY = 350    # The bird is on the Y-axis, which is the flying height up and down
        self.jump = False   # The bird lands automatically by default
        self.jumpSpeed = 10 # Jumping height 
        self.gravity = 0.1    # The force of gravity  
        self.dead = False   # Default bird health status is alive

    def birdUpdate(self):
        if self.jump:
            # Birds jump
            self.jumpSpeed -= 1             # It goes down, it goes up slower and slower
            self.birdY -= self.jumpSpeed    # The bird goes down, the bird goes up  
        else:   
            # The bird falls
            self.gravity += 0.1             # Gravity increases, it drops faster and faster
            self.birdY += self.gravity      # The bird's Y-axis goes up, the bird goes down
        self.birdRect[1] = self.birdY       # Change the Y position

class Pipeline(object):
    """Define a pipe class"""
    def __init__(self):
        """Define the initialization method"""
        self.wallx    = 400;    # The X-axis of the pipe
        self.pineUp   = pygame.image.load("assets/top.png")
        self.pineDown = pygame.image.load("assets/bottom.png")
        
    def updatePipeline(self):
        """"Pipeline movement method"""
        self.wallx -= 5       # The X axis of the pipe decreases, that is, the pipe moves to the left
        # When the pipe reaches a certain position, that is, the bird flies over the pipe, the score is increased by 1, and the pipe is reset
        if self.wallx < -80: 
            global score 
            score += 1
            self.wallx = 400

def createMap():
    """Define how to create a map"""
    screen.fill((255, 255, 255))      # Fill color
    screen.blit(background, (0, 0))   # Fill in the background

    # According to pipe
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,-300));    # Coordinate position of upper pipeline
    screen.blit(Pipeline.pineDown,(Pipeline.wallx,500)); # Lower pipe coordinate position
    Pipeline.updatePipeline()      # update pipeline movement

    # display the bird
    if Bird.dead:           # Pipe impact condition
        Bird.status = 2
    elif Bird.jump:         # Take off state
        Bird.status = 1 
    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY)) # Set the coordinates of the bird    
    Bird.birdUpdate()           # bird movement

    # display the score
    screen.blit(font.render('Score:'+str(score),-1,(255, 255, 255)),(100, 50)) # Set the color and coordinate position
    pygame.display.update()     # update display

def checkDead():
    # The rectangular position of the upper pipe
    upRect = pygame.Rect(Pipeline.wallx,-300,
                         Pipeline.pineUp.get_width() - 10,
                         Pipeline.pineUp.get_height())

    # The rectangular position of the lower pipe
    downRect = pygame.Rect(Pipeline.wallx,500,
                           Pipeline.pineDown.get_width() - 10,
                           Pipeline.pineDown.get_height())    
    # Check whether the bird collides with the upper and lower pipes
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
    # Check if the bird is flying beyond the upper and lower boundaries
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True    
        return True
    else :
        return False  

def getResutl():
    final_text1 = "Game Over" 
    final_text2 = "Your final score is:  " + str(score) 
    ft1_font = pygame.font.SysFont("Cobel", 70)               # Set the font for the first line of text
    ft1_surf = font.render(final_text1, 1, (242,3,36))  # Set the first line text color
    ft2_font = pygame.font.SysFont("Cobel", 50)               # Sets the second line of text font
    ft2_surf = font.render(final_text2, 1, (253, 177, 6)) # Sets the color of the second line
    screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100]) # Sets where the first line of text will appear
    screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 200]) # Sets where the second line of text will appear
    pygame.display.flip()      # Updates the entire Surface object to be displayed to the screen

if __name__ == '__main__':
    """main program"""
    pygame.init()       # Initialize the pygame
    pygame.font.init()  # Initialize font
    font = pygame.font.SysFont("Cobel", 50)    # Set the font and size
    size   = width, height = 400, 650       # Settings window
    screen = pygame.display.set_mode(size)  #  Display window
    clock  = pygame.time.Clock()             # Set the clock
    Pipeline = Pipeline() # Instantiate the pipe class
    Bird = Bird()         # Instantiate Birds
    score = 0
    while True:
        clock.tick(60)  # Performs 60 times per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True    # jumping
                Bird.gravity = 0.1    # The force of gravity
                Bird.jumpSpeed = 10 # The speed of jumping          

        background = pygame.image.load("assets/background.png") # Load the background image
        if checkDead() : # Check the bird's life status
            getResutl()  # If the bird dies, display the total score of the game
        else :
            createMap()  # Create a map
    pygame.quit()


