from random import randint

class cat:
     def __init__(self, health, hunger, super_health):
          self.health = health
          self.hunger = hunger
          self.super_health = super_health
     
     def die(self):
          if self.health <= 0:
               print("Cat is die!")
               self.health = 0
               self.hunger = 0
               self.super_health = 0
               
     
     def hunger_system(self):
          if self.hunger > 50:
               self.hunger = self.hunger + self.health
               if self.health > 100:
                    self.health = self.health - 100
                    self.super_health = self.super_health + self.health
                    self.health = 100
health = randint(0, 100)
hunger = randint(0, 100)
super_health = randint(0, 100)

Sigma = cat(health, hunger, super_health)

print('Health:', Sigma.health, ', ', 'Hunger:', Sigma.hunger, ', ', 'Super_health:', Sigma.super_health)