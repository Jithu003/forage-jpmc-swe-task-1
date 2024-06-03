import json
import random
import urllib.request
import time

# Assuming this URL is part of your setup
QUERY = "http://example.com/query?id={}"

def fetchQuotes():
    """ Placeholder function to simulate fetching quotes """
    quotes = [
        {"stock": "ABC", "top_bid": {"price": "120.48"}, "top_ask": {"price": "120.91"}},
        {"stock": "DEF", "top_bid": {"price": "114.07"}, "top_ask": {"price": "114.23"}},
    ]
    return quotes

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None  # Avoid division by zero
    return price_a / price_b

# Main method
if __name__ == "__main__":
    prices = {}

    # Query the price once every N seconds.
    N = 5  # Example: Change to the number of iterations you want
    for _ in range(N):
        # Simulate fetching quotes
        quotes = fetchQuotes()
        # In a real scenario, you would use:
        # quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

        # Assuming you want the ratio of two specific stocks, e.g., 'ABC' and 'DEF'
        if 'ABC' in prices and 'DEF' in prices:
            ratio = getRatio(prices['ABC'], prices['DEF'])
            print(f"Ratio ABC/DEF: {ratio}")
        else:
            print("Not enough data to calculate ratio")
        
        # Sleep for a while before the next iteration
        time.sleep(1)
