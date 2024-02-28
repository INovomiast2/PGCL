from .components import *
import random

class SET:
	@staticmethod
	def center_width(x):
		return (x / 2)
	
	def center_height(y):
		return (y / 2)
	
	def random_pos(x, y):
		x = random.random() * x
		y = random.random() * y
		return x, y