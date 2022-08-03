#   Creates Mathematically Accurate DNA model with major and minor grooves, base pairs, and double helix. 
#   
#   Created by Rokas Dargis as a part of Arya Lab research at Duke University
#   August 3rd, 2022
#   Licensed unit the MIT License 


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mayavi import mlab

#### All values are in Armstrong units (A) ###

radius = 10 #Radius of DNA
vs = 2*np.pi/34 #Veritcal shift to create double helix
z =  np.linspace(0,99.9,1000) #Crates a vertical axis from 0 to 99.9 at .01 A intervals
#First Helix equation
x_1 = radius*np.sin(-z*vs) 
y_1 = radius*np.cos(-z*vs)
#Second Helix equation, offset by the verical shift to establish major and minor groves of 12 A and 22 A respectively
x_2 = radius*np.sin(-(z+12)*vs)
y_2 = radius*np.cos(-(z+12)*vs)

#Convert Coordinates into DataFrame
DNA_dict = {
    'z' : z,
    'x_1': x_1,
    'y_1': y_1,
    'x_2': x_2,
    'y_2': y_2,
}
DNA_df = pd.DataFrame(DNA_dict)
DNA_df['z']=DNA_df['z'].round(2)

#Loop to create base pairs every 3.4 A
for i in range(0,30):
    x_list = []
    y_list = []
    z_index = 34*i #Place base pairs every 3.4 A 
    #Calculate the start and end point for the base pairs to connect to helix
    bp_x_1=DNA_df['x_1'][z_index] 
    bp_y_1=DNA_df['y_1'][z_index]
    bp_x_2=DNA_df['x_2'][z_index]
    bp_y_2=DNA_df['y_2'][z_index]
    mlab.plot3d([bp_x_1,bp_x_2],[bp_y_1,bp_y_2],[3.4*i,3.4*i],tube_radius=.5) #Plot base pairs
#Plots helices
mlab.plot3d(x_1,y_1,z,color=(1,0,0),tube_radius=1)
mlab.plot3d(x_2,y_2,z,color=(0,0,1),tube_radius=1) 
mlab.show() #show graph