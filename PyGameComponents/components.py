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

# Dropwdown
class Dropdown:
	def __init__(self, x, y, width, height, font_size, color, text_color, hover_color, options):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.font_size = font_size
		self.color = color
		self.text_color = text_color
		self.hover_color = hover_color  # New attribute for hover text color
		self.options = options
		self.selected_index = 0  # Initialize to first option
		self.font = pygame.font.Font(None, self.font_size)
		self.open = False
		self.hovered_index = None  # Track hovered option (if any)

		self.option_surfaces = [self.font.render(opt, True, self.text_color) for opt in self.options]

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

		selected_text_surface = self.font.render(self.options[self.selected_index], True, self.text_color)
		screen.blit(selected_text_surface, (self.x + 5, self.y + 5))

		if self.open:
			pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y + self.height, self.width, len(self.options) * self.height))

			for i, option in enumerate(self.options):
				option_surface = self.option_surfaces[i]
				# Change color based on hover and selection
				if i == self.hovered_index:
					text_color = self.hover_color  # Use hover color if hovered
				elif i == self.selected_index:
					text_color = self.text_color  # Use normal text color if selected
				else:
					text_color = self.text_color  # Default text color for other options
				option_surface = self.font.render(option, True, text_color)  # Re-render with updated color
				screen.blit(option_surface, (self.x + 5, self.y + self.height + (i * self.height) + 5))

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.is_clicked(event.pos):
				self.open = not self.open
			else:
				self.open = False

			if self.open:
				mouse_y = event.pos[1]
				clicked_index = (mouse_y - self.y - self.height) // self.height
				if 0 <= clicked_index < len(self.options):
					self.selected_index = clicked_index
					print(f"Selected option: {self.options[self.selected_index]}")  # Print selected option

		if event.type == pygame.MOUSEMOTION:
			# Detect hovered option
			mouse_x, mouse_y = event.pos
			if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
				# Calculate the index of the hovered option
				hovered_index = (mouse_y - self.y - self.height) // self.height
				if 0 <= hovered_index < len(self.options):
					self.hovered_index = hovered_index
				else:
					self.hovered_index = None  # Not hovering over an option
			else:
				self.hovered_index = None  # Not hovering over the dropdown

	def is_clicked(self, pos):
		return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

	def get_selected_option(self):
		return self.options[self.selected_index]

class Player:
	def __init__(self, x, y, sprite, width, height, screen, health=100, speed=100):
		self.x = x
		self.y = y
		self.original_sprite = sprite  # Store the original, unrotated sprite
		self.sprite = sprite  
		self.width = width
		self.height = height
		self.speed = speed
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.screen = screen
		self.health = health
		self.limit_w = screen.get_width() - self.width
		self.limit_h = screen.get_height() - self.height

	def draw(self, screen):
		screen.blit(self.sprite, (self.x, self.y))

	def update(self, keys, dt):
		dx = 0
		dy = 0

		if keys[pygame.K_LEFT]:
			dx -= self.speed * dt
			self.sprite = pygame.transform.rotate(self.original_sprite, -90)
		elif keys[pygame.K_RIGHT]:
			dx += self.speed * dt
			self.sprite = pygame.transform.rotate(self.original_sprite, -90)
		elif keys[pygame.K_UP]:
			dy -= self.speed * dt
			self.sprite = pygame.transform.rotate(self.original_sprite, -90)
		elif keys[pygame.K_DOWN]:
			dy += self.speed * dt
			self.sprite = pygame.transform.rotate(self.original_sprite, -90)

		# Implement screen edge collision handling
		self.x = max(0, min(self.x + dx, self.limit_w))
		self.y = max(0, min(self.y + dy, self.limit_h))

		self.rect.x = self.x
		self.rect.y = self.y

	def check_collision(self, object):
		return self.rect.colliderect(object.rect)
	
	def kill_player(self, health):
		self.health = 0

		

	
# Grid for the game

class Grid:
	def __init__(self, block_size, screen_width, screen_height, blocks_array):
		self.block_size = block_size
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.blocks = blocks_array

		# Calculate grid dimensions based on actual block_array size
		self.num_cols = len(blocks_array[0])
		self.num_rows = len(blocks_array)

		# Create collision grid using boolean values based on block_array values
		self.collision_grid = [[block >= 1 for block in row] for row in blocks_array]

		# Create empty sprite groups
		self.solid_blocks = pygame.sprite.Group()
		self.platform_blocks = pygame.sprite.Group()

	def draw(self, screen):
		for row in range(self.num_rows):
			for col in range(self.num_cols):
				block_type = self.blocks[row][col]
				x = col * self.block_size
				y = row * self.block_size

				if block_type >= 1:
					# Draw solid block
					block = pygame.sprite.Sprite()
					block.image = pygame.Surface((self.block_size, self.block_size))
					block.image.fill((0, 0, 0))  # Set block color
					block.rect = block.image.get_rect()
					block.rect.x = x
					block.rect.y = y
					self.solid_blocks.add(block)
					screen.blit(block.image, block.rect)

				# No need for platform_blocks as both 1 and 0 represent solid blocks

	def check_collision(self, player):
		# Check collision with all blocks (both solid and platform)
		for block in self.solid_blocks:
			if pygame.sprite.collide_rect(player, block):
				return True

		return False
	
# Enemy Object
class Enemy:
	def __init__(self, x, y, width, height, health):
		pass
	
	def draw(self, screen):
		pass

	def update(self, dt):
		pass

	def check_collision(self, player):
		pass

	def kill_enemy(self, enemy):
		pass

# Slider
class Slider:
	def __init__(self, x, y, width, height, min_value, max_value, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.min_value = min_value
		self.max_value = max_value
		self.color = color

		self.value = min_value
		
		self.thumb_size = 0.2 * self.width

		self.bar_rect = pygame.Rect(self.x, self.y, self.width, self.height)

		self.thumb_x = self.x + (self.value / (self.max_value - self.min_value))  * (self.width - self.thumb_size)

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.bar_rect)

		thumb_rect = pygame.Rect(self.thumb_x, self.y + self.height // 2 - self.thumb_size // 2, self.thumb_size, self.thumb_size)
		pygame.draw.rect(screen, (0, 0, 0), thumb_rect)

	def handle_event(self, event):
		"""Handles mouse events to update the slider value."""
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			# Check if the mouse click is within the slider bar
			if self.bar_rect.collidepoint(event.pos):
				# Calculate the new slider value based on mouse click position
				self.value = (event.pos[0] - self.x - self.thumb_size / 2) / (self.width - self.thumb_size) * (self.max_value - self.min_value) + self.min_value

				# Clamp the value within the allowed range
				self.value = max(self.min_value, min(self.value, self.max_value))

				# Update the thumb position based on the new value
				self.thumb_x = self.x + (self.value / (self.max_value - self.min_value)) * (self.width - self.thumb_size)

	def get_value(self):
		"""Returns the current value of the slider."""
		return self.value