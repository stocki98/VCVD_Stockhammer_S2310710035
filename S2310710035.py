<<<<<<< HEAD
__doc__ = 'sample file for a main methode'

#import system libs
import argparse
import sys

#required imports
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as syc


#setup argparser
parser = argparse.ArgumentParser(description='mass, velocity, friction')
parser.add_argument('--mass', type=int, help='Mass of the vehicle in kg')
parser.add_argument('--velocity', type=float, help='Velocity in m/s')
parser.add_argument('--friction', type=float, help='friction coefficient')
args = parser.parse_args()

#method for calculation and plot
def calc_plot(mass=1000, velocity=27, friction=0.65):
  #calcutlation of the stopping time
  stoptime = velocity / (friction*syc.g)
  time = np.arange(0.0, stoptime, 0.01)
  #calculation of the braking velocity
  breakingvelocity=velocity - (friction*syc.g) * time
  #calculation of the distance
  distance = velocity * time - (friction*syc.g * time ** 2) / 2
  stopdistance = velocity * stoptime - (friction*syc.g * stoptime ** 2) / 2
  #calculation rule of thumb
  snormal = (velocity*3.6/10) **2
  sdanger = (velocity*3.6/10) **2 * 0.5
  sreaction = (velocity*3.6/10) * 3
  sstop = snormal + sreaction
  sstopdanger = sdanger + sreaction
  #definition of the diagrams
  fig=plt.figure(figsize=[10,5])
  fig.subplots_adjust(top=0.8,)
  #add one plot
  ax1=fig.add_subplot(121)
  #add second plot
  ax2 = fig.add_subplot(122)
  #define plots
  ax1.plot(time, breakingvelocity, color ='green', lw = 2)
  ax2.plot(time, distance, color ='blue', lw = 2)
  #add axis labeling
  ax1.set_xlabel('time [s]')
  ax1.set_ylabel('Velocity [m/s]')
  ax2.set_xlabel('time [s]')
  ax2.set_ylabel('Distance [m]')
  ax1.grid('both')
  ax2.grid('both')
  #add plot label
  fig.suptitle('Coding Assingment S2310710035', fontweight ='bold')
  #export as PDF
  plt.savefig('S2310710035.pdf')
  #output of the resluts in the concole
  print('Mass:', mass, 'kg Velocity:', velocity, 'm/s Friction:', friction)
  print('Stop distance:', round(stopdistance, 2), 'm')
  print('Stop Time:', round(stoptime, 2), 's')
  print('Rule of thumb distance normal:', round(sstop, 2), 'm')
  print('Rule of thumb distance danger:', round(sstopdanger, 2), 'm')
#Call the calculate function and transfer the entered values
calc_plot(args.mass, args.velocity, args.friction)
#terminate program
sys.exit()
=======
__doc__ = 'sample file for a main methode'

#import system libs
import argparse
import sys

#required imports
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as syc


#setup argparser
parser = argparse.ArgumentParser(description='mass, velocity, friction')
parser.add_argument('--mass', type=int, help='Mass of the vehicle in kg')
parser.add_argument('--velocity', type=float, help='Velocity in m/s')
parser.add_argument('--friction', type=float, help='friction coefficient')
args = parser.parse_args()

#method for calculation and plot
def calc_plot(mass=1000, velocity=27, friction=0.65):
  #calcutlation of the stopping time
  stoptime = velocity / (friction*syc.g)
  time = np.arange(0.0, stoptime, 0.01)
  #calculation of the braking velocity
  breakingvelocity=velocity - (friction*syc.g) * time
  #calculation of the distance
  distance = velocity * time - (friction*syc.g * time ** 2) / 2
  stopdistance = velocity * stoptime - (friction*syc.g * stoptime ** 2) / 2
  #calculation rule of thumb
  snormal = (velocity*3.6/10) **2
  sdanger = (velocity*3.6/10) **2 * 0.5
  sreaction = (velocity*3.6/10) * 3
  sstop = snormal + sreaction
  sstopdanger = sdanger + sreaction
  #definition of the diagrams
  fig=plt.figure(figsize=[10,5])
  fig.subplots_adjust(top=0.8,)
  #add one plot
  ax1=fig.add_subplot(121)
  #add second plot
  ax2 = fig.add_subplot(122)
  #define plots
  ax1.plot(time, breakingvelocity, color ='green', lw = 2)
  ax2.plot(time, distance, color ='blue', lw = 2)
  #add axis labeling
  ax1.set_xlabel('time [s]')
  ax1.set_ylabel('Velocity [m/s]')
  ax2.set_xlabel('time [s]')
  ax2.set_ylabel('Distance [m]')
  ax1.grid('both')
  ax2.grid('both')
  #add plot label
  fig.suptitle('Coding Assingment S2310710035', fontweight ='bold')
  #export as PDF
  plt.savefig('S2310710035.pdf')
  #output of the resluts in the concole
  print('Mass:', mass, 'kg Velocity:', velocity, 'm/s Friction:', friction)
  print('Stop distance:', round(stopdistance, 2), 'm')
  print('Stop Time:', round(stoptime, 2), 's')
  print('Rule of thumb distance normal:', round(sstop, 2), 'm')
  print('Rule of thumb distance danger:', round(sstopdanger, 2), 'm')
#Call the calculate function and transfer the entered values
calc_plot(args.mass, args.velocity, args.friction)
#terminate program
sys.exit()
>>>>>>> a0bf0eabf05d53405c2ad2e332b3db274d526dcb
