import sys
import numpy as np
from Data_pre_processor import PreProcessor
from Get_Price_Data_Class import ImportData
# Add the folder path containing the library to the sys.path list
sys.path.append('/workspaces/Pre_Procesor_BT/vectorbt-master')

# Now you can import the library as usual
import vectorbt as vbt

ohlc_instance = ImportData()
pre_processor_instance = PreProcessor()
all_trades = pre_processor_instance.get_all_trades()
# all_assets = pre_processor_instance.get_all_assets()
sample = {
    'ticker': 'XBTUSDC',
    'historical_data_req_body': None,
    'live_data_req_body': None,
    'first_available_datapoint': None,
    'historical_data_url': 'https://api.kraken.com/0/public/OHLC?pair=XBTUSDT&interval=',
    'live_data_url': 'https://api.kraken.com/0/public/Ticker?pair=XBTUSDT',
    'data_provider': 'Kraken',
    'last_available_datapoint': None
}
test_trades = pre_processor_instance.get_trades_for_asset(sample)
test_ohlc = ohlc_instance.return_ohlc_dataframe(sample)
merge = 0
test_entries = 0
tet_exits = 0

# symbol                          BTC-USD      ETH-USD
# Date                                                
# 2017-11-09 00:00:00+00:00   7143.580078   320.884003
# 2017-11-10 00:00:00+00:00   6618.140137   299.252991
# 2017-11-11 00:00:00+00:00   6357.600098   314.681000
# 2017-11-12 00:00:00+00:00   5950.069824   307.907990
# 2017-11-13 00:00:00+00:00   6559.490234   316.716003
# ...                                 ...          ...
symbols = ["BTC-USD", "ETH-USD"]
price = vbt.YFData.download(symbols, missing_index='drop').get('Close')

fast_ma = vbt.MA.run(price, 10)
slow_ma = vbt.MA.run(price, 50)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)
pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100)
profit = pf.total_profit()

l = 0