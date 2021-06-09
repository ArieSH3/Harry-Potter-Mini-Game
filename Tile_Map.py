'''
	Author: Stefan Popovic
	Date  : 04/06/2021

	About : Map grid/world for player to move in. 
			Goal is to look similar to Nintendos Pokemon and Zelda game with different biomes
			and structures to explore (Dark Forest, Hogwarts, Hogsmead ans such)
	
	TODO  : 
		- Figure out how to set up different sprite blocks to create sensible terrain
		
		- Figure out how to automatically create a tilemap grid (So far its manually drawn)
		
		- Choose if tilemap will be sectioned and loaded as new instance when player walks over(instanced) 
			or if it will be slowly loaded when the players moves around the map(dynamic)
				
				*If dynamic(preferred) then choose if player will always be centered(like crosshair in FPS games)
				 	on the map or if player can move to the edge of the map before more is loaded slowly

				* Possibly create a big instanced map (eg. 128x128 tiles) and move dynamically in them while
					still loading another instance of 128x128 once you get out of the initial one.

					All of those will be manually created (not sure how yet) but they will represent a part
					of Hogwarts for example and once you get out of one 128x128 part then you load in to 
					another 128x128 part and same for the forests and other such environments.

					LOADED IN CHUNKS SOMEHOW
'''

import pygame
import sys
import random
from perlin_noise import PerlinNoise

GREEN      = (20 ,150,70 )
BROWN      = (200,140,70 )
BLUE  	   = (50 ,150,170)
DARK_GREEN = (20 ,100,50)
DARK_BLUE  = (30 ,130,170)
WHITE	   = (255,255,255)
BLACK      = (0  ,0  ,0  )
GREY	   = (120,120,120)

grass  = 0
dirt   = 1
water  = 2
forest = 3
deep_water = 4
white = 5
black = 6
grey  = 7

pnoise = PerlinNoise(octaves = 10, seed = 1)

colours = {
			grass : GREEN,
			dirt  : BROWN,
			water : BLUE,
			forest: DARK_GREEN,
			deep_water: DARK_BLUE,
			white : WHITE,
			black : BLACK,
			grey  : GREY
		}
	# Original tilemap
# tilemap = [
# 			[water,water,grass,grass,grass],
# 			[water,grass,grass,grass,grass],
# 			[grass,grass,grass,grass,dirt],
# 			[dirt,grass,grass,dirt,dirt],
# 			[dirt,dirt,grass,dirt,dirt]
# 		]
		

# #		Test tilemap (Random)
# tile_num = 64
# tilemap = []
# # Creating randomly spread tile elements in tilemap
# for i in range(tile_num):
# 	tilemap.append([])
# 	for j in range(tile_num):
# 		# Chooses random number from 0 to 3(and 3) because there are 4 types of tiles
# 		tilemap[i].append(random.randint(0, len(colours)-1))


#		TEST TILEMAP 2 (Perlin Noise)
noise_scale = 0.1
tile_num = 128 # 64
tilemap = []


for i in range(tile_num):
	nested_tile = []
	for j in range(tile_num):
		pic = pnoise((i/tile_num, j/tile_num))
		if pic < -0.3: # 0.0:
			nested_tile.append(deep_water)
		elif pic < -0.1: # 0.0:
			nested_tile.append(water)
		elif pic < 0.03: # 0.0:
			nested_tile.append(dirt)
		elif pic < 0.17:
			nested_tile.append(grass)
		else:
			nested_tile.append(forest)

			# Grey scale test
		# if pic < -0.10:
		# 	nested_tile.append(white)
		# elif pic < 0.10:
		# 	nested_tile.append(grey)
		# else:
		# 	nested_tile.append(black)
		
	tilemap.append(nested_tile)


TILE_SIZE  =  8 # 15 # 50
MAP_WIDTH  = len(tilemap[0]) # 5
MAP_HEIGHT = len(tilemap)    # 5

pygame.init()

display_surface = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))  #Fullscreen mode -   ((0,0), pygame.FULLSCREEN) 

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# Reset the display to default/base
		# display_surface.fill((0,0,0))
		for row in range(MAP_HEIGHT):
			for column in range(MAP_WIDTH):
				colour = colours[tilemap[row][column]]
				pygame.draw.rect(display_surface, colour, (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

	pygame.display.update()				