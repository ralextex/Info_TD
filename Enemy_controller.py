from Enemies import Enemy

class Enemy_controller(Enemy):
    def __init__(self, screen):
        self.screen = screen
        self.enemies = []
        self.enemies_spawned = 0
        self.path = [(126, 4), (126, 549), (574, 549), (574, 257), (794, 257)]
        

    def spawn(self,clk,to_spawn,rate):
        if((clk % rate) == 0):
            if(self.enemies_spawned < to_spawn):
                self.enemies_spawned += 1 
                self.enemies.append(Enemy(126,4,self.path))

        
    def check_enemies(self):
        hp_lost = 0
        if(len(self.enemies) == 0):
            self.enemies_spawned = 0
            return -1
        else:
            for en in self.enemies:
                if(en.alive):
                    en.move()
                    en.display(self.screen)
                else:
                    self.enemies.remove(en)
                    hp_lost += 1
            return hp_lost
