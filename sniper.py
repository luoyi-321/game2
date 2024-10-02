import random
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
scoop = pygame.image.load("sniperGme\pic\pic\scope.png")
sx=-38
sy=-10
target=pygame.image.load("sniperGme\pic\pic\\tget.png")
tx=random.randint(50,550)
ty=random.randint(50,550)
tx_change=0
ty_change=0


def drawt():
	screen.blit(target,(tx,ty))
def draws():
	screen.blit(scoop,(sx,sy))

run=True
while run:
	
	
	
	
	screen.fill((145,200,255))
	
	
	drawt()
	draws()
	trect=pygame.draw.rect(screen, (255, 0, 0),(tx+50,ty+50,35,35))
	srect=pygame.draw.rect(screen, (255, 0, 0),(sx+335,sy+335,15,20))
	
	
	
	

	
	for event in pygame.event.get():
#        >input keys<
		if event.type == pygame.QUIT:
			run=False
		keys=pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ty_change+=5
			if event.key == pygame.K_DOWN:
				ty_change-=5
			if event.key == pygame.K_LEFT:
				tx_change+=5
			if event.key == pygame.K_RIGHT:
				tx_change-=5
				pygame.display.update()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP: 
				ty_change=0
				
			if event.key == pygame.K_DOWN:
				ty_change=0
			if event.key == pygame.K_LEFT:
				tx_change=0
			if event.key == pygame.K_RIGHT:
				tx_change=0

		if srect.colliderect(trect) and keys[pygame.K_SPACE]:
			tx=random.randint(50,550)
			ty=random.randint(50,550)



	tx+=tx_change
	ty+=ty_change
				


	pygame.display.update()