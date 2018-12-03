# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:07:29 2018

@author: HP
"""

import random
#import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import agentframework
import csv
import requests
import bs4



'''
Step 1: Initialise parameters
'''
print('Step 1: Initialise parameters.')

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20


print("num_of_agents", str(num_of_agents))
print("num_of_iterations", str(num_of_iterations))
print("neighbourhood", str(neighbourhood))



'''
Step 2: Initialise GUI.
'''
print('Step 2: Initialise GUI.')
root = tkinter.Tk()
root.wm_title("Model")



'''
Step 3: Get data from the web.
'''
print('Step 3: Get data from the web.')
url = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
td_zs = soup.find_all(attrs={"class" : "z"})
for td in td_xs:
    print(td.text)
#print(td_ys)
#print(td_xs)



'''
Step 4: Initialise environment containing data about the spatial environment in which agents act
'''
print('Step 4: Initialise environment containing data about the spatial environment in which agents act.')

environment = []

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
            #print(value)
            environment.append(rowlist)



'''
Step 5: Initialise agents.
'''
print('Step 5: Initialise agents.')

agents = []

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, x, y))


'''
Step 6: Initialise the GUI.
'''
print('Step 6: Initialise the GUI.')

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
init = True
halted = False
rerunid = 0
total_ite = 0
print("A GUI window will appear. Please select \"Run Model\" from the \"Model\" menu to run the model.")


'''
Step 7: Animation.
'''
print('Step 7: Animation.')

def update(frame_number):
    global carry_on
    global init
    global halted
    global rerunid
    
    fig.clear()

    if (carry_on):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        half_full_agent_count = 0
        if i in range(num_of_agents):
            if (agents[i].store > 50):
                half_full_agent_count += 1
        if (half_full_agent_count == num_of_agents):
            carry_on = False
            print("stopping condition")
            
    #Plot the environment
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
        #print(agents[i].y,agents[i].x)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    global halted
    global total_ite
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()



#Display the plot

def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

def exiting():
    if halted == False:
        print(" run stopped after", total_ite, "iterations.")


"""

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

"""

#tkinter.mainloop()
print("Thank you for using the model")

'''
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
'''








