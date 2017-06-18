#!/usr/bin/python
## My first python code

##imports:

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
## My functions:



### Main program:
def main():


#Data:
  x = np.arange(0,10,0.01)
  y = np.sin(x)

  yexp = np.exp(x)


#Ex1

  fig1 = plt.figure()
  ax = fig1.add_subplot(111)  
  ax.plot(x,y,linestyle='--', color='green')
 
#Ex2

  fig2 = plt.figure()
  ax = fig2.add_subplot(111)  
  ax.plot(x,y,linestyle='--', color='green',label='line0')
  ax.set_title('Title',color='green',fontsize=20)
  ax.set_xlabel('X',color='green',fontsize=20)
  ax.set_ylabel('Y',color='green',fontsize=20)



#Ex3

  fig3 = plt.figure()
  ax = fig3.add_subplot(111)  
  ax.plot(x,yexp,linestyle='-', color='red')

#Ex4
  fig4 = plt.figure()
  ax1 = fig4.add_subplot(111)  
  ax2 = ax1.twinx()
  ax2.set_yscale('log')
  ax1.plot(x,yexp,linestyle='-', color='red')
  ax2.plot(x,yexp,linestyle='-', color='green')

#Ex5
#generate the data
  x,y = np.mgrid[0:51,0:51]
  z = np.sin(x/5.) + y*0
##plot
  fig5 = plt.figure()
  ax = fig5.add_subplot(111)  
  ax.pcolor(x, y, z, shading='flat')
  
#Ex6
#http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
  fig6 = plt.figure()
  ax1 = fig6.add_subplot(211)  
  ax1.pcolor(x, y, z, cmap='gray_r')
  ax2 = fig6.add_subplot(212)  
  ax2.pcolor(x, y, z, cmap='jet_r')

#Ex7

  x,y = np.mgrid[0:51,0:51]
  z = np.random.randn(51, 51)
  fig7 = plt.figure()
  ax = fig7.add_subplot(111)  
  ax.pcolor(x, y, z)


#Ex8
  z = z.reshape((51*51,))
  z.sort()
  z= z.reshape((51,51))
  fig8 = plt.figure()
  ax = fig8.add_subplot(111)  
  ax.pcolor(x, y, z)
  plt.show()





  
  
  

if __name__ == "__main__":
    main()

