# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ahkab
import numpy as np

#Defining the multi-loop RV circuit we will be using
mycir = ahkab.Circuit('Multi-Loop RV Circuit')

mycir.add_vsource('V1', 'n1', mycir.gnd, dc_value=5)
mycir.add_resistor('R1', 'n2', 'n1', value=3)
mycir.add_resistor('R2', 'n2', mycir.gnd, value=4)
mycir.add_resistor('R3', 'n3', 'n2', value=1)
mycir.add_vsource('V2', 'n3', mycir.gnd, dc_value=7)
mycir.add_resistor('R4', 'n4', 'n3', value=5)
mycir.add_resistor('R5', 'n4', mycir.gnd, value=2)
mycir.add_vsource('V3', 'n4', 'n2', dc_value=10)

#Using matrix method for solving the multi-loop RV circuit
R = np.matrix('7 -4 0 0; -4 5 0 -1; 0 0 7 -5; 0 -1 -5 6')
V = np.matrix('5; -7; 7; 10')
I = np.linalg.inv(R) * V

print('\nMatrix Method:\n')
print(I)

"""
The matrix method results in four loop current values, as our matrix was 4x4. These
values represent the actual current through each individual loop. Comparing to 
the Ahkab method, we see that our first loop is equal (~1.21898 = I(V1). the next two
loops, as designated previously, are subtracted to get the Ahkab method: 5.67153
- 0.88321 = 4.78832 = I(V2). Finally, our last loop gives us 6.54015 = I(V3),
which confirms the two analysis methods result in the same values.
"""

#Using ahkab method for solving the multi-loop RV circuit
opa = ahkab.new_op()
r = ahkab.run(mycir, opa)['op']


print('\nAhkab Method:\n')
print(r)

"""
We can note from the results of the Ahkab analysis, that the circuit provides 
the current through three loops represented by I(V1), I(V2), and I(V3). These
currents come out to be -1.21898 A, -4.78832 A, and -6.54015 A respectively.
The circuit has four loops total, but as two of the loops share a single source,
the two center loops were subtracted from eachother, which results in the
 -4.78832 A loop. Explained further in the ReadMe.txt.
 
 NOTE: the output of all currents are negative, but the direction chosen is
 arbitrary if all share the same polarity, thus the current loops remain equal
 to the above matrix method
"""



