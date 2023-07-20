"""
1. The stock_info( ) function is defined. Using the appropriate attribute of the stock_info( ) function, display
the names of all arguments to this function to the console.
An example of calling the function:
print(stock_info('ABC', 'USA', 115, '$'))
Company: ABC
Country: USA
Price: $ 115
Tip: Use the code attribute of the function.
Expected result:
('company', 'country', 'price', 'currency')
def stock_info(company, country, price, currency):
return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'
"""

def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'

# print(stock_info.__code__.co_name) #returns the name of function
# print(stock_info.__code__.co_code) #returns bytecode instructions of the function
# print(stock_info.__code__.co_argcount) #returns number of function's arguments
# print(stock_info.__code__.co_varnames) #returns tuple of string names of function arguments

attr = stock_info.__code__.co_varnames