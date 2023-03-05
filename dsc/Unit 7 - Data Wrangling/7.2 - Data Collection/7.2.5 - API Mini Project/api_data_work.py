# get api key from your .env file
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NASDAQ_API_KEY')

print(API_KEY)

## ---------------------------------------------
# These are the request URL parameters
uri = 'https://data.nasdaq.com/api/v3/datasets'
database_code = 'FSE'
dataset_code = 'AFX_X'
data = "data"  # or data or metadata
return_format = 'json'

# Add any request arguments
filters = dict(
    start_date='2017-01-01',
    end_date='2018-01-01',
    # collapse='monthly',
    # transform='rdiff',
    api_key=API_KEY
)
arguments = "&".join(  [f"{x}={y}" for x,y in filters.items()]  )

# create the url
url = os.path.join(uri,database_code,dataset_code,f"{data}.{return_format}?{arguments}")

## ---------------------------------------------

# First, import the relevant modules
import requests
import json
import datetime
from datetime import datetime, date, timedelta
## ---------------------------------------------
# Now, call the Nasdaq API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
r = requests.get(url)
json_dict = r.json()

## ---------------------------------------------
# get the columns names and the data
columns = json_dict['dataset_data']['column_names']
events = json_dict['dataset_data']['data']

# cleanup the columns names for database or other
columns  = [str(x).lower().replace(" ", "_") for x in columns[1:]]

unordered_dict = {}
for event in events:
    date_string = event[:1][0]
    date = datetime.strptime(date_string, '%Y-%m-%d')
    data = event[1:]
    res = dict(zip(columns, data))
    unordered_dict[date] = res

## ---------------------------------------------
my_keys = list(unordered_dict.keys())
my_keys.sort()
nasdaq = {i: unordered_dict[i] for i in my_keys}

# earliest and latest date
print(f"earliest date: {my_keys[0]}, last_date: {my_keys[len(my_keys)-1]}")

# are all days accounted for?
# tbd

## ---------------------------------------------
for k,v in nasdaq.items():
    print(f"date: {k}, data: {v}")
    break
## ---------------------------------------------
start_date = datetime(2017,1,1)
end_date = datetime(2018,1,1)


class StockSummary:

    def __init__(self):
        self.last_date = datetime(2016,12,31)
        self.last_event = None
        self.highest_open = 0.0
        self.lowest_open = 0.0
        self.largest_1day_change = 0.0
        self.largest_2day_change = 0.0
        self.largest_trading_volume = 0.0
        self.trading_volumes = []
        self.output = []

    def summarize(self, date: datetime, event: dict):
        test = []

        self.last_date = date
        open = event['open']
        close = event['close']
        vol = event['traded_volume']
        high = event['high']
        low = event['low']
        test = [str(date), open, close, high, low]

        self.highest_open = max(open, self.highest_open)
        self.lowest_open = min(open, self.lowest_open) if self.lowest_open != 0 else open

        self.largest_1day_change = max(
            event['high'] - event['low'],
            self.largest_1day_change
        )

        if self.last_event is not None:
            self.largest_2day_change = max(
                self.last_event['high'] - event['low'],
                self.largest_2day_change
            )
        test += [self.highest_open, self.lowest_open,self.largest_1day_change,  self.largest_2day_change]

        self.last_date = date
        self.last_event = event
        return "\t".join( [str(x) for x in test] )


missing_data = []
stock = StockSummary()


def valid_float(element, field):
    if field not in element:
        return None
    datum = element[field]
    try:
        return float(datum)
    except:
        return None


def valid_record(event: dict):
    if valid_float(event, 'open') is None:
        return False
    if valid_float(event, 'close') is None:
        return False
    if valid_float(event, 'high') is None:
        return False
    if valid_float(event, 'low') is None:
        return False
    if valid_float(event, 'traded_volume') is None:
        return False
    return True

def process(start_date: datetime):
    while start_date != end_date:

        if start_date not in nasdaq:
            t = (start_date,)
            missing_data.append(t)
        else:
            event = nasdaq[start_date]
            if not valid_record(event):
                missing_data.append((start_date, event))
            else:
                output = stock.summarize(start_date, event)
                print(output)
                # file1.write(output+"\n")

        start_date += timedelta(days=1)

if __name__ == '__main__':
    process(start_date=start_date)

#%%
