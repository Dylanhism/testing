colour = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

#in loop for getting events
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      mousePos = pygame.mouse.get_Pos()
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
    elif event.type == pygame.QUIT:
      done = True
pygame.QUIT()
