


'''--- Goal
Write a class to handle a sequence of voltage measurements at different times.

--- Specifications
- the class name must be VoltageData
- the class must be initialized with two generic iterables of the same length
  holding the numerical values of times and voltages
- alternatively the class can be initialized from a text file
- the class must expose two attributes: 'timestamps' and 'voltages', each returning
  a numpy array of type numpy.float64 of the corresponding quantity.
- the values should be accessible with the familiar square parenthesis syntax:
  the first index must refer to the entry, the second selects time (0) or 
  voltage (1). Slicing must also work.
- calling the len() function on a class instance must return the number of 
  entries
- the class must be iterable: at each iteration, a numpy array of two 
  values (time and voltage) corresponding to an entry in the file must be
  returned
- the print() function must work on class instances. The output must show one
  entry (time and voltage), as well as the entry index, per line.
- the class must also have a debug representation, printing just the values 
  row by row
- the class must be callable, returning an interpolated value of the tension 
  at a given time
- the class must have a plot() method that plots data using matplotlib.
  The plot function must accept an 'ax' argument, so that the user can select
  the axes where the plot is added (with a new figure as default). The user
  must also be able to pass other plot options as usual
- [optional] support a third optional column for the voltage errors
- [optional] rewrite the run_tests() function in sandbox/test_voltage_data.py
  as a sequence of proper UnitTests'''



import numpy as np 
import matplotlib.pyplot as plt 
from voltage_data_live import VoltageData  
class VoltageData:
    def __init__(self,timestamps,voltages):
      t= np.array(timestamps, dtype=np.float64)#sono anticipati e li chiudiamo
      v= np.array(voltages, dtype=np.float64)  
      self.data=np.column_stack((timestamps,voltages))  #voglio qualcosa di privato

      '''if len(timestamps) != len(voltages):
          raise ValueError("Times and voltages must have the same length")  non rilevante perché ora abbiamo column_stack'''
      

    @property
    def timestamps(self):
        return self.data[:,0]  #prendo tutte le righe della prima colonna   
    
    @property
    def voltages(self):
        return self.data[:,1]  #prendo tutte le righe della seconda colonna 
    def __getitem__(self, indices)
        return self.data[indices]  #ritorno le righe e colonne selezionate  :


    @classmethod
    def from_file(cls, filpath):
        timestamps,voltages = np.loadtxt(filpath, unpack=True)
            
        return cls(timestamps, voltages) #sto chiamando il costruttore della classe

    def __len__(self):
        return len(self.timestamps) # ho controllato a riga 45 che coincidono, essendo pubblici potrei avere un problema


