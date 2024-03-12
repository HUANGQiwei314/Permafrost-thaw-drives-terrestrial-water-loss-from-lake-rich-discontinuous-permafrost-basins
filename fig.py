# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:39:01 2023

@author: dell
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib as mpl

# 文件路径
file_path = 'Fig2.xlsx'  # 替换为你的文件路径

# 子图标题和纵坐标标题
sub_titles = ['a. Annual', 'b. Ice-breakup', 'c. Ice-free', 'd. Ice-covered']
y_labels = [
    'Annual TWS anamoly, mm', 
    'Ice-breakup TWS anamoly, mm', 
    'Ice-free TWS anamoly, mm', 
    'Ice-covered TWS anamoly, mm'
]

# 变量列表
variables = ['Continuous', 'Discontinuous', 'Sporadic', 'Isolated', 'None-permafrost', '6basins']

# 设置绘图风格
sns.set()
sns.set(context='paper', palette='muted', font='sans-serif', 
        font_scale=1.2, color_codes=True, rc=None, 
        style='ticks') 
# plt.rcParams["font.family"] = "Arial" # "Times New Roman"

# 创建一个大图和4个子图
fig, axs = plt.subplots(2, 2, figsize=(18, 14))  # 调整大小和布局
axs = axs.flatten()  # 将2x2的子图数组转换为一维数组

# 循环处理每个工作表
for i in range(4):
    # 读取工作表
    df = pd.read_excel(file_path, sheet_name=i+1)  # 工作表索引从0开始

    # 计算总体均值和标准差
    for var in variables:
        df[f'{var}_overall_mean'] = df[[f'{var}1', f'{var}_mean2', f'{var}_mean3']].mean(axis=1)
        df[f'{var}_overall_std'] = df[[f'{var}1', f'{var}_mean2', f'{var}_mean3']].std(axis=1)

    # 绘制均值和标准差
    for var in variables:
        axs[i].plot(df['year'], df[f'{var}_overall_mean'], label=f'{var}', linewidth=4)
        axs[i].fill_between(df['year'], 
                            df[f'{var}_overall_mean'] - 0.3*df[f'{var}_overall_std'], 
                            df[f'{var}_overall_mean'] + 0.55*df[f'{var}_overall_std'], 
                            alpha=0.06)

    # 添加子图标题和纵坐标标题
    axs[i].set_title(sub_titles[i], loc='left', fontsize=24, weight='bold')  # 将标题放在左上角
    axs[i].set_ylabel(y_labels[i], fontsize=20, weight='bold')

    # 计算并展示回归统计信息
    regression_stats = ""
    for j in range(0, len(variables), 2):  # 每行显示两个变量的统计信息
        if j+1 < len(variables):
            var1 = variables[j]
            var2 = variables[j+1]
            slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['year'], df[f'{var1}_overall_mean'])
            slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df['year'], df[f'{var2}_overall_mean'])
            p_val_str1 = "*" if p_value1 < 0.05 else ""
            p_val_str2 = "*" if p_value2 < 0.05 else ""
            regression_stats += f"{var1}: {slope1:.2f}{p_val_str1}, {var2}: {slope2:.2f}{p_val_str2}\n"
        else:  # 处理变量数量为奇数的情况
            var = variables[j]
            slope, intercept, r_value, p_value, std_err = linregress(df['year'], df[f'{var}_overall_mean'])
            p_val_str = "*" if p_value < 0.05 else ""
            regression_stats += f"{var}: {slope:.2f}{p_val_str}\n"

    # 在子图的右上角放置回归统计信息
    axs[i].text(0.2, 0.93, regression_stats, transform=axs[i].transAxes, fontsize=20,
                verticalalignment='top', horizontalalignment='left', 
                bbox=dict(boxstyle="round,pad=0.1", edgecolor='white', facecolor='white')) # bottom
   
    axs[i].tick_params(axis='both', which='major', length=6, color='black', direction='out', labelsize=22)
    
# 设置大图的其他属性
for ax in axs:
    # ax.set_xlabel('Year')
    # 设置子图背景颜色为白色
    ax.set_facecolor('white')
    # ax.legend(fontsize=14, loc='upper right')
    # 为坐标轴添加小短线（刻度）
    ax.tick_params(axis='both', which='major', length=8, color='black', direction='out', labelsize=20)

    # 为每个子图添加黑色边框
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
axs[2].set_xlabel('Year', fontsize=20, weight='bold')
axs[3].set_xlabel('Year', fontsize=20, weight='bold')       

# 获取第一个子图的图例句柄和标签
handles, labels = axs[0].get_legend_handles_labels()

# 将图例放在大图正下方中央位置，并留出更多空间
legend = fig.legend(handles, labels, loc='lower center', 
                    bbox_to_anchor=(0.52, -0.05), 
                    ncol=len(variables), 
                    fontsize=22,
                    frameon=False)
plt.setp(legend.get_title(), weight='bold')
# 调整布局
plt.tight_layout(rect=[0, 0, 1, 0.97])  # 增加底部的空间

# 显示图表
plt.show()
