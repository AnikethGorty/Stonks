# Stonks
I try to create a stock market simulator. 

# 14 March 2025 UPDATE:

I have made some kind of skeletal framework for this app. Using docker for containing the whole thing and pip installing my files for me. 
Python: I'm using flask library for web-based interactions. May move it offline someday, idk tho. 
I'm using AlphaVantage for historical data which will train the db.
Pandas, numpy etc for the actual training until I become competent enough to use Tensorflow. 


If you wanna quickly test/iterate this thing, just copy the code from the python file to google collab and run it there, then copy it back to VSCode. 
Over there we probably don't need Flask. Actually why do we need flask? We need to use JavaScript(gotta learn that quick) for the interaction between frontend and backend, and we'll use something like flutter to make an app to do all this stuff. Lets keep python to just the Machine Learning part.

# 18 March 2025 UPDATE:
15,16: I was at my cousin's house and couldn't bother to code with like a billion humans crowding up the house
17: Sleep deprivation
Today I downloaded a lot of data as a CSV file and saved it in the repo. I will use this data to do basic training for the algorithm.

The CSV File: I've got intraday trading data with 5 minutes interval of Gamestop Stock from 4 AM 18 Feb 2025 to 17 March 2025 8 PM. Basically a month of data of 5 mins separation. We know the opening price, closing price, high and low per 5 mins - 3818 tuples worth of data. 

## Making a Machine Learning Model
**AIM**: We want max profit and minimum loss. */Unlike/* the average WallStreetsBets user thanks to whom I even know what a gamestop even is, I want the AI to make rational decisions. 

How profitable? Sky's the limit, but the minimum profit we should be able to make on it should be proportional to the money invested. In India an FD gives you 7.10% for 1.5 years. They've predicted an inflation rate of 4.2%. I wanna keep up with inflation, and that should be enough. 

**How do we get there?**:  
I see 2 possible ways. #1: Predict how the stock market will do on a particular day and act according to that information.
#2: Just execute a number of trades and see which ones do well and when. Use this knowledge to create a trading strategy.
Will way #1 and way #2 both be equally as successful?
How would I work on this? Backtrading. I need a good backtrading library. Backtrader looking good rn
