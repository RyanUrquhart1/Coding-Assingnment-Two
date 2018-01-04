"""
This file contains the agent class for model. This contains behaviournal information that will be called when the model is run.

"""
#import random function used to dictate agent movement.
import random


#creates the agent class
#All agents will start at the same place (the pub)
#All agents start with home = False. This is used in the model in conjuction with self.number. When their x/y cordinates have the number they are assinged self.home will turn to True.
#Agents have an individual step count, this increases with each step.
#agents can access the environment (what they are moving on) and environmentdensity (where density is added to the corresponding cordinates.)
class Agent():
    def __init__ (self, environment, environmentdensity, agents, number):
        self.environment = environment
        self.environmentdensity = environmentdensity
        self.steps = 0
        self.agents = agents
        self.house = number
        self.x = (140)
        self.y = (150)
        self.home = False
        
 #move command, each time it is run the agents will move to a new x/y cordinate based on the random function. Each move also adds a step.       
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299
        if random.random() > 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299
            
        self.steps = (self.steps) +1


                
            

        
        

        
        
        
        
    
        
        
        
        

        
        
            
            
        
        
        
    