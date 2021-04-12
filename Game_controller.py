# Importieren der Pygame-Bibliothek
import pygame 
from random import randint
import os

#Andere Klassen werden importiert
from Enemy_controller import *
from Button import *

#Game controller controlliert das Spiel
class Game_controller(Enemy_controller):
    def __init__(self):

        #Screen wird erstellt
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arcade", 40)
        pygame.display.set_caption("tower defense")
        self.displayWeite,self.displayHöhe = 1000,600
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))

        self.clk = 0
        #Enemy controller wird definiert
        self.en_crtl = Enemy_controller(self.screen)

        #notwendige variablen werden erstellt
        self.health = 25
        self.money = 1000
        self.round = 1
        self.alive = True
        self.round_alive = False

        #Background wird gezeichnet
        self.background = pygame.image.load("sprites/Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite -200,self.displayHöhe))

        #Text wird erstellt
        self.health_text = self.font.render(("Lives: %d" % self.health), False,(255, 255, 255))
        self.money_text = self.font.render(("Money: %d" % self.money), False,(255, 255, 255) )
        self.round_text = self.font.render(("Round: %d" % self.round), False,(255, 255, 255) )

        #Die variablen für die Buttons werden erstellt
        self.buttons = []
        self.wave_button_id = 1
        self.tower_button_id = 2
        self.restart_button_id = 3


    def display_static(self):
        """
        Zuständig für das zeichnen der nicht veränderten sprites
        :return: None
        """
        self.screen.blit(self.background,(0,0))
        display_grid(self.screen, 10)
        self.screen.blit(self.health_text,(self.displayWeite -190,0))
        self.screen.blit(self.money_text, (self.displayWeite -190,40))
        self.screen.blit(self.round_text, (self.displayWeite -190,80))
        for button in self.buttons:
            button.display_button(button.mode)

    def event_handler(self):
        """
        Zuständig für alle events
        :return: None
        """
        for button in self.buttons:
            button.highlight()
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button_handler()
                
        
    def button_handler(self):
        """
        Zuständig für die Buttons 
        :return: None
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        for button in self.buttons:
            if(button.inside(mouse_x,mouse_y)):
                if(button.id == self.wave_button_id):
                    if(not self.round_alive):
                        print("SEND NEW WAVE")
                        self.round_alive = True
                if(button.id == self.tower_button_id):
                    print("THIS IS A TOWER")
                if (button.id == self.restart_button_id):
                    self.start()
                    
    def blocking (self):
        #blocking between round to be updated
        while(not self.round_alive):
            self.event_handler()
            self.display_static()
            pygame.display.update()  

    def restart(self):
        """
        Zuständig für das restarten des Spieles 
        :return: None
        """        
        self.health = 25
        self.money = 1000
        self.round = 1
        self.alive = True
        self.round_alive = False
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))


    def game_end(self):  
        """
        Zuständig für das End screen 
        :return: None
        """     
        self.game_over_text = self.font.render(("You Lost at Round: %d" % self.round), False,(0, 0, 0) )
        self.screen.fill((255,0,0))
        self.screen.blit(self.game_over_text,(200,200))
        self.alive = False   
        self.event_handler()
        self.buttons[2].display_button(0)
        

    def start(self):
        """
        Zuständig für das starten des Programmes
        :return: None
        """        
        self.restart()
        
        self.nb_en = 0
        clock = pygame.time.Clock()

        #Buttons werden ersttellt
        self.buttons.append(Button(self.screen,self.displayWeite -190,500,180,90,'START',self.font,(170,170,0),self.wave_button_id))
        self.buttons.append(Button(self.screen,self.displayWeite -190,400,180,90,'TOWER',self.font,(0,170,170),self.tower_button_id))   

        while self.alive:
            clock.tick(30)
            self.event_handler()

            self.clk = 0

            nb_en = self.round * 5

            self.blocking()

            while (self.round_alive):
                self.display_static()
                self.event_handler()

                self.en_crtl.spawn(self.clk,nb_en,10)
                
                en_state = self.en_crtl.check_enemies()
                if(en_state == -1):
                    self.round_alive = False
                    print("ROUND IS FINISHED")
                else:
                    self.health -= en_state
                    self.health_text = self.font.render(("Lives: %d" % self.health), False,(0, 0, 0) )
                self.clk += 1

                #verlieren des Spieles wird gemacht (to be updated )
                if (self.health <= 0):
                    self.buttons.append(Button(self.screen,100,200,160,90,'Restart',self.font,(0,170,170),self.restart_button_id))
                    while True:
                        self.game_end()
                        pygame.display.update()
                pygame.display.update()
                
    







def display_grid(screen, res):
    """
    Ein Gitter wird erstellt für eine bessere Übersicht
    :parameter: Screen resolution
    :return: None
    """  
    #X Linien werden gemacht    
    x = [i for i in range(screen.get_width()) if (i % res == 0)]
    for i in x:
        pygame.draw.line(screen,(255,255,255),(i,0),(i,screen.get_height()),1)

    #Y Linien werden gemacht
    y = [i for i in range(screen.get_height()) if (i % res == 0)]
    for j in y:
        pygame.draw.line(screen,(255,255,255),(0,j),(screen.get_width(),j),1)

