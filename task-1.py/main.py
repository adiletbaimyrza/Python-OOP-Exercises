def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'

class Solution():
    def arg_names():
        return stock_info.__code__.co_varnames