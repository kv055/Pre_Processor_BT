from DB_Classes.Querry_Back_Testing import QuerryTradesDummyData
from DB_Classes.Querry_Live_Trading_Logs import QuerryLogStrategyOutput
from DB_Classes.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB

class PreProcessor:
    def __init__(self):
        self.back_trades_instance = QuerryTradesDummyData()
        self.live_logs_instance = QuerryLogStrategyOutput()
        self.price_data_instance = Querry_Assets_OHLC_from_DB()
        
    def get_all_trades(self):
        return self.back_trades_instance.return_all_trades()
    
    def get_trades_for_asset(self, asset):
        return self.back_trades_instance.return_trades_for_asset(asset)
    
    def get_all_live_logs(self):
        return self.live_logs_instance.return_all_log_strategy_output()
    
    def get_all_assets(self):
        return self.price_data_instance.return_all_assets()
    
    def get_historical_ohlc(self, sample_dict):
        return self.price_data_instance.return_historical_ohlc_from_db(sample_dict)



