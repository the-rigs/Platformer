import pygame
from settings import *

class SpriteSheet():
  def __init__(self, image):
    self.sheet = image
  def get_image(self, frame,framey, width, height, color):
    image = pygame.Surface((width, height))
    image.blit(self.sheet, (0, 0), ((frame * width), (framey*height), width, height))
    image = pygame.transform.scale(image, (BLOCK_SIZE, BLOCK_SIZE))
    image.set_colorkey(color)

    return image