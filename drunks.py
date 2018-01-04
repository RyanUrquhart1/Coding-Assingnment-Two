"""
The data for this project is within 'drunkfinal.csv',  I have changed the data file to alter the number that 
dictates the pub location. Initially this was set as the number 1
I have changed these to the number 175. The number itself does not matter
but It needed to be one not in use by the households, the only reason for doing this is to make the pub visible on the initial map.
"""

# TOWN PLANNING FOR DRUNKS # 
#Pull in the data file and find the pub and home points
#Draw the pub and homes on the screen
#Model the drunks leaving the pub and store how many drunks pass thorugh certain points
#Draw the density on the map 
#Save the density map to a file as a text file
import numpy
import matplotlib.pyplot
import drunkagentclass

#Defines variables and creates lists that will be populated later in the model, sets the number of agents to 25.
steps = []
environment = []  
environmentdensity = []
agents = []
num_of_agents = 25


#Here I import the environment data that the agents will interact with, this is stored as list and plotted to show the user.
#I also import a duplicate of this file, this will be where the point density is added to ensure it doesn't interfere with the agents finding their home.
import csv 
f = open('drunkfinal.csv' , newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
       rowlist.append(item)
    environment.append(rowlist)
    
f.close()

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

import csv 
f = open('aftermovement.csv' , newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
       rowlist.append(item)
    environmentdensity.append(rowlist)
    
f.close()


#The code below makes the agents and places them in the centre of the plot (in the pub)
#The number dicates the agents home, this is first created in the drunkagentclass.py, it uses the number of agents to to give them all a number.
#(i+1)*10 is used as the lists starts at zero. Each agent will have a multiple of 10. 10-250.
for i in range(num_of_agents):
    number = (i+1)*10
    agents.append(drunkagentclass.Agent(environment, environmentdensity, agents, number)) 
     

#New plot is made to show agents in the pub.
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
   

#moves the agents
#each agent moves one at time, the print function prints every time one makes it home so you know the model is running.
#each cordinate the agent stands on adds 1 to the environment density map
#once the agents reach their own home they stop.
for i in range(num_of_agents):
    print(i)
    while agents[i].home==False:
        agents[i].move()
        environmentdensity[agents[i].y][agents[i].x]+=1
        if agents[i].house==agents[i].environment[agents[i].y][agents[i].x]:
            agents[i].home=True
            
    
#plots the agents after they make it home        
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
 

#prints number of steps it took each agent to make it home     
for i in range(num_of_agents):
    print("steps" + " " + str(agents[i].steps))

#The number of steps is then appended to a new list
for i in range(num_of_agents):
    steps.append(agents[i].steps)
    
#The list of steps is then used by the numpy mean function to work out the average number of steps, this is then printed.
averagesteps = numpy.mean(steps)
print("The average number of steps taken to reach home is " + str(averagesteps))



#plots environment density
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environmentdensity)


#Writes environmentdensity to new file.
f2 = open('densitymap.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environmentdensity:		
	writer.writerow(row)		
f2.close()





    

