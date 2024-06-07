import pandas as pd
def change500():
    # Load the historical data for DJIA and NASDAQ
    djia_data_path = r'C:\Users\joeym\Downloads\Dow Jones Industrial Average Historical Data.csv'
    nasdaq_data_path = r'C:\Users\joeym\Downloads\NASDAQ Composite Historical Data.csv'

    djia_data = pd.read_csv(djia_data_path, parse_dates=['Date'])
    nasdaq_data = pd.read_csv(nasdaq_data_path, parse_dates=['Date'])

    # Rename columns for clarity and consistency
    djia_data.columns = ['Date', 'DJIA_Close', 'DJIA_Open', 'DJIA_High', 'DJIA_Low', 'DJIA_Volume', 'DJIA_Change']
    nasdaq_data.columns = ['Date', 'NASDAQ_Close', 'NASDAQ_Open', 'NASDAQ_High', 'NASDAQ_Low', 'NASDAQ_Volume', 'NASDAQ_Change']

    # Ensure the data is sorted by date
    djia_data.sort_values('Date', inplace=True)
    nasdaq_data.sort_values('Date', inplace=True)

    # Merge the two datasets on the Date column
    merged_data = pd.merge(djia_data, nasdaq_data, on='Date')

    # Convert 'DJIA_Close' and 'NASDAQ_Close' to numeric
    merged_data['DJIA_Close'] = pd.to_numeric(merged_data['DJIA_Close'].str.replace(',', ''), errors='coerce')
    merged_data['NASDAQ_Close'] = pd.to_numeric(merged_data['NASDAQ_Close'].str.replace(',', ''), errors='coerce')

    # Calculate daily point changes for DJIA
    merged_data['DJIA_Point_Change'] = merged_data['DJIA_Close'] - merged_data['DJIA_Close'].shift(1)
    merged_data['NASDAQ_Point_Change'] = merged_data['NASDAQ_Close'] - merged_data['NASDAQ_Close'].shift(1)
    # Filter for days when DJIA was up by 500 points or more and NASDAQ was down
    significant_drops = merged_data[(merged_data['DJIA_Point_Change'] >= 500) & 
                                    (merged_data['NASDAQ_Close'] < merged_data['NASDAQ_Close'].shift(1))]

    # Display the dates and changes
    significant_drops = significant_drops[['Date', 'DJIA_Point_Change', 'DJIA_Close', 'NASDAQ_Point_Change', 'NASDAQ_Close']]
    print(significant_drops)

def change1Percent():
# Load the historical data for DJIA and NASDAQ
    djia_data_path = r'C:\Users\joeym\Downloads\Dow Jones Industrial Average Historical Data.csv'
    nasdaq_data_path = r'C:\Users\joeym\Downloads\NASDAQ Composite Historical Data.csv'

    djia_data = pd.read_csv(djia_data_path, parse_dates=['Date'])
    nasdaq_data = pd.read_csv(nasdaq_data_path, parse_dates=['Date'])

    # Rename columns for clarity and consistency
    djia_data.columns = ['Date', 'DJIA_Close', 'DJIA_Open', 'DJIA_High', 'DJIA_Low', 'DJIA_Volume', 'DJIA_Change']
    nasdaq_data.columns = ['Date', 'NASDAQ_Close', 'NASDAQ_Open', 'NASDAQ_High', 'NASDAQ_Low', 'NASDAQ_Volume', 'NASDAQ_Change']

    # Ensure the data is sorted by date
    djia_data.sort_values('Date', inplace=True)
    nasdaq_data.sort_values('Date', inplace=True)

    # Merge the two datasets on the Date column
    merged_data = pd.merge(djia_data, nasdaq_data, on='Date')

    # Convert 'DJIA_Close' and 'NASDAQ_Close' to numeric
    merged_data['DJIA_Close'] = pd.to_numeric(merged_data['DJIA_Close'].str.replace(',', ''), errors='coerce')
    merged_data['NASDAQ_Close'] = pd.to_numeric(merged_data['NASDAQ_Close'].str.replace(',', ''), errors='coerce')

    # Calculate daily percentage changes for DJIA
    merged_data['DJIA_Percent_Change'] = merged_data['DJIA_Close'].pct_change() * 100

    # Filter for days when DJIA was up by 1% or more and NASDAQ was down
    significant_drops = merged_data[(merged_data['DJIA_Percent_Change'] >= 1) & 
                                    (merged_data['NASDAQ_Close'] < merged_data['NASDAQ_Close'].shift(1))]

    # Display the dates and changes
    significant_drops = significant_drops[['Date', 'DJIA_Percent_Change', 'DJIA_Close', 'NASDAQ_Close']]
    print(significant_drops)
change500()
change1Percent()