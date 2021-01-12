import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import stats


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    df.plot.scatter('Year','CSIRO Adjusted Sea Level',label='original data',figsize=(12, 7))


    # Create first line of best fit
    yearto2050 = pd.Series([int(i) for i in range(1880, 2051)])
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(yearto2050, intercept + slope*yearto2050, 'r', label='best fit')
    


    # Create second line of best fit
    recent = df[df['Year']>=2000]
    slope_y, intercept_y, r_y, p_y, std_err_y = stats.linregress(recent['Year'],recent['CSIRO Adjusted Sea Level'])

    yearto2050_2 = pd.Series([int(i) for i in range(2000, 2051)])
    plt.plot(yearto2050_2, intercept_y + slope_y*yearto2050_2, 'g', label='>year 2000')


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend(fontsize="medium")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()