import pygame
from PyGameComponents import core as pgcCore

def main():

	pygame.init()

	WIDTH = 1280
	HEIGHT = 720

	# Example usage in main.py:
	font = pygame.font.Font(None, 32)
	button = pgcCore.Button(0, 0, 150, 50, "Viva 42", (255, 0, 0), (200, 0, 0), (255, 255, 255), font)
	checkbox = pgcCore.Checkbox(100, 100, 20, 2, (255, 255, 255), (150, 150, 150), (255, 255, 255))
	text = pgcCore.Text("Hola Mundo", 32, (255, 255, 255), 150, 150)
	textInput = pgcCore.TextInput(pgcCore.SET.center_width(WIDTH), pgcCore.SET.center_height(HEIGHT), 300, 250, 28, (220, 210, 140), (220, 215, 150), (255, 255, 255), 10)


	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("PyGame Component Library")

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if button.is_clicked(pygame.mouse.get_pos()):
					text.update_text("Hola Mundo")
					new_x, new_y = pgcCore.SET.random_pos(WIDTH, HEIGHT)
					print(f"New X: {new_x} \n New Y: {new_y}")
					text.set_position(new_x, new_y)
					text.draw(screen)
			
			
			checkbox.handle_event(event)
			textInput.handle_event(event)
		
		if button.is_clicked(pygame.mouse.get_pos()):
			button.color = (200, 0, 0)
		else:
			button.color = (255, 0, 0)

		screen.fill((0, 0, 0))

		button.draw(screen)
		checkbox.draw(screen)
		text.draw(screen)
		textInput.draw(screen)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	main()