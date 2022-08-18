# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:35:57 2020

@author: Andre Stevens
@description: Working with tabular data
"""
import pandas as pd
import matplotlib.pyplot as plt

aq = pd.read_csv("air_quality_no2.csv",
                 index_col=0, parse_dates=True)
# print("\n{}\n".format(aq.head()))

# EXAMPLE 1: Quick visualization
# aq.plot()

# EXAMPLE 2: Retrieve only the data from Paris
# aq["station_paris"].plot()

# EXAMPLE 3: Visually compare the NO2 values measured in London vs Paris
#aq.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

# EXAMPLE 4: 
# print([method_name for method_name in dir(aq.plot) if not method_name.startswith("_")])

# EXAMPLE 5: Boxplot
# aq.plot.box()

# EXAMPLE 5: Each column in a separate subplot
# apl = aq.plot.area(figsize=(12, 4), subplots=True)

# EXAMPLE 6: Customization example
fig, axs = plt.subplots(figsize=(12,4))
aq.plot.area(ax = axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")

