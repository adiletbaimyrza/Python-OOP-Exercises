def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'

# print(stock_info.__code__.co_name) #returns the name of function
# print(stock_info.__code__.co_code) #returns bytecode instructions of the function
# print(stock_info.__code__.co_argcount) #returns number of function's arguments
# print(stock_info.__code__.co_varnames) #returns tuple of string names of function arguments

class Solution():
    def arg_names():
        return stock_info.__code__.co_varnames