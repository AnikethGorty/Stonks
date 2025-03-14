import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Fetch the API key from environment variables
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

if not API_KEY:
    raise ValueError("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")

# Initialize TimeSeries object
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Fetch intraday stock data for Microsoft (MSFT)
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='compact')

# Plot the data
data['4. close'].plot()
plt.title('Intraday Stock Data for MSFT')
plt.show()

print("Data fetched and plotted successfully!")