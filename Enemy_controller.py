from Enemies import Enemy

#Kontrolliert und benutzt die Enemies
class Enemy_controller():
    def __init__(self, screen):
        self.screen = screen
        self.enemies = []
        self.enemies_spawned = 0
        self.path = [(126, 4), (126, 549), (574, 549), (574, 257), (794, 257)]
        

    def spawn(self,clk,to_spawn,rate):
        """
        Spawnt die Gegner 
        :param : counter, wieviele Gegner, Geschwindigkeit des spawnen
        :return: None
        """
        if((clk % rate) == 0):
            if(self.enemies_spawned < to_spawn):
                self.enemies_spawned += 1 
                self.enemies.append(Enemy(126,4,self.path))

        
    def check_enemies(self):
        """
        Guckt ob Enemies noch am Leben sind   
        :return: None
        """
        hp_lost = 0
        if(len(self.enemies) == 0):
            self.enemies_spawned = 0
            return -1
        else:
            for en in self.enemies:
                if(en.alive):
                    en.move()
                    en.display(self.screen)

                #Löscht die enemies wenn sie das Ziel erreichen
                else:
                    self.enemies.remove(en)
                    hp_lost += 1
            return hp_lost
