# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:07:28 2018

@author: HP
"""

import random

class Agent():
    
    def __init__(self, environment, agents, x, y):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        if (x == None):
            self._x = random.randint(0,299)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,299)
        else:
            self._y = y
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299

        if random.random() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299
    
    def eat(self): # can you make it eat what is left?
        #If more than 10 get 10
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            #Store what is left
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            self.store = 0


    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
        
        
        
        
        
        
        