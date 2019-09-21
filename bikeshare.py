import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    month = ""
    day = ""
    print('Hola! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter a city you would like data for: ")
        city = city.lower()
        if city in CITY_DATA.keys():
            break
        print("Your type the wrong city. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you like to see in the data: ")
        month = month.lower()
        if month in MONTHS:
            break
        print("This is an invalid month. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day do you like to see in the data: ")
        day = day.lower()
        if day in DAY:
            break
        print("This is an invalid day. Please try again.")

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
    file = CITY_DATA[city]
    df = pd.read_csv(file)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month_name()
    df['Start Hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df.loc[df['month'] == month.capitalize()]
    if day != 'all':
        df = df.loc[df['day'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    cm = df.groupby('month').size().reset_index(name="count").sort_values(by='count', ascending=False)
    cm = cm.reset_index(drop=True)
    print(cm['month'][0] + ' is the most common month for this data')
    

    # TO DO: display the most common day of week
    cd = df.groupby('day').size().reset_index(name="count").sort_values(by='count', ascending=False)
    cd = cd.reset_index(drop=True)
    print(cd['day'][0] + ' is the most common day for this data')

    # TO DO: display the most common start hour
    ch = df.groupby('Start Hour').size().reset_index(name="count").sort_values(by='count', ascending=False)
    ch = ch.reset_index(drop=True)
    print(str(ch['Start Hour'][0]) + ' is the most common hour for this data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss = df.groupby('Start Station').size().reset_index(name="count").sort_values(by='count', ascending=False)
    ss = ss.reset_index(drop=True)
    print(ss['Start Station'][0] + ' is the most common start station for this data')

    # TO DO: display most commonly used end station
    es = df.groupby('End Station').size().reset_index(name="count").sort_values(by='count', ascending=False)
    es = es.reset_index(drop=True)
    print(es['End Station'][0] + ' is the most common end station for this data')

    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station']).size().reset_index(name="count").sort_values(by='count', ascending=False)
    combo = combo.reset_index(drop=True)
    
    print(combo['Start Station'][0] + ' ' + combo['End Station'][0] + ' is the most common start station and end station combination for this data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is ' + str(total_time) + ' seconds')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The average travel time is ' + str(avg_time) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ut = df.groupby('User Type').size().reset_index(name="count")
    print(ut)

    # TO DO: Display counts of gender
    try:
        gender = df.groupby('Gender').size().reset_index(name="count")
        print(gender)
    except:
        print('no gender data available')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        yb = df.groupby('Birth Year').size().reset_index(name="count").sort_values(by='count', ascending=False)
        yb = yb.reset_index(drop=True)
        print(str(int(yb['Birth Year'][0])) + ' is the most common year of bith for this data')
    
        eyb = df.sort_values(by='Birth Year', ascending=True)
        eyb = eyb.reset_index(drop=True)
        print(str(int(eyb['Birth Year'][0])) + ' is the earliest year of bith for this data')

        mryb = df.sort_values(by='Birth Year', ascending=False)
        mryb = mryb.reset_index(drop=True)
        print(str(int(mryb['Birth Year'][0])) + ' is the most recent year of bith for this data')
        
    except:
        print('no birth year data available')
    
    data = ""
    while True:
         data = input("Do you want to see 5 lines of raw data?: ")
         data = data.lower()
         print(df.head())
         if data.lower() != 'yes':
            break
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
