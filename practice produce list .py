prices={
    'aapl':191.88,
    'goog':1186.96,
    'ibm':149.24,
    'orcl':48.44,
    'acn':166.89,
    'fb':208.09,
    'symc':21.29}
prices2={key:value for key,value in prices.items() if value>100}
print(prices2)
