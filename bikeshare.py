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
    city = input('would you like to see data for Chicago, NYC, or Washington?').lower()
    while city not in CITY_DATA.keys():
            city = input('Please inter a valid name. Chicago, New York, or Washington?  ').lower()



    # get user input for month (all, january, february, ... , june)
    months=['all','january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']
    while True:
        month = input('what month you would like to pull data from?  ').lower()
        if month in months:
            break
        else:
            print ('incorrect value')



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('what day you would like to pull data from?  ').lower()
        if day in days:
            break
        else:
            print ('incorrect value')

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

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

    popular_month = df['month'].mode()[0]
    print('The most common month is -> {}'.format(popular_month))


    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('The most common month is -> {}'.format(popular_day))



    # display the most common start hour


    popular_hour = df['Hour'].mode()[0]

    print('The most common month is -> {}'.format(popular_day))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is -> {}'.format(popular_start_station))


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is -> {}'.format(popular_end_station))



    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+','+df['End Station']
    combination = df['combination'].mode()[0]
    print('The most frequent used combination is -> {}'.format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print ('the total of travel time is -> {}'.format(total_time))


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print ('the mean of travel time is -> {}'.format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print ('counts of user types -> {}'.format(user_types))




    # Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts().to_frame()
        print('the counts of genders is -> {}'.format(gender_count))
    # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        print ('the earliest year of birth is -> {}'.format(earliest_year))
        recent_year = int(df['Birth Year'].max())
        print ('the most recent year of birth is -> {}'.format(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print ('the most common year of birth is -> {}'.format(common_year))
    else:
        print('there is no data for this city')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()