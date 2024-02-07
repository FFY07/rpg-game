from pathlib import Path
import random
from .main_unit import Unit

import pygame


class Tank(Unit):
    def __init__(self, name, icon, health, strength, defence):
        super().__init__()
        self.name = name
        self.icon = icon
        self.health = health
        self.strength = strength
        self.defence = defence