import time
import pandas as pd
import numpy as np

# dictionary of the cities and there .csv-files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# dictionary of name of days per week and there day number starting by 0
DAYS_OF_WEEK = {'monday': 0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}

#dictionary of names and numbers of the months
MONTHS = {'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    bln_check = False
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while bln_check == False:
        city = input('For which city do you wanna get the data - chicago, new york city, washington? Please type in.\n')
        city = city.lower()
        if city in CITY_DATA:
            bln_check = True
        else:
            print('Wrong city - please type in a correct one.')
    
    str_filter = input('\nDo you wanna filter data by day, month, both or not at all? - Input "none" for no filter.\n')
    
    if str_filter == 'both':
        # get user input for month (all, january, february, ... , june)
        bln_check = False
        while bln_check == False:
            month = input('\nFor which month do you wanna get the data - january, ..., june or all of them? Please type in.\n')
            if month.lower() in MONTHS or month.lower() == 'all':
                bln_check = True
            else:
                print('Wrong month or no data for the asked month - please try again.')

        # get user input for day of week (all, monday, tuesday, ... sunday)
        bln_check = False
        while bln_check == False:
            day = input('\nFor which day of week do you wanna get the data - monday, ..., sunday or all? Please type in.\n')
            if day.lower() in DAYS_OF_WEEK or day.lower() == 'all':
                bln_check = True
            else:
                print('Wrong day - please try again.')
                       
    elif str_filter == 'month':
        # get user input for month (all, january, february, ... , june)
        bln_check = False
        while bln_check == False:
            month = input('\nFor which month do you wanna get the data - january, ..., june or all of them? Please type in.\n')
            if month.lower() in MONTHS or month.lower() == 'all':
                bln_check = True
                day = 'all'
            else:
                print('Wrong month or no data for the asked month - please try again.')
                       
    elif str_filter == 'day':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        bln_check = False
        while bln_check == False:
            day = input('\nFor which day of week do you wanna get the data - monday, ..., sunday or all? Please type in.\n')
            if day.lower() in DAYS_OF_WEEK or day.lower() == 'all':
                bln_check = True
                month = 'all'
            else:
                print('Wrong day - please try again.')
                       
    elif str_filter == 'none':
        month = ''
        day = ''
                 
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
    # set 
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all' and month != '':
        # use the index of the months list to get the corresponding int
        month = MONTHS[month]

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all' and day != '':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAYS_OF_WEEK[day.lower()]]

    return df


def time_stats(df):
    """
    Asks user to specify a city, month, and day to analyze.

    Args:
        (DataFrame) df - data of the <cityname>.csv file
    Prints:
        - the most common month of the bike rentals
        - the most common day of week of the bike rentals
        - the most common start hour of the bike rentals 
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mean()
    for month, number in MONTHS.items():
        if number == int(common_month):
            print('The most common month:\n    Month: {}\n'.format(month.title()))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mean()
    for day, number in DAYS_OF_WEEK.items():
        if number == int(common_day):
            print('The most common day:\n    Day: {}\n'.format(day.title()))   

    # TO DO: display the most common start hour
    df_hours = df['Start Time'].dt.hour
    common_hour = df_hours.mean()
    print('The most common start hour is {}h.'.format(int(common_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def int_to_time(time_seconds):
    """
    Calculates the days, hours, minutes and seconds according to the argument time_seconds.
    First the days will be calculated. Then of the rest the hours are calulated, then the minutes and the rest are the seconds.

    Args:
        (DataFrame) df - data of the <cityname>.csv file
    Returns:
        (int) days - number of full days of the time in seconds
        (int) hours - number of full hours of the time in seconds
        (int) minutes - number of full minutes of the time in seconds
        (int) seconds - number of seconds
    """
    days = time_seconds // (24 * 3600)
    time_seconds = time_seconds % (24 * 3600)
    hours = time_seconds // 3600
    time_seconds = time_seconds % 3600
    minutes = time_seconds // 60
    time_seconds %= 60
    seconds = time_seconds

    return days, hours, minutes, seconds


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - DataFrame of the <cityname>.csv file

    Prints:
        - name of the most commonly used start station and how often it was used
        - name of the most commonly used end station and how often it was used
        - station names of the most commonly used station combination and how often it appeared
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df.groupby(['Start Station'])['Start Station'].count()
    max_start_station_name = start_station.idxmax()
    max_start_station_value = start_station[max_start_station_name]
    print('The most commonly used start station is: \n    Name:  {},\n    Count: {}\n'.format(max_start_station_name, max_start_station_value))

    # TO DO: display most commonly used end station
    end_station = df.groupby(['End Station'])['End Station'].count()
    max_end_station_name = end_station.idxmax()
    max_end_station_value = end_station[max_end_station_name]
    print('The most commonly used end station is: \n    Name:  {},\n    Count: {}\n'.format(max_end_station_name, max_end_station_value))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station'] + '|' + df['End Station']
    trip_combination = df.groupby(['station_combination'])['station_combination'].count()
    max_trip_combination_name = trip_combination.idxmax()
    max_trip_combination_value = trip_combination[max_trip_comb_name]
    list_stationcombination = max_trip_combination_name.split('|')
    print('The most frequent combination of start and end station is:\n    Start Station: {},\n    End Station:   {},\n    Count:         {}\n'.format(list_stationcombination[0], list_stationcombination[1], max_trip_combination_val))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
        
    Args:
        (DataFrame) df - DataFrame of the <cityname>.csv file

    Prints:
        - total travel time in days, hours, minutes and seconds
        - mean travel time in days, hours, minutes and seconds
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    days, hours, minutes, seconds = int_to_time(total_travel_time)
    print('The total travel time:\n    Days:    {}, \n    Hours:   {}, \n    Minutes: {}, \n    Seconds: {}\n'.format(int(days),int(hours),int(minutes),int(seconds)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    days,hours,minutes,seconds = int_to_time(mean_travel_time)
    print('The mean travel time:\n    Days:    {}, \n    Hours:   {}, \n    Minutes: {}, \n    Seconds: {}\n'.format(int(days),int(hours),int(minutes),int(seconds)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
            
    Args:
        (DataFrame) df - DataFrame of the <cityname>.csv file

    Prints:
        - name and appearence count of the different user types
        - name and appearence count of the different genders
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    for user, counter in user_types.iteritems():
        print('The appearence of user types: \n    User Type: {},  \n    Appearence: {}\n'.format(user, counter))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df.groupby(['Gender'])['Gender'].count()
        for gender, counter in gender_types.iteritems():
            print('The appearence of genders: \n    Gender:     {},  \n    Appearence: {}\n'.format(gender, counter))
    else:
        print('There is no column "Gender" in file of city {}'.format(city.title()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_years = df['Birth Year']
        min_birth_year = birth_years.min()
        max_birth_year = birth_years.max()
        mean_birth_year = birth_years.mean()
        print('Birth Year appearences: \n    Earliest:    {}, \n    Most recent: {}, \n    Most common: {}'.format(int(min_birth_year), int(max_birth_year),int(mean_birth_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_dataframes(df):
    """Displays the filtered data of the dataframe

    Args:
        (DataFrame) df - DataFrame of the <cityname>.csv file

    Prints:
        - 5 rows of the dataframe per decision
    """
    view_data = input('\nDo you wanna see the first 5 rows of the filtered data? Enter yes or no.\n')
    start_loc = 0
    while view_data.lower() != 'no':
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_data = input('\nDo you wanna see the next 5 rows of the filtered data? Enter yes or no.\n')

def main():
    """main methode"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        show_dataframes(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()