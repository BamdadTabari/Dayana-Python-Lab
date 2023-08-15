import MetaTrader5 as mt5

# connect to the MetaTrader server
mt5.initialize()

# get some market data
symbol = "EURUSD"
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 10)

# print the market data
for rate in rates:
    print(rate)

# disconnect from the server
mt5.shutdown()
