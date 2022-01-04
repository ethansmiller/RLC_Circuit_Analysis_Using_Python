# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:16:32 2021

@author: Ethan
"""

import ahkab
from ahkab import circuit, printing, time_functions
import pylab as plt
import numpy as np
from matplotlib.pyplot import *

#setting up the figure 
get_ipython().run_line_magic('pylab', 'inline')
figsize = (15, 10)

#creating step function to be applied to our circuit
voltage_step = time_functions.pulse(v1=0, v2=1, td=500e-9, tr=1e-12, pw=1, tf=1e-12, per=2)

#creating our 4-Loop RLC circuit: an extended version of the provided RLC circuit from lecture
mycir = ahkab.Circuit('Multi-Loop RLC Circuit')

mycir.add_vsource('V1', n1='n1', n2=mycir.gnd, dc_value=1, ac_value=1, function=voltage_step)
mycir.add_resistor('R1', n1= 'n1', n2= 'n2', value= 600)
mycir.add_inductor('L1', n1= 'n2', n2= 'n3', value= 15.24e-3)
mycir.add_capacitor('C1', n1= 'n3', n2= mycir.gnd, value= 119.37e-9)
mycir.add_inductor('L2', n1= 'n3', n2= 'n4', value= 61.86e-3)
mycir.add_capacitor('C2', n1= 'n4', n2= mycir.gnd, value= 155.12e-9)
mycir.add_inductor('L3', n1= 'n4', n2= 'n5', value= 100e-3)
mycir.add_capacitor('C3', n1= 'n5', n2= mycir.gnd, value= 180e-9)
mycir.add_resistor('R2', n1= 'n5', n2= mycir.gnd, value= 1.2e3)


#Performing OP analysis and printing it in the console
op_analysis = ahkab.new_op()
r = ahkab.run(mycir, op_analysis)['op']

print('\n\nOP Analysis:\n')
print(r, op_analysis)
print('\n\n')

#running both ac and tran analysis, which are then printed
ac_analysis = ahkab.new_ac(start=1e3, stop=1e5, points=100)
tran_analysis = ahkab.new_tran(tstart=0, tstop=1.2e-3, tstep=1e-6, x0=None)
r = ahkab.run(mycir, an_list=[ac_analysis, tran_analysis])

print(r)

#TRAN analysis, leveraged from ahkab lecture
#figure opens in 'Plots' tab of Spyder
fig = plt.figure()
plt.title(mycir.title + " - TRAN Simulation")
plt.plot(r['tran']['T'], r['tran']['VN1'], label="Input Voltage")
plt.plot(r['tran']['T'], r['tran']['VN5'], label="Output Voltage")
plt.legend()
plt.grid(True)
plt.ylim([0, 1.2])
plt.ylabel('Step Response')
plt.xlabel('Time [s]')
fig.savefig('tran_plot.png')


#AC analysis, leveraged from ahkab lecture
#figure opens in 'Plots' tab of Spyder
fig = plt.figure()
plt.subplot(211)
plt.semilogx(r['ac']['f'], np.abs(r['ac']['Vn5']), 'o-')
plt.ylabel('abs(V(n5)) [V]')
plt.title(mycir.title + " - AC Simulation")
plt.subplot(212)
plt.grid(True)
plt.semilogx(r['ac']['f'], np.angle(r['ac']['Vn5']), 'o-')
plt.xlabel('Frequency')
plt.ylabel('arg(V(n5)) [rad]')
fig.savefig('ac_plot.png')
plt.show()

#Printing the gathered netlist for reference
print('\nGathered netlist:\n')
print(mycir)

#Beginning PZ analysis
#running the PZ analysis to gather our poles and zeros: printed in the console
pza = ahkab.new_pz('V1', ('n5', mycir.gnd), x0=None)
r = ahkab.run(mycir, pza)['pz']

r.keys()

print('\nPoles and Zeros of our circuit:\n')
for x, _ in r:
    print ("* %s = %+g %+gj Hz" % (x, np.real(r[x]), np.imag(r[x])))


#Plotting of our Poles and Zeros, which again is printing in the 'Plots' tab of Spyder
figure(figsize=figsize)
# plot o's for zeros and x's for poles
for x, v in r:
    plot(np.real(v), np.imag(v), 'bo'*(x[0]=='z')+'rx'*(x[0]=='p'))
# set axis limits and print some thin axes
xm = 1e6
xlim(-xm*10., xm*10.)
plot(xlim(), [0,0], 'k', alpha=.5, lw=.5)
plot([0,0], ylim(), 'k', alpha=.5, lw=.5)
# plot the distance from the origin of p0 and p1
plot([np.real(r['p0']), 0], [np.imag(r['p0']), 0], 'k--', alpha=.5)
plot([np.real(r['p1']), 0], [np.imag(r['p1']), 0], 'k--', alpha=.5)
# print the distance between p0 and p1
plot([np.real(r['p1']), np.real(r['p0'])], [np.imag(r['p1']), np.imag(r['p0'])], 'k-', alpha=.5, lw=.5)
# label the singularities
text(np.real(r['p1']), np.imag(r['p1'])*1.1, '$p_1$', ha='center', fontsize=20)
text(.4e6, .4e7, '$z_0$', ha='center', fontsize=20)
text(np.real(r['p0']), np.imag(r['p0'])*1.2, '$p_0$', ha='center', va='bottom', fontsize=20)
xlabel('Real [Hz]'); ylabel('Imag [Hz]'); title('Singularities');


#AN IDENTICAL SIMULATION OF OP ANALYSIS AND TRAN ANALYSIS WERE DONE IN LTSPICE
#TO COMPARE WITH PYTHON RESULTS. PICTURES LOCATED IN PROGRAM FOLDER.
