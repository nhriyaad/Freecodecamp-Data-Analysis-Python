import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Sea Level Data', alpha=0.6)
    
    # Add labels, title, and legend
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('CSIRO Adjusted Sea Level (inches)', fontsize=14)
    plt.title('Scatter Plot of Sea Level Rise', fontsize=16)
    plt.legend()
    plt.grid(True)
    
    # Display the plot
    plt.show()
    # Create first line of best fit
    fit1 = linregress(x, y)
    x_fit1 = range(int(x.min()), 2051)  # Extend to the year 2050
    y_fit1 = fit1.slope * x_fit1 + fit1.intercept
    plt.plot(x_fit1, y_fit1, color='red', label='Best Fit: All Data', linestyle='--')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO Adjusted Sea Level']
    fit2 = linregress(x_recent, y_recent)
    x_fit2 = range(2000, 2051)  # Extend to the year 2050
    y_fit2 = fit2.slope * x_fit2 + fit2.intercept
    plt.plot(x_fit2, y_fit2, color='green', label='Best Fit: 2000 Onward', linestyle='-.')

    # Add labels and title
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Sea Level (inches)', fontsize=14)
    plt.title('Rise in Sea Level', fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()    
