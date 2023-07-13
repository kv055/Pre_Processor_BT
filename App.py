import sys
from Data_pre_processor import PreProcessor
from Get_Price_Data_Class import ImportData
# Add the folder path containing the library to the sys.path list
sys.path.append('/workspaces/Pre_Procesor_BT/vectorbt-master')

# Now you can import the library as usual
import vectorbt as vbt

ohlc_instance = ImportData()
pre_processor_instance = PreProcessor()
# all_trades = pre_processor_instance.get_all_trades()
# all_assets = pre_processor_instance.get_all_assets()

sample = {
    'ticker': 'AAVEETH',
    'historical_data_req_body': None,
    'live_data_req_body': None,
    'first_available_datapoint': None,
    'historical_data_url': 'https://api.kraken.com/0/public/OHLC?pair=AAVEUSD&interval=',
    'live_data_url': 'https://api.kraken.com/0/public/Ticker?pair=AAVEUSD',
    'data_provider': 'Kraken',
    'last_available_datapoint': None
}

test_trades = pre_processor_instance.get_trades_for_asset(sample)
test_ohlc_frame = ohlc_instance.return_ohlc_dataframe(sample)

for position in test_trades['trades']:
    position_open = position['Open'].strftime("%Y-%m-%d")
    position_close = position['Closed'].strftime("%Y-%m-%d")

    test_ohlc_frame.loc[position_open, 'Entries'] = True
    test_ohlc_frame.loc[position_close, 'Exits'] = True

test_ohlc_frame.fillna(False, inplace=True)

closing_price = test_ohlc_frame['Close']
entries = test_ohlc_frame['Entries']
exits = test_ohlc_frame['Exits']


pf = vbt.Portfolio.from_signals(closing_price, entries, exits, init_cash=100)
profit = pf.total_profit()

l = 0