# -*- coding: utf-8 -*-
"""
Investment Growth Graph
@author: MadMerlyn
"""
num_years = 30
from invest import Invest
import matplotlib.pyplot as plt
#Build data-table
_data = Invest(1000, 400, 0.08, years=num_years)
annual = range(12,(12*num_years)+1,12)
#Generate lists from data-table
plot_data = [item for item in _data if item['period'] in annual]
total = [item['total'] for item in plot_data]
invested = [item['invested'] for item in plot_data]
interest = [item['interest'] for item in plot_data]
time = [item/12 for item in annual]

labels = ['invested', 'interest', 'total']
colors = ['blue', 'red', 'green']

plt.plot(time, invested, 'r-', time, interest, 'b-', time, total, 'g-')
plt.xlabel('Years')
plt.ylabel('USD')
plt.show()
