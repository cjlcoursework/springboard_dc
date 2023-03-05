#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from https://data.nasdaq.com/ (formerly Quandl API).

# As a first step, you will need to register a free account on the https://data.nasdaq.com/ website.

# After you register, you will be provided with a unique API key, that you should store:
# 
# *Note*: Use a `.env` file and put your key in there and `python-dotenv` to access it in this notebook. 
# 
# The code below uses a key that was used when generating this project but has since been deleted. Never submit your keys to source control. There is a `.env-example` file in this repository to illusrtate what you need. Copy that to a file called `.env` and use your own api key in that `.env` file. Make sure you also have a `.gitignore` file with a line for `.env` added to it. 
# 
# The standard Python gitignore is [here](https://github.com/github/gitignore/blob/master/Python.gitignore) you can just copy that. 

# In[43]:


# get api key from your .env file
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('NASDAQ_API_KEY')

print(API_KEY)


# Nasdaq Data has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# ## create the uri
# > for calling Nasdaq with a dataset and arguments

# In[44]:


# These are the request URL parameters
uri = 'https://data.nasdaq.com/api/v3/datasets'
database_code = 'FSE'
dataset_code = 'AFX_X'
data = "data"  # or data or metadata
return_format = 'json'

# Add any request arguments
filters = dict(
    start_date='2016-12-28',   # keep a few extra dates in case the api calculates non-inclusive - we'll filter them out later
    end_date='2018-01-02',
    # collapse='monthly',
    # transform='rdiff',
    api_key=API_KEY
)
arguments = "&".join(  [f"{x}={y}" for x,y in filters.items()]  )

# create the url
url = os.path.join(uri,database_code,dataset_code,f"{data}.{return_format}?{arguments}")


# You can find the detailed Nasdaq Data API instructions here: https://docs.data.nasdaq.com/docs/in-depth-usage

# While there is a dedicated Python package for connecting to the Nasdaq API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# ## imports

# In[45]:


# First, import the relevant modules
import requests
import json
import datetime
from datetime import datetime, date, timedelta
from functools import reduce


# Note: API's can change a bit with each version, for this exercise it is reccomended to use the nasdaq api at `https://data.nasdaq.com/api/v3/`. This is the same api as what used to be quandl so `https://www.quandl.com/api/v3/` should work too.
# 
# Hint: We are looking for the `AFX_X` data on the `datasets/FSE/` dataset.

# ## request the data

# In[46]:


# Now, call the Nasdaq API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
r = requests.get(url)
json_dict = r.json()


# ## inspect the data

# In[47]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure

#print(json.dumps(json_dict, indent=2))


# Collect data from the Frankfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD)
# Convert the returned JSON object into a Python dictionary

# In[48]:


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


# In[49]:


my_keys = list(unordered_dict.keys())
my_keys.sort()
nasdaq = {i: unordered_dict[i] for i in my_keys}

# earliest and latest date
print(f"earliest date: {my_keys[0]}, last_date: {my_keys[len(my_keys)-1]}")

# are all days accounted for?
 # tbd


# In[50]:


#
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

    def summarize(self, date: datetime, event: dict):
        self.last_date = date
        try:
            open = event['open']
            close = event['close']
            vol = event['traded_volume']
            self.highest_open = max(open, self.highest_open)
            self.lowest_open = min(open, self.lowest_open) if self.lowest_open != 0 else open

            self.largest_1day_change = max(
                event['high'] - event['low'],
                self.largest_1day_change
            )

            if self.last_event is not None:
                self.largest_2day_change = max(
                    self.last_event['close'] - event['close'],
                    self.largest_2day_change
                )

            self.trading_volumes.append(event['traded_volume'])
        except Exception as e:
            print(e)

        self.last_date = date
        self.last_event = event


# In[51]:


def valid_float(element, field) -> float or None:
    if field not in element:
        return None
    datum = element[field]
    try:
        return float(datum)
    except:
        return None

def valid_record(event: dict) -> bool:
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


def sum_array(arr: list[float]) -> float:
    sum = reduce(lambda x, y: x+y, arr)
    return(sum)

def median_array(arr: list[float]) -> float:
    arr.sort()
    n = len(arr)
    half = n / 2
    if n % 2 == 0:
        x = arr[int(half) - 1]
        y = arr[int(half)]
        median = (x + y) / 2
    else:
        median = arr[int(half)]
    return median


# In[52]:


start_date = datetime(2017,1,1)
end_date = datetime(2018,1,1)
missing_dates = []
missing_data = []
stock = StockSummary()


# In[53]:


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


# ## Tasks

# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# ### 3. Calculate what the highest and lowest opening prices were for the stock in this period.

# In[ ]:


print(f"Highest open: {stock.highest_open}")
print(f"Lowest open: {stock.lowest_open}")


# ### 4. What was the largest change in any one day (based on High and Low price)

# In[ ]:


print(f"Largest one day change: {stock.largest_1day_change}")


# ### 5. What was the largest change between any two days (based on Closing Price)

# In[ ]:


print(f"Largest difference between previous close and next day close: {stock.largest_2day_change}")


# ## 6. What was the average daily trading volume during this year

# In[ ]:


average_trading_volume  = sum_array(stock.trading_volumes) / len(stock.trading_volumes)
print(f"Average daily trading volume during 2017: {average_trading_volume}")


# ### (Optional) What was the median trading volume during this year.

# In[ ]:


median_trading_volume  = median_array(stock.trading_volumes)
print(f"Median trading volume during 2017: {median_trading_volume}")

