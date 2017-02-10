import pygame
import pygame.locals

pygame.init()
size = (800, 600)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("WELCOME TO THE MATRIX")

bottle = pygame.image.load("Bottle.png")
pepe = pygame.image.load("happy.png")

colour = (0, 0, 0) 
RED = (255, 0, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 

screen.fill(WHITE)
pygame.display.update()
done = False
rotate = 0

#all_fonts = pygame.font.get_fonts()
#print all_fonts

tinyText = pygame.font.SysFont("comicsansms", 10)
fontText = pygame.font.SysFont("Arial", 40)
bigText = pygame.font.SysFont("Arial", 60)

def menu():
    pygame.mixer.init()
    pygame.mixer.music.load("Mario Paint Music.mp3")
    pygame.mixer.music.stop()
    screen.fill(WHITE)
    testText = bigText.render("Paint", True, BLACK)
    quitText = fontText.render("Quit", True, BLACK)
    instructText = fontText.render("Instructions", True, BLACK)
    secretText = tinyText.render("Secret", True, BLACK)
    instructPosition = instructText.get_rect()
    instructPosition.centerx = screen.get_rect().centerx
    instructPosition.centery = screen.get_rect().centery + 100
    secretPosition = secretText.get_rect()
    secretPosition.centerx = screen.get_rect().centerx + 300
    secretPosition.centery = screen.get_rect().centery + 250
    testPosition = testText.get_rect()
    testPosition.centerx = screen.get_rect().centerx
    testPosition.centery = screen.get_rect().centery - 100
    quitPosition = quitText.get_rect()
    quitPosition.centerx = screen.get_rect().centerx
    quitPosition.centery = screen.get_rect().centery + 200
    screen.blit(testText, testPosition)
    screen.blit(instructText, instructPosition)
    screen.blit(secretText, secretPosition)
    screen.blit(quitText, quitPosition)
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if testPosition.collidepoint(mousePos):
                    paint()
                elif quitPosition.collidepoint(mousePos):
                    done = True
                elif instructPosition.collidepoint(mousePos):
                    instruct()
                elif secretPosition.collidepoint(mousePos):
                    weird()
                    
    pygame.quit()

def paint():
    #pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Mario Paint Music.mp3")
    pygame.mixer.music.play()
    colour = (0, 0, 0) 
    RED = (255, 0, 0)
    ORANGE = (255, 102, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (204, 0, 204)
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    #((xpos, ypos, width, hieght), filling width)
    pygame.draw.rect(screen, BLACK,(0,0, 40,40), 0)
    pygame.draw.rect(screen, RED,(40,0, 40,40), 0)
    pygame.draw.rect(screen, ORANGE,(80,0, 40,40), 0) 
    pygame.draw.rect(screen, YELLOW,(120,0, 40,40), 0)
    pygame.draw.rect(screen, GREEN,(160,0, 40,40), 0)
    pygame.draw.rect(screen, CYAN,(200,0, 40,40), 0)
    pygame.draw.rect(screen, BLUE,(240,0, 40,40), 0)
    pygame.draw.rect(screen, PURPLE,(280,0, 40,40), 0)
    
    sizeFont = pygame.font.SysFont("Arial", 10)
    size1Text = sizeFont.render("1", True, BLACK)
    size2Text = sizeFont.render("2", True, BLACK)
    size3Text = sizeFont.render("3", True, BLACK)
    screen.blit(size1Text, (700, 0))
    screen.blit(size2Text, (725, 0))
    screen.blit(size3Text, (750, 0))

    blackRect = pygame.Rect(0, 0, 40, 40)
    redRect = pygame.Rect(40, 0, 40, 40)
    orangeRect = pygame.Rect(80, 0, 40, 40)
    yellowRect = pygame.Rect(120, 0, 40, 40)
    greenRect = pygame.Rect(160, 0, 40, 40)
    cyanRect = pygame.Rect(200, 0, 40, 40)
    blueRect = pygame.Rect(240, 0, 40, 40)
    purpleRect = pygame.Rect(280, 0, 40,40)
    size1 = pygame.Rect(700, 0, 25, 25)
    size2 = pygame.Rect(725, 0, 25, 25)
    size3 = pygame.Rect(750, 0, 25, 25)
    
    pygame.display.update()
    squareSize = (10,10)
    
    done = False
    while not done:
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            menu()
        for event in pygame.event.get():
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            rectSize = (mousePos[0] - squareSize[0]/2, mousePos[1] - squareSize[1]/2)
            if event.type == pygame.QUIT: 
                done = True
            elif pressed1 == True:
                if blackRect.collidepoint(mousePos):
                    colour = BLACK
                elif redRect.collidepoint(mousePos):
                    colour = RED
                elif orangeRect.collidepoint(mousePos):
                    colour = ORANGE
                elif yellowRect.collidepoint(mousePos):
                    colour = YELLOW
                elif greenRect.collidepoint(mousePos):
                    colour = GREEN
                elif cyanRect.collidepoint(mousePos):
                    colour = CYAN
                elif blueRect.collidepoint(mousePos):
                    colour = BLUE
                elif purpleRect.collidepoint(mousePos):
                    colour = PURPLE
                elif size1.collidepoint(mousePos):
                    squareSize = (10, 10)
                elif size2.collidepoint(mousePos):
                    squareSize = (20, 20)
                elif size3.collidepoint(mousePos):
                    squareSize = (30, 30)
                elif size1.collidepoint(mousePos) == False and size2.collidepoint(mousePos) == False and size3.collidepoint(mousePos) == False:
                    if blackRect.collidepoint(mousePos) == False and redRect.collidepoint(mousePos) == False and orangeRect.collidepoint(mousePos) == False and yellowRect.collidepoint(mousePos) == False:
                        if  greenRect.collidepoint(mousePos) == False and cyanRect.collidepoint(mousePos) == False and blueRect.collidepoint(mousePos) == False and purpleRect.collidepoint(mousePos) == False:
                            pygame.draw.rect(screen, colour, (rectSize, squareSize), 0)
                            pygame.display.update()
            elif pressed3 == True:
                if size1.collidepoint(mousePos) == False and size2.collidepoint(mousePos) == False and size3.collidepoint(mousePos) == False:
                    if blackRect.collidepoint(mousePos) == False and redRect.collidepoint(mousePos) == False and orangeRect.collidepoint(mousePos) == False and yellowRect.collidepoint(mousePos) == False:
                        if  greenRect.collidepoint(mousePos) == False and cyanRect.collidepoint(mousePos) == False and blueRect.collidepoint(mousePos) == False and purpleRect.collidepoint(mousePos) == False:
                            pygame.draw.rect(screen, WHITE, (rectSize, squareSize), 0)
                            pygame.display.update()
                    
    pygame.quit()

def weird():
    screen.fill(WHITE)
    sizeFont = pygame.font.SysFont("ravie", 25)
    oddText = sizeFont.render("I don't even", True, BLACK)
    screen.blit(oddText, (400,100))
    pygame.display.update()
    rotate = 0
    done = False
    while not done:
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            menu()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                screen.blit(pepe, mousePos)

        screen.blit((pygame.transform.rotate(bottle, rotate)), (100,100))
        pygame.display.update()
        rotate += 0.3
    pygame.quit()
    
def instruct():
    screen.fill((255, 255, 255))
    sizeFont = pygame.font.SysFont("Arial", 25)
    backText = sizeFont.render("->Back to menu", True, BLACK) #Text you want to appear
    instructText = sizeFont.render("Left click is to paint with colour. Left-click the colours on the top to change colour.", True, BLACK)
    instruct2Text = sizeFont.render("Left click the numbers on the top to change the brush size.", True, BLACK)
    instruct3Text = sizeFont.render("Press the escape key at any time to return to the main menu.", True, BLACK)
    inst3Position = instruct3Text.get_rect()
    inst3Position.centerx = screen.get_rect().centerx #centers text for a good look
    inst3Position.centery = screen.get_rect().centery
    inst2Position = instruct2Text.get_rect()
    inst2Position.centerx = screen.get_rect().centerx
    inst2Position.centery = screen.get_rect().centery - 100
    instPosition = instructText.get_rect()
    instPosition.centerx = screen.get_rect().centerx
    instPosition.centery = screen.get_rect().centery - 200
    backPosition = backText.get_rect()
    backPosition.centerx = screen.get_rect().centerx
    backPosition.centery = screen.get_rect().centery + 200
    screen.blit(backText, backPosition)
    screen.blit(instructText, instPosition)
    screen.blit(instruct2Text, inst2Position)
    screen.blit(instruct3Text, inst3Position)
    pygame.display.update()
    done = False
    while not done:
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if backPosition.collidepoint(mousePos):
                    menu()
                
    pygame.quit()
menu()



