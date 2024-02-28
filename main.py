import pygame
from PyGameComponents import core as pgclCore

# GLOBAL VARIABLES
WIN_WIDTH = 800
WIN_HEIGHT = 600

world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def main():
	pygame.init() # Start a new game window
	
	# Settings
	screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
	pygame.display.set_caption("PGCL Playground")
	clock = pygame.time.Clock()
 
	player_sprite = pygame.image.load("sprite.webp")
	resized_sprite = pygame.transform.scale(player_sprite, (80, 80))
	player = pgclCore.Player(100, 100, resized_sprite, resized_sprite.get_width(), resized_sprite.get_height(), screen, 150)
	grid = pgclCore.Grid(50, WIN_WIDTH, WIN_HEIGHT, world)
	# running
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					running = False
   
		keys = pygame.key.get_pressed()
		dt = clock.tick(60) / 1000
		player.update(keys, dt)
  
		screen.fill((255, 255, 255))
		grid.draw(screen)
		if grid.check_collision(player):
			player.dx = 0
			player.dy = 0
		player.draw(screen)

		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	main()