import numpy as np 
'''
Consider the fermentation of glucose into ethanol: C6H12O6 → 2C2H5OH + 2CO2. 
A fermentor is initially charged with 10,000 liters of feed solution and the rate 
of carbon dioxide production is measured by a sensor in moles/hour. At t = 10, 20, 30, 40, 50, 60, 70, and 80 hours,
the CO2 generation rates are 58.2, 65.2, 67.8, 65.4, 58.8, 49.6, 39.1, and 15.8 moles/hour respectively.
Assuming that each reading represents the average CO2 production rate over the previous ten hours, 
calculate the total amount of CO2 generated and the final ethanol concentration in grams per liter. 
using np.array lets solve the problem! 
Ethanol molar mass = 46.07g/m
'''
ethanol_MolMass = 46.07
time = np.array([10, 20, 30, 40, 50, 60, 70,80])
rates = np.array([58.2, 65.2, 67.8, 65.4, 58.8, 49.6, 39.1,15.8])
hour_dif = 10
produced_gas_per_hour = rates*10
total_co2 = produced_gas_per_hour.sum()
print(total_co2)
print((total_co2)*46.07)
ethanol_prod = (total_co2)*46.07
conc_gL = ethanol_prod/10000
print(conc_gL)
