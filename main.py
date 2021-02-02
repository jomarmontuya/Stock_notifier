from stock_notifier import Stock, SMS
import os

# Stock authentication API key from https://www.alphavantage.co/
STOCK_AUTH_KEY = os.environ.get("STOCK_AUTH_KEY")
# Change STOCK Ticker Depending on your need
STOCK = "TSLA"
# Change Company Name Depending on your need
COMPANY = "Tesla"

# Get API KEY From STOCK https://newsapi.org/
NEWS_AUTH_KEY = os.environ.get("NEWS_AUTH_KEY")

# Register account twilio and get Account SID and Account Token
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
ACCOUNT_TOKEN = os.environ.get("ACCOUNT_TOKEN")

# Get your own number from twilio
FROM_NUMBER = +15625219232
# Change to number depending on your need
# Notice: Free trial projects are only allowed to add verified caller IDs via SMS.
# https://support.twilio.com/hc/en-us/articles/223180048-Adding-a-Verified-Phone-Number-or-Caller-ID-with-Twilio
TO_NUMBER = +639981740071

# Create New Instance of Stock Class Pass in Stock auth key from https://www.alphavantage.co/ and stock ticker
stock = Stock(apikey=STOCK_AUTH_KEY, stock_symbol=STOCK)
# Stock Class has get_data method that returns stock data in json format
x = stock.get_data()
print(x)

# Stock Class has get_new method that returns latest news regarding to the stock but you must pass in
# News api key from  https://newsapi.org/ and company name
y = stock.get_news(NEWS_AUTH_KEY, COMPANY)
print(y)

# SMS is another class within stock notifier you can notify stock update to sms using twilio
# SMS class must pass in account_sid and account_token from twilio
sms = SMS(ACCOUNT_SID, ACCOUNT_TOKEN)
# SMS class has send method to send actual message but you must pass in
# from number your twilio phone number and to number and message
sms.send(FROM_NUMBER, TO_NUMBER, "Hello There!")
