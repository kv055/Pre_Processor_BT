from Data_pre_processor import PreProcessor
from vectorbt_master import vectorbt as vbt


def Backtrading(test_trades):
    Test_data_instance = PreProcessor()
    # Formating and appending a pandas dataframe tailored to vectorBT
    Test_data_instance.datastructure_VectorBT(test_trades)
    
    for asset in test_trades:
        vbt_frame = asset['VBT_Frame']
        closing_price = vbt_frame['Close']
        entries = vbt_frame['Entry']
        exits = vbt_frame['Exits']

        pf = vbt.Portfolio.from_signals(closing_price, entries, exits, init_cash=100)
        profit = pf.total_profit()
        print(profit)
        asset['VBT_PnL'] = profit
