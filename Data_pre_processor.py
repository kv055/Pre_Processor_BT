
class PreProcessor:
    def __init__(self):
        pass
        
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



