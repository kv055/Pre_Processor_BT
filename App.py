from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pandas as pd
import datetime
import os.path
import sys

import backtrader as bt
import pandas as pd
import backtrader.analyzers as btanalyzers
from Data_pre_processor import PreProcessor
from Backtrader_Strategy import SmaCross
from Get_Price_Data_Class import ImportData

# Create an instance of the component
my_component = PreProcessor()
all_assets = my_component.get_all_assets()

ohlc_instance = ImportData()
sample_dict = {
    'ticker': 'XBTUSDC',
    'historical_data_req_body': None,
    'live_data_req_body': None,
    'first_available_datapoint': None,
    'historical_data_url': 'https://api.kraken.com/0/public/OHLC?pair=XBTUSDT&interval=',
    'live_data_url': 'https://api.kraken.com/0/public/Ticker?pair=XBTUSDT',
    'data_provider': 'Kraken',
    'last_available_datapoint': None
}
dataframe = ohlc_instance.return_ohlc_dataframe(sample_dict)


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(SmaCross)

    # Pass it to the backtrader data feed and add it to cerebro
    datafeed = bt.feeds.PandasData(dataname=dataframe)

    # Add the data feed to cerebro
    cerebro.adddata(datafeed)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.01)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Optimize the strategy parameters
    cerebro.optstrategy(
        SmaCross,
        pfast=range(5,25),  # Specify the range of values for pfast
        pslow=range(10,50)  # Specify the range of values for pslow
    )

    cerebro.addanalyzer(btanalyzers.Returns, _name = "returns")

    # Run the optimization
    results = cerebro.run()

    par_list = [[
        x[1].params.pfast, 
        x[1].params.pslow,
        x[1].analyzers.returns.get_analysis()['rnorm100'], 
        # x[0].analyzers.drawdown.get_analysis()['max']['drawdown'],
        # x[0].analyzers.sharpe.get_analysis()['sharperatio']
    ] for x in results]


	
par_df = pd.DataFrame(par_list, columns = ['length_fast', 'length_slow', 'return'])
# , 'dd', 'sharpe'

l = 0