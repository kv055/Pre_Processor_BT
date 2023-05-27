from DB_Classes.Querry_Back_Testing import QuerryTradesDummyData
from DB_Classes.Querry_Live_Trading_Logs import QuerryLogStrategyOutput
from DB_Classes.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB

# # Get BackTTesting Trades from DB
# Back_Trades_Instance = QuerryTradesDummyData()
# all_trades = Back_Trades_Instance.return_all_trades()
# l = 0

# # Get LiveTrading Logs
# Live_Logs_instance = QuerryLogStrategyOutput()
# live_logs = Live_Logs_instance.return_all_log_strategy_output()
# l = 0

# Get Pricedata
Price_Data_Instance = Querry_Assets_OHLC_from_DB()
all_assets = Price_Data_Instance.return_all_assets()
sample_dict = {
            'ticker': 'XBTUSDC', 
            'historical_data_req_body': None, 
            'live_data_req_body': None, 
            'first_available_datapoint': None, 
            'historical_data_url': 'https://api.kraken.com/0/public/OHLC?pair=XBTUSDT&interval=', 
            'live_data_url': 'https://api.kraken.com/0/public/Ticker?pair=XBTUSDT', 
            'data_provider': 'Kraken',
            'last_available_datapoint': None}
ohlc = Price_Data_Instance.return_historical_ohlc_from_db(sample_dict)
l = 0
