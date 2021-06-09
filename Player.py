'''
	Creating a player and basic movement and interaction
'''

import pygame
import sys
import math
import time

#________________________________VARIABLES_______________________________________
			# COLOURS
WHITE = (255,255,255)
BLACK = (0  ,0  ,0  )

WINDOW_SIZE = (1000, 1000)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)

FPS = 60
clock = pygame.time.Clock()

p_pos_x = WINDOW_SIZE[0]//2
p_pos_y = WINDOW_SIZE[1]//2

p_width = 30
p_height= 30 

velocity = 250 #5
'''		Normalized velocity allows object to move diagonally at the same speed as it does
		left and right, up and down.
		When we move diagonally without normalization then x and y move at their same speed
		except that they move at the same time so for diagonal it travels a further distance
		for the same time as it does travel a shorter distance from left,right and up,down
		Normalization fixes that by dividing velocity of x and y by sqrt(2) = 1.414... and 
		when they are active at the same time then diagonal is no longer faster.	'''
normalized_vel = velocity/math.sqrt(2)
		# Initializing time before loop
previous_time = time.time()

pygame.init()
#___________________________________GAME LOOP______________________________________
while True:
			# Set fps
	clock.tick(FPS)
			
			# Calculate delta time
			# Used to make game run at same speed regardless of FPS variations
	now_time = time.time()
	delta_time = now_time - previous_time
	previous_time = now_time

			# EXIT LOOP
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

#_________________________________MOVEMENT KEYS_____________________________________
	key = pygame.key.get_pressed()

			# Checks if opposing keys pressed that player doesnt move
	if key[pygame.K_LEFT] and key[pygame.K_RIGHT]:
		pass
	elif key[pygame.K_DOWN] and key[pygame.K_UP]:
		pass
			# Checks for diagonal movement and normalizes diagonal speed
	elif key[pygame.K_LEFT] and key[pygame.K_UP]:
		p_pos_x -= normalized_vel * delta_time
		p_pos_y -= normalized_vel * delta_time
	elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:
		p_pos_x -= normalized_vel * delta_time
		p_pos_y += normalized_vel * delta_time
	elif key[pygame.K_RIGHT] and key[pygame.K_UP]:
		p_pos_x += normalized_vel * delta_time
		p_pos_y -= normalized_vel * delta_time
	elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
		p_pos_x += normalized_vel * delta_time
		p_pos_y += normalized_vel * delta_time
			#Checks for simple left,right,up,down movement and moves character
	elif key[pygame.K_LEFT]:
   		p_pos_x -= velocity * delta_time
	elif key[pygame.K_RIGHT]:
   		p_pos_x += velocity * delta_time
	elif key[pygame.K_UP]:
   		p_pos_y -= velocity * delta_time
	elif key[pygame.K_DOWN]:
   		p_pos_y += velocity * delta_time
	


			# Fills screen with colour so previous iteration doesnt show up with the current iteratior
	SCREEN.fill(BLACK)

	rect = pygame.Rect(p_pos_x, p_pos_y, p_width, p_height)
	pygame.draw.rect(SCREEN, WHITE, rect)
			# Circles are extra just to create a capsule shape (Can be commented out)
	pygame.draw.circle(SCREEN, WHITE, (p_pos_x+p_width//2, p_pos_y), (p_width//2))
	pygame.draw.circle(SCREEN, WHITE, (p_pos_x+p_width//2, p_pos_y+p_height), (p_width//2))


	
			# Updates the screen with info (Should be last code in while loop)
	pygame.display.update()
