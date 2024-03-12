# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:39:01 2023

@author: dell
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns

# 读取Excel文件
df = pd.read_excel('components.xlsx',sheet_name=1)  # 替换为你的文件路径

# =============================================================================
# # Creating two plots, one for Eurasia and the other for North American
# 
# # Plot for Eurasia
# plt.figure(figsize=(12, 6))
# # P_Eurasia as bar plot
# plt.bar(df['Year'], df['P_Eurasia']-df['E_Eurasia'], width=0.4, label='P-E Eurasia', color='b')
# # R_Eurasia as line plot
# plt.plot(df['Year'], df['R_Eurasia'], label='R Eurasia', color='r', marker='o')
# plt.xlabel('Year')
# plt.ylabel('Values')
# plt.title('P-E VS R in Eurasia during 1981-2020')
# plt.legend()
# plt.show()
# 
# # Plot for North American
# plt.figure(figsize=(12, 6))
# # P_North American as bar plot
# plt.bar(df['Year'], df['P_North American']-df['E_North American'], width=0.4, label='P-E North American', color='b')
# # R_North American as line plot
# plt.plot(df['Year'], df['R_North American'], label='R North American', color='r', marker='o')
# plt.xlabel('Year')
# plt.ylabel('Values')
# plt.title('P-E VS R in North American during 1981-2020')
# plt.legend()
# plt.show()
# =============================================================================


# Modifying the plots with adjusted axis ranges

plt.rcParams["font.family"] = "Arial" # "Times New Roman"

min1=min(
    (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).min()-5,
    (df['R_Eurasia']-np.mean(df['R_Eurasia'])).min()-5
        ) 
min2=min(
    (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).min()-5,
    (df['R_North American']-np.mean(df['R_North American'])).min()-5
        )
max1=max(
    (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).max()+5,
    (df['R_Eurasia']-np.mean(df['R_Eurasia'])).max()+5
        ) 
max2=max(
    (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).max()+5,
    (df['R_North American']-np.mean(df['R_North American'])).max()+5
        )



# Creating a single figure with both subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

# Plot for Eurasia with dual-axis and adjusted axis ranges on the first subplot
ax1 = axes[0]
# ax1.bar(df['Year'], df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia']), width=0.4, label='P-E Eurasia', color='b')
# ax1.plot(df['Year'], df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia']), label='P-E Eurasia', color='b', marker='o')
ax1.scatter(df['Year'], 
            df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia']), 
            label='P-E Eurasia', 
            color='b')
ax1.fill_between(df['Year'], 
                 (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).rolling(window=5, min_periods=1).mean()-
                     (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).rolling(window=5, min_periods=1).std(),
                 (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).rolling(window=5, min_periods=1).mean()+
                     (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).rolling(window=5, min_periods=1).std(),  
                 color='blue', 
                 alpha=0.04)
ax1.plot(df['Year'], 
         (df['P_Eurasia']-df['E_Eurasia']-np.mean(df['P_Eurasia']-df['E_Eurasia'])).rolling(window=5, min_periods=2).mean(), 
         label='P-E Eurasia', 
         color='b', 
         linewidth=4)

ax1.set_ylabel('P-E Eurasia anamoly, mm', color='b', fontsize=20, weight='bold')
ax1.set_ylim([min1,max1])
ax1.set_xlim(1979,2021)

ax1.tick_params(axis='y', labelcolor='b', labelsize=18)
ax1.tick_params(axis='x', labelsize=18)
title1 = ax1.set_title('a. Eurasia', loc='right', fontsize=20, weight='bold')
title1.set_position((0.15, 0.7))  # x, y position of the title

ax2 = ax1.twinx()
# ax2.plot(df['Year'], df['R_Eurasia']-np.mean(df['R_Eurasia']), label='R_Eurasia', color='r', marker='o')
ax2.scatter(df['Year'], 
            df['R_Eurasia']-np.mean(df['R_Eurasia']), 
            label='R_Eurasia', 
            color='r')
ax2.fill_between(df['Year'], 
                 (df['R_Eurasia']-np.mean(df['R_Eurasia'])).rolling(window=5, min_periods=1).mean()-
                     (df['R_Eurasia']-np.mean(df['R_Eurasia'])).rolling(window=5, min_periods=1).std(),
                 (df['R_Eurasia']-np.mean(df['R_Eurasia'])).rolling(window=5, min_periods=1).mean()+
                     (df['R_Eurasia']-np.mean(df['R_Eurasia'])).rolling(window=5, min_periods=1).std(),  
                 color='r', 
                 alpha=0.04)
ax2.plot(df['Year'], 
         (df['R_Eurasia']-np.mean(df['R_Eurasia'])).rolling(window=5, min_periods=2).mean(), 
         label='R_Eurasia', 
         color='r', 
         linewidth=4)

ax2.set_ylabel('R Eurasia anamoly, mm', color='r', fontsize=20, weight='bold')
ax2.set_ylim([min1,max1])
ax2.tick_params(axis='y', labelcolor='r', labelsize=18)

# Plot for North American with dual-axis and adjusted axis ranges on the second subplot
ax3 = axes[1]
# ax3.bar(df['Year'], df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American']), width=0.4, label='P-E North America', color='b')
# ax3.plot(df['Year'], df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American']), label='P-E North America', color='b', marker='o')
ax3.scatter(df['Year'], 
        df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American']), 
        label='P-E North America', 
        color='b')
ax3.fill_between(df['Year'], 
                 (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).rolling(window=5, min_periods=1).mean()-
                     (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).rolling(window=5, min_periods=1).std(),
                 (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).rolling(window=5, min_periods=1).mean()+
                     (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).rolling(window=5, min_periods=1).std(),  
                 color='blue', 
                 alpha=0.04)
ax3.plot(df['Year'], 
         (df['P_North American']-df['E_North American']-np.mean(df['P_North American']-df['E_North American'])).rolling(window=5, min_periods=2).mean(),
         label='P-E North America', 
         color='b', 
         linewidth=4)
ax3.set_xlabel('Year', fontsize=20, weight='bold')
ax3.set_ylabel('P-E North America anamoly, mm', color='b', fontsize=18, weight='bold')
ax3.set_ylim([min2,max2])
ax3.set_xlim(1979,2021)
ax3.tick_params(axis='y', labelcolor='b', labelsize=18)
ax3.tick_params(axis='x', labelsize=18)
title3 = ax3.set_title('b. North America', loc='right', fontsize=20, weight='bold')
title3.set_position((0.25, 0.7))  # x, y position of the title

ax4 = ax3.twinx()
# ax4.plot(df['Year'], 
#          df['R_North American']-np.mean(df['R_North American']), 
#          label='R_North America', 
#          color='r', 
#          marker='o')
ax4.scatter(df['Year'], 
         df['R_North American']-np.mean(df['R_North American']), 
         label='R_North America', 
         color='r')
ax4.fill_between(df['Year'], 
                 (df['R_North American']-np.mean(df['R_North American'])).rolling(window=5, min_periods=1).mean()-
                     (df['R_North American']-np.mean(df['R_North American'])).rolling(window=5, min_periods=1).std(),
                 (df['R_North American']-np.mean(df['R_North American'])).rolling(window=5, min_periods=1).mean()+
                     (df['R_North American']-np.mean(df['R_North American'])).rolling(window=5, min_periods=1).std(),  
                 color='r', 
                 alpha=0.04)
ax4.plot(df['Year'], 
         (df['R_North American']-np.mean(df['R_North American'])).rolling(window=5, min_periods=2).mean(), 
         label='R_North America', 
         color='r', 
         linewidth=4)
ax4.set_ylabel('R North America anamoly, mm', color='r', fontsize=20, weight='bold')
ax4.set_ylim([min2,max2])
ax4.tick_params(axis='y', labelcolor='r', labelsize=18)

fig.tight_layout()
plt.show()

# =============================================================================

# plt.rcParams["font.family"] = "Arial" # "Times New Roman"

# # Define the range for Y-axis for each variable
# # p_eurasia_range = [df['P_Eurasia'].min() - 100, df['P_Eurasia'].max() ]
# r_eurasia_range = [df['R_Eurasia'].min() - 200, df['R_Eurasia'].max()+50]
# # p_north_american_range = [df['P_North American'].min() - 50, df['P_North American'].max() + 50]
# r_north_american_range = [df['R_North American'].min() - 200, df['R_North American'].max() + 50]

# # Plot for Eurasia with dual-axis and adjusted axis ranges
# fig, ax1 = plt.subplots(figsize=(12, 6))
# ax1.bar(df['Year'], df['P_Eurasia']-df['E_Eurasia'], width=0.4, label='P-E Eurasia', color='b')
# # ax1.set_xlabel('Year', fontsize=18, weight='bold')
# ax1.set_ylabel('P-E Eurasia, mm', color='b', fontsize=20, weight='bold')
# ax1.set_xlim(1979,2022)
# # ax1.set_ylim(p_eurasia_range)
# ax1.tick_params(axis='y', labelcolor='b', labelsize=18)
# ax1.tick_params(axis='x', labelsize=18) 
# 
# ax2 = ax1.twinx()
# ax2.plot(df['Year'], df['R_Eurasia'], label='R_Eurasia', color='r', marker='o')
# ax2.set_ylabel('R Eurasia, mm', color='r', fontsize=20, weight='bold')
# ax2.set_ylim(r_eurasia_range)
# ax2.tick_params(axis='y', labelcolor='r', labelsize=18)
# 
# # plt.title('P-E VS R in Eurasia during 1981-2020', fontsize=18, weight='bold')
# fig.tight_layout()
# plt.show()
# 
# # Plot for North American with dual-axis and adjusted axis ranges
# fig, ax1 = plt.subplots(figsize=(12, 6))
# ax1.bar(df['Year'], df['P_North American']-df['E_North American'], width=0.4, label='P-E North America', color='b')
# ax1.set_xlabel('Year', fontsize=20, weight='bold')
# ax1.set_ylabel('P-E North America, mm', color='b', fontsize=18, weight='bold')
# ax1.set_xlim(1979,2022)
# # ax1.set_ylim(p_north_american_range)
# ax1.tick_params(axis='y', labelcolor='b', labelsize=18)
# ax1.tick_params(axis='x', labelsize=18) 
# 
# ax2 = ax1.twinx()
# ax2.plot(df['Year'], df['R_North American'], label='R_North America', color='r', marker='o')   # color='m','g'
# ax2.set_ylabel('R North America, mm', color='r', fontsize=20, weight='bold')
# ax2.set_ylim(r_north_american_range)
# ax2.tick_params(axis='y', labelcolor='r', labelsize=18)
# 
# # plt.title('P-E VS R in North American during 1981-2020', fontsize=18, weight='bold')
# fig.tight_layout()
# plt.show()
# 
# =============================================================================
