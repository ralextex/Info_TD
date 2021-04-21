# Importieren der Pygame-Bibliothek
import pygame 
from random import randint
import os

# Andere Klassen werden importiert
from Enemy_controller import *
from Button import *
from Tower_controller import *

# Game controller controlliert das Spiel
class Game_controller():
    def __init__(self):

        # Screen wird erstellt
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tower Defense")
        self.displayWeite,self.displayHöhe = 1000,600
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))

        # Font
        self.font = pygame.font.SysFont("Arial", 40)

        # Background
        self.background = pygame.image.load("sprites/Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite -200,self.displayHöhe))

        # Schwierigkeits Einstellungen
        self.en_scaling = 1.5
        self.price_scaling = 1.2
        self.health_scaling = 1.15
        
        # Controller werden definiert
        self.en_crtl = Enemy_controller(self.screen, self.en_scaling, self.health_scaling)
        self.tw_crtl = Tower_controller(self.screen, self.price_scaling)

        # Spiel Variablen
        self.clk = 0 # Counter innerhalb einer Runde (Zeit verfolgung)
        self.health = 25
        self.round = 1
        self.alive = True # Spieler ist noch lebendig
        self.nend = True # Not End
        self.round_ongoing = False # Runde läuft noch
        self.tower_placement = False # Ein Tower wird gerade plaziert

        # GUI Text
        self.health_text = self.font.render(("Lives: %d" % self.health), False,(255, 255, 255))
        self.money_text = self.font.render(("Money: %d" % self.tw_crtl.money), False,(255, 255, 255) )
        self.round_text = self.font.render(("Round: %d" % self.round), False,(255, 255, 255) )
        self.game_over_text = self.font.render(("You lost on round: %d" % self.round), False,(0, 0, 0) )

        # Buttons
        self.buttons = []
        self.wave_button_id = 1
        self.tower_button_id = 2
        self.restart_button_id = 3

    def display_static(self):
        """
        Zuständig für das zeichnen der nicht veränderten sprites, Aktualisierung UI Text und Buttons
        :return: None
        """
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))

        # for Debugging purpose
        # display_grid(self.screen, 10)

        # Update Text
        self.screen.blit(self.health_text,(self.displayWeite -190,0))
        self.money_text = self.font.render(("Money: %d" % self.tw_crtl.money), False,(255, 255, 255) )
        self.screen.blit(self.money_text, (self.displayWeite -190,40))
        self.screen.blit(self.round_text, (self.displayWeite -190,80))

        # Display Buttons
        self.display_buttons()

    def display_buttons(self):
        """
        Zuständig für das zeichnen der Buttons
        :return: None
        """
        for button in self.buttons:
                button.display_button(button.mode)

    def event_handler(self):
        """
        Zuständig für alle events
        :return: None
        """
        # Highlight
        for button in self.buttons:
            button.highlight()
        for tower in self.tw_crtl.towers:
            tower.highlight()

        # Schließen des Programmes
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
                
            # Bei Maus klick
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x,mouse_y) = pygame.mouse.get_pos()
                
                self.button_handler()
                
                # Platzieren eines Towers
                if(self.tower_placement):
                    ret = self.tw_crtl.add_tower(mouse_x,mouse_y)
                    if(ret):
                        self.buttons[1].text = ["TOWER",str(int(self.tw_crtl.price))]
                        self.tower_placement = False
                                         
    def button_handler(self):
        """
        Zuständig für die Buttons event
        :return: None
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        for button in self.buttons:
            # Click innerhalb eines Buttons
            if(button.rect.inside(mouse_x,mouse_y)):
                # Event nach dem ID
                if(button.id == self.wave_button_id):
                    if(not self.round_ongoing):
                        print("SEND NEW WAVE")
                        self.round_ongoing = True
                if(button.id == self.tower_button_id):
                    self.tower_placement = True
                if (button.id == self.restart_button_id):
                    self.nend = False
                    self.start()
                    
    def blocking (self):
        """
        Zwischen den Runden warten auf event
        :return: None
        """     
        while(not self.round_ongoing):
            self.money_text = self.font.render(("Money: %d" % self.tw_crtl.money), False,(255, 255, 255) )
            self.display_static()
            self.tw_crtl.display_towers()
            self.event_handler()
            pygame.display.update()  

    def game_end(self):  
        """
        Zuständig für das End screen und wartet auf ein Event (Restart, Ende)
        :return: None
        """     
        self.screen.fill((255,0,0))
        self.game_over_text = self.font.render(("You lost on round: %d" % self.round), False,(0, 0, 0) )
        self.screen.blit(self.game_over_text,(300,200))
        self.display_buttons()
        self.event_handler()
        pygame.display.update()
        
    def start(self):
        """
        Hauptcode des Programmes läuft so lange das Spiel geht
        :return: 0 for succesfull finish
        """      

        clock = pygame.time.Clock()
     
        # Reset parameters
        self.health = 25
        self.round = 1
        self.alive = True
        self.nend = True
        self.round_ongoing = False
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))
        self.en_crtl = Enemy_controller(self.screen, self.en_scaling, self.health_scaling)
        self.tw_crtl = Tower_controller(self.screen, self.price_scaling)
        
        # Loeschen von Restart Button
        for button in self.buttons:
            if(button.id == self.restart_button_id):
                self.buttons.remove(button)
        
        #Buttons werden ersttellt
        self.buttons.append(Button(self.screen,self.displayWeite -190,500,180,90,["NEW WAVE"],self.font,(170,170,0),self.wave_button_id))
        self.buttons.append(Button(self.screen,self.displayWeite -190,400,180,90,["TOWER",str(self.tw_crtl.price)] ,self.font,(0,170,170),self.tower_button_id))  

        # Text wird angezeigt
        self.screen.blit(self.health_text,(self.displayWeite -190,0))
        self.screen.blit(self.money_text, (self.displayWeite -190,40))
        self.screen.blit(self.round_text, (self.displayWeite -190,80))

        pygame.display.update()

        while self.alive:
            # Zwischen den Runden

            clock.tick(30)
            self.event_handler()

            # Reset Clk
            self.clk = 0
            self.tw_crtl.round_ready()
        
            self.blocking()

            while (self.round_ongoing):
                # Innerhalb eine Runde
                clock.tick(30)

                self.display_static()
                self.event_handler()

                self.en_crtl.spawn(self.clk,self.round)         
                en_state = self.en_crtl.update_enemies()
                self.en_crtl.display_enemies()

                self.tw_crtl.display_towers()
                self.tw_crtl.attack(self.clk, self.en_crtl.enemies) 

                if(en_state == -1):
                    self.round_ongoing = False
                    print("ROUND IS FINISHED")
                else:
                    self.health -= en_state
                    self.health_text = self.font.render(("Lives: %d" % self.health), False,(255, 255, 255) )
                
                self.clk += 1

                # verlieren des Spieles
                if (self.health <= 0):
                    # Remove Buttons
                    self.buttons = []
                    self.alive = False
                    self.tower_placement = False

                    # restart Button
                    self.buttons.append(Button(self.screen,100,350,500,100,["Restart"],self.font,(0,170,170),self.restart_button_id))
                    
                    while self.nend:
                        self.game_end()

                    if(self.nend):
                        return 0

                # Display Update
                pygame.display.update()        

            #Round is finished
            self.round+=1 
            self.round_text = self.font.render(("Round: %d" % self.round), False,(255, 255, 255) ) 
    


def display_grid(screen, res):
    """
    Ein Gitter wird erstellt für eine bessere Übersicht (Debugging Purpose)
    :parameter: Screen, grid resolution
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