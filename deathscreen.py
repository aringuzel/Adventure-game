import pygame, sys
from settings import *
import time


class Deathscreen:
    def __init__(self):
        
        #general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, 50)

        #Text setup
        self.text_surf = self.font.render('GAME OVER', False, (111, 196, 169))
        self.text_rect = self.text_surf.get_rect(center = (640, 360))
        self.quit_text_surf = self.font.render('Press C to quit', False, (111, 196, 169))
        self.quit_text_rect = self.text_surf.get_rect(center = (540, 460))

    def display(self):
        self.display_surface.fill('black')
        self.display_surface.blit(self.text_surf, self.text_rect)
        self.display_surface.blit(self.quit_text_surf, self.quit_text_rect)