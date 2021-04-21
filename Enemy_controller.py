from Enemies import Enemy

# Kontrolliert und benutzt die Enemies
class Enemy_controller():
    def __init__(self, screen, en_scaling, health_scaling):
        self.screen = screen

        self.en_scaling = en_scaling
        self.health_scaling = health_scaling

        self.rate = 10 #spawn rate
        self.rate_change = True
        self.enemies = []
        self.enemies_spawned = 0 # enemies spawned in current round
        self.spawning = False # finished spawning for the round
        self.path = [(126, 4), (126, 549), (574, 549), (574, 257), (805, 257)] # Weg
        

    def spawn(self,clk,rnd):
        """
        Spawnt die Gegner 
        :param : clock, Runde
        :return: None
        """
        if (rnd % 7 == 0):
            if(self.rate_change):
                self.rate = self.rate * 0.75
                self.rate_change = False
        else:
            self.rate_change = True
            
        to_spawn = int(8 * self.en_scaling ** (rnd-1) ) # Scaling wie viele to_spawn
        health = int(10 * self.health_scaling ** (rnd-1) ) # Scaling wie viel Leben
        
        if((clk % int(self.rate)) == 0): # Spawn an enemy every rate iteration
            if(self.enemies_spawned < to_spawn): # did I spawn all enemy
                self.spawning = True
                self.enemies_spawned += 1 
                self.enemies.append(Enemy(126,4,self.path,health))
            else:
                self.spawning = False

        
    def update_enemies(self):
        """
        Zustaendig fuer gegner bewegung und ob am leben  
        :return: -1 for end of round, else health lost
        """
        hp_lost = 0 # Leben verloren
        if(len(self.enemies) == 0): # Runde zu ende
            if (not self.spawning): # Oder alle TOD
                self.enemies_spawned = 0
                return -1 # End round
            else:
                return hp_lost 
        else:
            for en in self.enemies:
                if(en.alive): # Wenn am leben
                    en.move()

                #Löscht die enemies wenn sie das Ziel erreichen
                else:
                    self.enemies.remove(en)
                    hp_lost += 1
            return hp_lost

    def display_enemies(self):
        """
        Anzeige der Gegner
        :return: None
        """
        for en in self.enemies:
            en.display(self.screen)

