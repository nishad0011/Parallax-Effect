import pygame
import math

pygame.init()

#SCREEN
screen_width = 800
screen_height = 604
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Parallax Scroll") #WINDOW TITLE

clock = pygame.time.Clock()


#FONT
font = pygame.font.Font("freesansbold.ttf", 32)

#ASSETS
background = [
			[pygame.image.load("./800p/_11_background.png").convert_alpha()			,0,0,0],
			[pygame.image.load("./800p/_10_distant_clouds.png").convert_alpha()		,0,0,1],
			[pygame.image.load("./800p/_09_distant_clouds1.png").convert_alpha()	,0,0,2],
			[pygame.image.load("./800p/_08_clouds.png").convert_alpha()				,0,0,3],
			[pygame.image.load("./800p/_07_huge_clouds.png").convert_alpha()		,0,0,4],
			[pygame.image.load("./800p/_06_hill2.png").convert_alpha()				,0,0,5],
			[pygame.image.load("./800p/_05_hill1.png").convert_alpha()				,0,0,6],
			[pygame.image.load("./800p/_04_bushes.png").convert_alpha()				,0,0,7],
			[pygame.image.load("./800p/_03_distant_trees.png").convert_alpha()		,0,0,8],
			[pygame.image.load("./800p/_02_trees and bushes.png").convert_alpha()	,0,0,9],
			[pygame.image.load("./800p/_01_ground.png").convert_alpha()				,0,0,10],
			]

#GAME VARIABLES
bg_width = background[0][0].get_width()
bg_asset_count = len(background)

scroll_value = 0
no_of_tiles = math.ceil(screen_width/background[0][0].get_width())

#update display
def display_update():
	# fill the screen with a color to wipe away anything from last frame
	screen.fill("white")

	# RENDER YOUR GAME HERE	
	for i in range(bg_asset_count):
		for tile in range(-1,no_of_tiles+1):
			screen.blit(background[i][0], (background[i][1]+(background[i][0].get_width()*tile) , 0))

	#FPS METER
	fps = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
	screen.blit( fps , (700 , 15))

	# flip() the display to put your work on screen
	pygame.display.flip()

	clock.tick(60)  # limits FPS


if __name__ == "__main__" :
	running = True
	while running:
		# poll for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					scroll_value = 1

				elif event.key == pygame.K_RIGHT:
					scroll_value = -1

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					scroll_value = 0

		for i in range(bg_asset_count):
			background[i][1] += scroll_value * background[i][3]
			if abs(background[i][1]) > bg_width:
				background[i][1] = 0

		display_update()

	
pygame.quit()

