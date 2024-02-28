from pygame.font import Font
from pygame import draw
import pygame
import time

# Button
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = font  # Store the passed font object
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

    def draw(self, screen):
        draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

# Checkbox
checkmark_points = [
	(0.1, 0.7),
	(0.4, 0.9),
	(0.8, 0.3),
	(0.4, 0.1),
	(0.1, 0.3)
]

def draw_checkmark(screen, color, size, pos):
	# Calculate point coordinates based on size and position
    points = [(size * x + pos[0], size * y + pos[1]) for x, y in checkmark_points]

    # Draw lines connecting the points
    draw.lines(screen, color, True, points)

class Checkbox:
	def __init__(self, x, y, size, border_width, color, fill_color, checkmark_color, checked=False):
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		self.fill_color = fill_color
		self.border_width = border_width
		self.checkmark_color = checkmark_color
		self.checked = checked

	def draw(self, screen):
		draw.rect(
			screen,
			self.color,
			(self.x, self.y, self.size, self.size),
			self.border_width
		)

		if self.checked:
			draw_checkmark(
				screen,
				self.checkmark_color,
				self.size - self.border_width * 2,
				(self.x + self.border_width, self.y + self.border_width)
			)

			draw.rect(
				screen,
				self.fill_color,
				(
					self.x + self.border_width,
					self.y + self.border_width,
					self.size - self.border_width * 2,
					self.size - self.border_width * 2
				)
			)
	
	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and self.is_clicked(event.pos):
			self.checked = not self.checked
	
	def is_clicked(self, pos):
		return (
			self.x <= pos[0] <= self.x + self.size
			and self.y <= pos[1] <= self.y + self.size
		)

# Text
class Text:
	def __init__(self, text, font_size, color, x, y):
		self.text = text
		self.font_size = font_size
		self.color = color
		self.x = x
		self.y = y
		self.font = Font(None, self.font_size)
		self.text_surface = self.font.render(self.text, True, self.color)
		self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

	def draw(self, screen):
		screen.blit(self.text_surface, self.text_rect)
	
	def update_text(self, new_text):
		self.text = new_text
		self.text_surface = self.font.render(self.text, True, self.color)
		self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

	def set_position(self, x, y):
		self.x = x
		self.y = y
		self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))  # Update rect

	def get_width(self):
		return self.text_rect.width
	
	def get_height(self):
		return self.text_rect.height
	
# Text Input
class TextInput:
	def __init__(self, x, y, width, height, font_size, color, active_color, text_color, value_length=20, active=False):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font_size = font_size
		self.color = color
		self.active_color = active_color
		self.text = ""
		self.value_length = value_length
		self.text_color = text_color
		self.font = Font(None, self.font_size)
		self.text_surface = self.font.render(self.text, True, self.text_color)
		self.active = active

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

		if self.active:
			pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height), 2)
		
		screen.blit(self.text_surface, (self.x + 5, self.y + 5))
	
	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.is_clicked(event.pos):
				self.set_active(True)
			else:
				self.set_active(False)

		if event.type == pygame.KEYDOWN and self.active:
			if event.key == pygame.K_BACKSPACE:
				self.text = self.text[:-1]
			elif event.key == pygame.K_RETURN:
				print(self.text)
				time.sleep(1)
				text = ""
				self.text_surface = self.font.render(self.text, True, self.text_color)
			else:
				if len(self.text) < self.value_length:
					self.text += event.unicode

			self.text_surface = self.font.render(self.text, True, self.text_color)

	def set_active(self, active):
		self.active = active

	def is_clicked(self, pos):
		return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
	
	def get_text(self):
		return self.text

# Dropdown
class Dropdown:
	def __init__(self, x, y, width, height, font_size, color, text_color, options):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font_size = font_size
		self.color = color
		self.text_color = text_color
		self.options = options
		self.selected_index = 0
		self.font = Font(None, self.font_size)
		self.open = False

		self.option_surfaces = [self.font.render(opt, True, self.text_color) for opt in self.options]