import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate x values for prediction (from 1880 to 2050)
    years_extended = pd.Series(range(1880, 2051))
    line1 = slope * years_extended + intercept
    plt.plot(years_extended, line1, 'r', label='Best Fit Line (1880-2050)', linewidth=2)

    # Create second line of best fit (data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate x values for prediction (from 2000 to 2050)
    years_recent = pd.Series(range(2000, 2051))
    line2 = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line2, 'green', label='Best Fit Line (2000-2050)', linewidth=2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()