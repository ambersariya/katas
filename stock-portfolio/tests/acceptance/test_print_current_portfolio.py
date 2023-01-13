expected_portfolio = """|company | shares | current price | current value | last operation|
|Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018|
|Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016|
|XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018|"""


def test_should_print_current_portfolio(portfolio_tracker):
    portfolio_tracker.add_purchase(
        number_of_shares=1000, stock="Old School Waterfall Software LTD",
        purchase_date="14/02/1990")
    portfolio_tracker.add_purchase(number_of_shares=400, stock="Crafter Masters Limited",
                                   purchase_date="09/06/2016")
    portfolio_tracker.add_purchase(number_of_shares=700, stock="XP Practitioners Incorporated",
                                   purchase_date="10/12/2018")
    portfolio_tracker.add_sale(number_of_shares=500, stock="Old School Waterfall Software LTD",
                               sell_date="11/12/2018")
    portfolio_tracker.update_value(stock="Old School Waterfall Software LTD", value="5.75")
    portfolio_tracker.update_value(stock="Crafter Masters Limited", value="17.25")
    portfolio_tracker.update_value(stock="XP Practitioners Incorporated", value="25.55")

    portfolio_output = portfolio_tracker.print_portfolio()
    assert expected_portfolio == portfolio_output
