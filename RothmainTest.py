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

fontText = pygame.font.SysFont("Arial", 40)

def menu():
    
    testText = fontText.render("testing", True, BLACK)
    quitText = fontText.render("quit", True, BLACK)
    testPosition = testText.get_rect()
    testPosition.centerx = screen.get_rect().centerx
    testPosition.centery = screen.get_rect().centery - 200
    quitPosition = quitText.get_rect()
    quitPosition.centerx = screen.get_rect().centerx
    quitPosition.centery = screen.get_rect().centery
    screen.blit(testText, testPosition)
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
                    
    pygame.quit()

def paint():
    #pygame.init()
    colour = (0, 0, 0) 
    RED = (255, 0, 0) 
    BLUE = (0, 0, 255) 
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, RED, (0,0, 25,25), 0)
    pygame.draw.rect(screen, BLUE, (25,0, 25,25), 0)
    sizeFont = pygame.font.SysFont("Arial", 10)
    size1Text = sizeFont.render("1", True, BLACK)
    size2Text = sizeFont.render("2", True, BLACK)
    size3Text = sizeFont.render("3", True, BLACK)
    screen.blit(size1Text, (700, 0))
    screen.blit(size2Text, (725, 0))
    screen.blit(size3Text, (750, 0))

    redRect = pygame.Rect(0, 0, 25, 25)
    blueRect = pygame.Rect(25, 0, 25, 25)
    size1 = pygame.Rect(700, 0, 25, 25)
    size2 = pygame.Rect(725, 0, 25, 25)
    size3 = pygame.Rect(750, 0, 25, 25)
    
    pygame.display.update()

    squareSize = (10,10)
    
    done = False
    while not done:
        for event in pygame.event.get():
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT: 
                done = True
            elif pressed1 == 1:
                #mousePos = pygame.mouse.get_pos()
                if redRect.collidepoint(mousePos):
                    colour = RED
                elif blueRect.collidepoint(mousePos):
                    colour = BLUE
                elif size1.collidepoint(mousePos):
                    squareSize = (10, 10)
                elif size2.collidepoint(mousePos):
                    squareSize = (20, 20)
                elif size3.collidepoint(mousePos):
                    squareSize = (30, 30)
                elif redRect.collidepoint(mousePos) == False and blueRect.collidepoint(mousePos) == False and size1.collidepoint(mousePos) == False and size2.collidepoint(mousePos) == False and size3.collidepoint(mousePos) == False:
                    pygame.draw.rect(screen, colour, (mousePos, squareSize), 0)
                    pygame.display.update()
            elif pressed3 == 1:
                if redRect.collidepoint(mousePos) == False and blueRect.collidepoint(mousePos) == False and size1.collidepoint(mousePos) == False and size2.collidepoint(mousePos) == False and size3.collidepoint(mousePos) == False:
                    pygame.draw.rect(screen, WHITE, (mousePos, squareSize), 0)
                    pygame.display.update()
                    
    pygame.quit()

def wierd():
    
    done = False
    while not done:
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

menu()
