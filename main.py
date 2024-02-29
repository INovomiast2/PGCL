import pygame
from PyGameComponents import core as pgclCore

# GLOBAL VARIABLES
WIN_WIDTH = 1080
WIN_HEIGHT = 400

def main():
	pygame.init() # Start a new game window
	
	# Settings
	screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
	pygame.display.set_caption("PGCL Playground")
	clock = pygame.time.Clock()
 
	player_sprite = pygame.image.load("sprite.webp")
	resized_sprite = pygame.transform.scale(player_sprite, (80, 80))
	player = pgclCore.Player(100, 100, resized_sprite, resized_sprite.get_width(), resized_sprite.get_height(), screen, 100, 150)
	#(Slider for testing)
	slider = pgclCore.Slider(100, 200, 100, 20, 0, 100, (240, 0, 0))
	# Create an empty text object to be updated later
	slider_text = pgclCore.Text("", 32, (0, 0, 0), 300, 200)

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
				
				if event.key == pygame.K_k:
					print(player.health)
					player.kill_player(player.health)
					print(player.health)
					if player.health == 0:
						player.speed = 0
						screen.fill((0, 0, 0))
						exit("PLAYER KILLED!")
						
			slider.handle_event(event)

		keys = pygame.key.get_pressed()
		dt = clock.tick(60) / 1000
		player.update(keys, dt)
  
		screen.fill((255, 255, 255))
		slider.draw(screen)
		# Update the text content using the current slider value
		slider_text.update_text(f"Slider Value: {round(slider.get_value())}")
		player.draw(screen)
		slider_text.draw(screen)

		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	main()
