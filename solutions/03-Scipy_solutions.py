#!/usr/bin/python
## My first python code

##imports:

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import readsav, wavfile
from scipy.linalg import solve
from scipy import fftpack

## My functions:


def read_idl_file():
  """
  Author S. Sousa and D. Andreasen
  Exercise 1. Read an IDL file
  """

  print "\n\n\nExercise 1:\n\n"
  idl = readsav('idl_vars.sav')
  print "-------------------------------------"
  print 'Type of IDL object:', type(idl)
  print 'Keys in object:', idl.keys()

  for key in idl.keys():
    print "-------------------------------------"
    print "Checking idl variable with name: ", key
    var = idl[key]
    print type(var)
# if var is a ndarray check the type of the elements
    if isinstance(var,np.ndarray):
      print "Type of the array: ", type(var[0])

  Msg = ''
  for msg in idl['array_str']:
    Msg = Msg + msg + ' '
  print '\nSuper hidden message:', Msg + ':('


def linalg_solve():
  """
  Author D. Andreasen
  Exercise 2. Solve a system of linear equations:
  """
  print "\n\n\nExercise 2:\n\n"
  # Some linear algebra
  A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], dtype=float)
  b = np.array([1, -2, 0])
  sol = solve(A, b)
  print '\nSolution to linear problem:', sol


def cat_purr():
  """
  Author S. Sousa
  Exercise 3. Fast Transform Fourier of a Cat Purr
  """
  print "\n\n\nExercise 3:\n\n"
  # The file must be in the current directory, or include the path in the name
  filenamewav = 'cat_purr.wav'
  rate,data = wavfile.read(filenamewav)
  time = np.arange(len(data),dtype='float')/rate
  fig = plt.figure()

  ax1 = fig.add_subplot(121)  
  ax1.plot(time,data)

##Making and plotting the Transform Fourier
  sample_freq = fftpack.fftfreq(data.size, d=1./rate)
  pidxs = np.where(sample_freq > 0)
  print "Computing the FFT... It will be Legen... Wait for it...\n"
  sig_fft = fftpack.fft(data)
  print "dary, Legendary!!!. FFT computed."
  freqs = sample_freq[pidxs]
  power = np.abs(sig_fft)[pidxs]
  ax2 = fig.add_subplot(122)  
  ax2.plot(freqs,power)
  ax2.set_xlim(0,200)
  plt.show()



### Main program:
def main():
  
#ex1
  read_idl_file()
#ex2
  linalg_solve()
#ex3 will take some time to compute the fft
  cat_purr()


if __name__ == "__main__":
    main()

