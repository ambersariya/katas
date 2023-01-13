expected_portfolio = """|company | shares | current price | current value | last operation|
|Old School Waterfall Software LTD | 500 | $5.75 | $2,875.00 | sold 500 on 11/12/2018|
|Crafter Masters Limited | 400 | $17.25 | $6,900.00 | bought 400 on 09/06/2016|
|XP Practitioners Incorporated | 700 | $25.55 | $17,885.00 | bought 700 on 10/12/2018|"""

purchase_dates = [
    "14/02/1990",
    "09/06/2016",
    "10/12/2018",
    "11/12/2018"
]


def test_should_print_current_portfolio(mocker, portfolio_tracker):
    with mocker.patch('datetime.datetime.now') as patched_datetime:
        patched_datetime.side_effect = purchase_dates
        portfolio_tracker.add_purchase(number_of_shares=1000,
                                       asset_name="Old School Waterfall Software LTD")
        portfolio_tracker.add_purchase(number_of_shares=400, asset_name="Crafter Masters Limited")
        portfolio_tracker.add_purchase(number_of_shares=700,
                                       asset_name="XP Practitioners Incorporated")

        portfolio_tracker.add_sale(number_of_shares=500,
                                   asset_name="Old School Waterfall Software LTD")

        portfolio_tracker.update_value(asset_name="Old School Waterfall Software LTD", value="5.75")
        portfolio_tracker.update_value(asset_name="Crafter Masters Limited", value="17.25")
        portfolio_tracker.update_value(asset_name="XP Practitioners Incorporated", value="25.55")

        portfolio_output = portfolio_tracker.print_portfolio()
        assert expected_portfolio == portfolio_output
