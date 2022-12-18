# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:30:56 2022

@author: TAK
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =['chicago','new york city','washington']
    city = input('Please, enter the city you want to analyze.\
    you may select from (chicago , new york city , washington): \n' ).lower()
    while city not in cities:
        print('Invalid choice please try again')
        city = input('Please, enter the city you want to analyze.\
    you may select from (chicago , new york city , washington): \n' ).lower()


    # get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    month=input('Please, select the month filter\n ( january, february, ... , june) or all: \n').lower()
    while month not in months :
        print('Invalid input please try again')
        month=input('Please, select the month filter\n ( january, february, ... , june) or all: \n').lower()



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day=input('Please, select the day filter\n ( monday, tuesday, ... sunday) or all: \n').lower()
    while day not in days :
        print('Invalid input please try again')
        day=input('Please, select the day filter\n ( monday, tuesday, ... sunday) or all: \n').lower()
   # return day

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month is ',common_month)


    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('The most common day of week is ',common_day)


    # display the most common start hour
    common_starthour=df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is ',common_starthour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startstation=df['Start Station'].mode()[0]
    print('The most common start station is ',common_startstation)


    # display most commonly used end station
    common_endstation=df['End Station'].mode()[0]
    print('The most common end station is ',common_endstation)


    # display most frequent combination of start station and end station trip
    common_combination=(df['Start Station']+df['End Station']).mode()[0]
    print('The  most frequent combination of start station and end station trip is \n',common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time in seconds = ',travel_time,'\n and in minutes = ',travel_time/60)


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The mean travel time = ',mean_time, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print('The count of user types is: \n',user_count)
    # Display counts of gender
    if 'Gender' in df.columns :
        gender = df['Gender'].value_counts()
        print('The counts of gender is: \n',gender)

        # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest=df['Birth Year'].min()
        print('The earliest year of birth is: ',int(earliest))

        recent = df['Birth Year'].max()
        print('Tho most recent year of birth is: ',int(recent))

        most_common = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ',int(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data?\n Enter yes or no? ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
