colour = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
pygame.draw.rect(screen, RED, (0,0, 25,25), 0)
pygame.draw.rect(screen, BLUE, (25,0, 25,25), 0)
sizeFont = pygame.font.SysFont("Arial", 10)
size1Text = sizeFont.render("1", True, BLACK)
size2Text = sizeFont.render("2", True, BLACK)
screen.blit(size1Text, (700, 0))
screen.blit(size2Text, (725, 0))

redRect = pygame.Rect(0, 0, 25, 25)
blueRect = pygame.Rect(25, 0, 25, 25)
size1 = pygame.Rect(700, 0, 25, 25)
size2 = pygame.Rect(725, 0, 25, 25)

#in loop for getting events

while ...
  if event.type == pygame.MOUSEBUTTONDOWN:
    mousePos = pygame.mouse.get_Pos()
    if mousePos == redRect:
      colour = RED
    elif mousePos == blueRect:
      colour = BLUE
    elif mousePos == size1:
      squareSize = (10, 10)
    elif mousePos == size2:
      squareSize = (20, 20)
    elif mousePos != redRect || mousePos != blueRect:
      pygame.draw.rect(screen, colour, (mousePos, squareSize), 0)
