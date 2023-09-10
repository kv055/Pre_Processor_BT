import sys
# Add the folder path containing the library to the sys.path list
sys.path.append('/home/hackerboi/Dokumente/Abelian_Code/Repositories/Pre_Procesor_BT/vectorbt-master')

from Data_pre_processor import PreProcessor
# Now you can import the library as usual
import vectorbt as vbt




def Backtrading(test_trades):
    Test_data_instance = PreProcessor()
    test_ohlc_frame = Test_data_instance.datastructure_VectorBT(test_trades)
    
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