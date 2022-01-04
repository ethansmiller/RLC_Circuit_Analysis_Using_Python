*MAKE SURE TO RUN COMMAND 'pip install ahkab' IN ANACONDA POWERSHELL COMMAND PROMPT

Code was written using the provided example code and lecture notes from Professor Pham.

GUIDE:

Begin running the file 'RV_Circuit_Analysis.py'. The circuit described is a 4-Loop RV circuit, consisting of 5 resistors and 3 voltage sources.


First, we see the results of the matrix method in the console:

	[[1.2189781 ]
 	[0.88321168]
 	[5.67153285]
 	[6.54014599]]


We now see the results of Akhab analysis in the console:

	Variable    Units       Value         Error    %
	----------  -------  --------  ------------  ---
	VN1         V         5        -5e-12          0
	VN2         V         1.34307  -1.34293e-12    0
	VN3         V         7        -7.00062e-12    0
	VN4         V        11.3431   -1.13447e-11    0
	I(V1)       A        -1.21898   0              0
	I(V2)       A        -4.78832   0              0
	I(V3)       A        -6.54015  -1.77636e-15    0

*Note direction of current are all same polarity, thus can be changed to be positive


COMPARE THE TWO RESULTS:

The first loops are identical(V1), the second loop of the Akhab method (V2) is simply a subtraction of the second and third loop that share a voltage source (loops are going in opposite directions). Finally, the last loop is identical(V3).



Next, run the file 'RLC_Circuit_Analysis.py'. Note the RLC circuit is represented in the code and the values of the circuit are being stored. When ran, We first see the simple OP analysis from the Akhab package in the console.

	Variable    Units           Value         Error    %
	----------  -------  ------------  ------------  ---
	V         1            -1e-12          0
	VN2         V         0.666667     -6.66667e-13    0
	VN3         V         0.666667     -6.66667e-13    0
	VN4         V         0.666667     -6.66667e-13    0
	VN5         V         0.666667     -6.66667e-13    0
	I(V1)       A        -0.000555556   0              0
	I(L1)       A         0.000555556   0              0
	I(L2)       A         0.000555556   0              0
	I(L3)       A         0.000555556   0              0 



Next, we observe simple AC and TRAN analysis that was performed.

By opening the 'Plots' tab in Spyder, we can see the outputs. First, the tran plot is produced which shows input and output of the step applied to our circuit. This plot can also be seen in 'tran_plot.png' within the program's folder. Next, the AC plot is produced which shows an AC analysis of the same circuit. This plot can also be seen in 'ac_plot.png' within the program's folder.


Next, we observe PZ analysis that was performed.

In the console, after the AC and Tran analysis, we will see a gathered netlist, as well as the poles and zeros of our circuit.

	* p0 = -2033.9 -901.625j Hz
	* p1 = -2033.9 +901.625j Hz
	* p2 = -962.21 -1242.22j Hz
	* p3 = -962.21 +1242.22j Hz
	* p4 = -505.277 -2468.51j Hz
	* p5 = -505.277 +2468.51j Hz
	* z0 = -2.35654e+06 -1.71128e+06j Hz
	* z1 = -2.35654e+06 +1.71128e+06j Hz
	* z2 = +898511 -2.76891e+06j Hz
	* z3 = +898511 +2.76891e+06j Hz
	* z4 = +2.91024e+06 +0j Hz

The poles and zeros are also plotted in the final plot within the 'Plots' tab of Spyder. This plot can also be seen in 'pz_plot.png' within the program's folder.The blue points represent of zeros, while the red points represent poles (which are all very close to the origin).


Finally, we run an identical SPICE analysis, using the TRAN method of analysis. The SPICE circuit can be seen in 'LTSpice_RLC_Circuit.png' within the program's folder. The plot can also be found under 'LTSpice_tran_plot. We also ran a basic OP analysis in LTSpice which is found in 'LTSpice_OP_analysis.png'.



COMPARE THE PYTHON AND LTSPICE METHODS:


Comparing out LTSpice tran plot with our Python plot, we see that the two are entirely identical, thus proving a success in simulation and analysis.

Comparing our LTSpice OP analysis with our Python analysis, we see they are ALSO identical thus proving a success in simulation and analysis.


LTSPICE OP ANALYSIS RESULT:

	       --- Operating Point ---

	V(n001):	1	 	 voltage
	V(n002):	0.666667	 voltage
	V(n003):	0.666667	 voltage
	V(n004):	0.666666	 voltage
	V(n005):	0.666666	 voltage
	I(C3):	 	1.2e-019	 device_current
	I(C2):	 	1.03413e-019	 device_current
	I(C1):	 	7.958e-020	 device_current
	I(L3):	 	0.000555555	 device_current
	I(L2):	 	0.000555555	 device_current
	I(L1):	 	0.000555555	 device_current
	I(R2):	 	0.000555555	 device_current
	I(R1):	 	-0.000555555	 device_current
	I(V1):	 	-0.000555555	 device_current
