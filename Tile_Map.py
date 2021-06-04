'''
	Author: Stefan Popovic
	Date  : 04/06/2021

	About : Map grid/world for player to move in. 
			Goal is to look similar to Nintendos Pokemon and Zelda game with different biomes
			and structures to explore (Dark Forest, Hogwarts, Hogsmead ans such)
	
	TODO  : 
		- Figure out how to set up different sprite blocks to create sensible terrain
		- Figure out how to automatically create a tilemap grid (So far its manually drawn)
		- Choose if tilemap will be sectioned and loaded as new instance when players walks(instanced) 
			over or if it will be slowly loaded when the players moves around the map(dynamic)
'''

import pygame
import sys

GREEN = (20 ,150,70 )
BROWN = (200,140,70 )
BLUE  = (50 ,150,170)

grass = 0
dirt  = 1
water = 2

colours = {
			grass: GREEN,
			dirt : BROWN,
			water: BLUE
		}
tilemap = [
			[water,water,grass,grass,grass],
			[water,grass,grass,grass,grass],
			[grass,grass,grass,grass,dirt],
			[dirt,grass,grass,dirt,dirt],
			[dirt,dirt,grass,dirt,dirt]
		]

TILE_SIZE  = 50
MAP_WIDTH  = 5
MAP_HEIGHT = 5

pygame.init()

display_surface = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# Reset the display to default/base
		# display_surface.fill((0,0,0))
		for row in range(MAP_WIDTH):
			for column in range(MAP_HEIGHT):
				colour = colours[tilemap[row][column]]
				pygame.draw.rect(display_surface, colour, (column*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))

	pygame.display.update()				