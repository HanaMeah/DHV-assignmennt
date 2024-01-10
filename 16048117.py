# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:46:41 2024

@author: hanam
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(15, 10), layout='constrained', facecolor='lightblue')
grid = plt.GridSpec(3, 6, wspace=0.2, hspace=0.05, figure=fig)

# overall title
fig.suptitle('How did the 2020 pandemic effect plane and train travel?',
             fontsize=20, weight='bold', color='blue', va='top')

# my name and ID number
fig.text(0.85, 1, 'Name: Hana Meah' + '\nID: 16048117\n', fontsize=11,
         weight='bold', ha='left', va='top')

# 5 subplot areas, 4 for plots and 1 for brief summary
ax11 = fig.add_subplot(grid[0, 0:2])
ax12 = fig.add_subplot(grid[0, 2:4])
ax21 = fig.add_subplot(grid[1, 0:2])

ax23 = fig.add_subplot(grid[0, 4:7])
ax24 = fig.add_subplot(grid[1, 4:7])


# My brief description
fig.text(0.28, 0.57, ' Brief Summary:\n' +
         '\n Bar plot 1 & 2 shows the number of passengers travelling by' +
         '\n train in each country for 2019 compared to 2020. The pandemic' +
         '\n caused a 50% decrease overall.\n' +

         '\n The line plot shows the number of passengers travelling by' +
         '\n plane had a steady trend leading up to 2019 with a sudden fall' +
         '\n  in 2020 in each country and overall fall of -74%.\n'

         '\n The pie chart shows Covid-19 cases count in each country is linked' +
         '\n to the percentage fall in travel. The UK has the 2nd smallest' +
         '\n proportion of cases at 9.7% &largestr drop in travel suggesting' +
         '\n travel restrictions may have been stricter than other countries.\n' +
         
         '\n My final plot is a line plot for GDP in each country. There is only' +
         '\n small drop in GDP, with Switzerland showing a small increase. This' +
         '\n suggests that although the travel industry was effected, it did not' +
         '\n make a noticable change to the overall economy.\n', 
         fontsize=11, weight='bold', ha='left', va='top', color='blue')


def bargraph2019(df):
    """

    Bar Graph showing Railway Passenger Transport in 2019 - Plot 1

    """

    colors = ['royalblue', 'orange', 'green', 'red', 'mediumpurple']
    ax11.bar(df['CountryName'], df['2019'], color=colors)
    ax21.set_ylim([0, 100000])

    ax11.set(xlabel='Countries Using Railway', ylabel='Number of Passengers',
             title='Passengers Using Railway Transport 2019')

    ax11.xaxis.label.set_color('blue')
    ax11.yaxis.label.set_color('blue')
    ax11.title.set_color('blue')
    ax11.title.set_weight('bold')
    ax11.tick_params(colors='blue', which='both', labelsize=9)

    return


def bargraph2020(df):
    """

    Bar Graph showing Railway Passenger Transport in 2020 - Plot 2

    """

    colors = ['royalblue', 'orange', 'green', 'red', 'mediumpurple']
    ax21.set_ylim([0, 100000])

    ax21.bar(df['CountryName'], df['2020'], color=colors)

    ax21.set(xlabel='Countries Using Railway', ylabel='Number of Passengers',
             title='Passengers Using Railway Transport 2020')
    ax21.xaxis.label.set_color('blue')
    ax21.yaxis.label.set_color('blue')
    ax21.title.set_color('blue')
    ax21.title.set_weight('bold')
    ax21.tick_params(colors='blue', which='both', labelsize=9)

    ax21.text(0.0, 20000, '- 70%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax21.text(1.0, 55000, '- 42%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax21.text(2.0, 62000, '- 42%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax21.text(3.0, 9000, '- 38%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax21.text(4.0, 8000, '- 58%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax21.text(3.1, 70000, 'Train Travel\n' + 'Declined\n' + 'Worldwide\n' + 'by -50%',
              fontsize=10, weight='bold', ha='left', va='bottom', color='blue')
    return


def reading_my_data(datafilename):
    """

    Function to read my Airplane data csv file whcih outputs the  original 
    dataframe and the cleaned transposed data frame which I can create my line
    plot with

    """

    df_orig = pd.read_csv(datafilename)
    columns = df_orig.columns[1:]

    df_orig[columns] = df_orig[columns].apply(pd.to_numeric)

    # Transposing my dataframe
    df_transposed = df_orig.transpose()
    df_transposed.columns = df_transposed.iloc[0]
    df_transposed = df_transposed.iloc[1:]
    df_transposed = df_transposed.apply(pd.to_numeric)

    # reset index and insert a column for 'Year'
    df_transposed.reset_index(drop=True, inplace=True)
    df_transposed.insert(0, 'Year',
                         ['2015', '2016', '2017', '2018', '2019', '2020'])

    return df_transposed, df_orig


def lineplot(df):
    """

    Function to make lineplot of Plane Travel from 2015 to 2020
    to show how the trend clearly changed due to the pandemic - Plot 3

    """

    ax12.plot(df['Year'], df['UK'], label='UK')
    ax12.plot(df['Year'], df['Germany'], label='Germany')
    ax12.plot(df['Year'], df['France'], label='France')
    ax12.plot(df['Year'], df['Switzerland'], label='Switzerland')
    ax12.plot(df['Year'], df['Spain'], label='Spain')
    ax12.set(xlabel='Year of Travel', ylabel='Number of Passengers',
             title='Plane Travel Trends 2015 to 2020')
    ax12.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left')

    ax12.xaxis.label.set_color('blue')
    ax12.yaxis.label.set_color('blue')
    ax12.title.set_color('blue')
    ax12.title.set_weight('bold')
    ax12.tick_params(colors='blue', which='both')
    ax12.text(5.5, 0.5, 'Plane Travel\n' + 'Declined \n' +
              'Worldwide \n' + 'by -74% from\n' + '2019 to 2020\n', fontsize=10,
              weight='bold', ha='left', color='blue')
    
    ax12.text(4.9, 144000000, '- 78%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax12.text(4.9, 133000000, '- 76%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax12.text(4.9, 120000000, '- 65%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax12.text(4.9, 105000000, '- 70%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    ax12.text(4.9, 92000000, '- 70%\n', fontsize=10,
              weight='bold', ha='center', va='bottom', color='black')
    
    return


def piechart_covid(df, categories):
    """

    Pie Chart showing proportion of COVID 19 cases proportion of countries
    travel

    """

    ax23.pie(df, labels=categories, autopct='%1.1f%%')

    ax23.set(title='Covid-19 Cases Proportion in the World 2020')
    ax23.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left', fontsize=8)

    ax23.title.set_color('blue')
    ax23.title.set_weight('bold')

    ax23.text(0.9, -1, 'Largest proportion\n' +
              'of cases is Spain\n' +
              'which shows the 2nd\n' +
              'largest drop in travel',
              fontsize=9, weight='bold', ha='left', color='blue')

    return


def lineplotGDP(df):
    """

    This function creates a lineplot of my data for GDP

    """

    ax24.plot(df['Year'], df['UK'], label='UK')
    ax24.plot(df['Year'], df['Germany'], label='Germany')
    ax24.plot(df['Year'], df['France'], label='France')
    ax24.plot(df['Year'], df['Switzerland'], label='Switzerland')
    ax24.plot(df['Year'], df['Spain'], label='Spain')
    ax24.set(xlabel='Year Recorded', ylabel='GDP',
             title='GDP Trends per country 2015 to 2020')
    ax24.legend(loc='upper left', fontsize = 8)

    ax24.xaxis.label.set_color('blue')
    ax24.yaxis.label.set_color('blue')
    ax24.title.set_color('blue')
    ax24.title.set_weight('bold')
    ax24.tick_params(colors='blue', which='both')

    return


# read railway train data
df_railway = pd.read_csv("RailwayTransport.csv")

# call plot 1 and plot 2 functions with my railway data file as an input
bargraph2019(df_railway)
bargraph2020(df_railway)

# working out percentage decrease by country for Railway Transport
railway_2019 = df_railway['2019']
railway_2020 = df_railway['2020']
difference2 = railway_2020 - railway_2019

# list of % decrease for each country in railway
percentage_increase_rail = difference2/railway_2019 * 100

# percentage decrease overall in all countries together in railway
overall_percentage_increase_rail = np.mean(percentage_increase_rail)  # -50.47


# read air plane data
df_air_passengers, df_air_original = reading_my_data('AirPassengers.csv')

# call plot 3 function with my air transport data file as an input
lineplot(df_air_passengers)

# working out overall percentage decrease for air travel 2019 to 2020
air_2019_total = np.sum(df_air_original['2019'])
air_2020_total = np.sum(df_air_original['2020'])
difference = air_2020_total - air_2019_total
percent_increase = difference / air_2019_total * 100  # -73.6317

# working out percentage decrease by country for Railway Transport
air_2019 = df_air_original['2019']
air_2020 = df_air_original['2020']
difference3 = air_2020 - air_2019
# list of % decrease for each country in railway
percentage_increase_air = difference3/air_2019 * 100

# Description of each dataframe
df_railway.describe()
df_air_passengers.describe()

# plotting pie chart for Covid-19 cases using using my function
df_covid = pd.read_csv("CovidMobility.csv")
df = df_covid.iloc[:, -1]
categories = ['UK', 'Germany', 'France', 'Switzerland', 'Spain']

# Pie Plot
piechart_covid(df, categories)


# read GDP data and make GDP line plot
df_GDP = pd.read_csv("GDP.csv")
lineplotGDP(df_GDP)


plt.show()
