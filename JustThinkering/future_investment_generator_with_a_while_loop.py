investment = 10000
year = 0
while year < 20:
    yearly_investment = investment * 0.05
    investment += yearly_investment
    year += 1
    investment = round(investment, 2)
    print(investment)
