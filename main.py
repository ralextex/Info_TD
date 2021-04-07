#Programm zuständig für den Game controller und startet das Spiel

from random import randint
import os

from Game_controller import Game_controller

Spiel = Game_controller()
Spiel.start()
