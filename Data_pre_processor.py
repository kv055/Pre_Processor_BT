import pandas as pd

class PreProcessor:
    def __init__(self):
        pass
        
    def datastructure_VectorBT(self,asset_dicts):
        asset_dicts_formated = []
        for asset in asset_dicts:
            vbt_frmame = self.price_and_trades_frame(asset)
            asset['VBT_Frame'] = vbt_frmame

        return asset_dicts_formated
    
    def price_and_trades_frame(self, asset):
        # Prepare Pricedataframe
        ohlc_data_frame = pd.DataFrame(asset['OHLC']) 
        
        ohlc_data_frame['Open'] = pd.to_numeric(ohlc_data_frame['Open'])
        ohlc_data_frame['High'] = pd.to_numeric(ohlc_data_frame['High'])
        ohlc_data_frame['Low'] = pd.to_numeric(ohlc_data_frame['Low'])
        ohlc_data_frame['Close'] = pd.to_numeric(ohlc_data_frame["Close"])
        ohlc_data_frame['Average'] = pd.to_numeric(ohlc_data_frame["Average"])

        del ohlc_data_frame['DataProvider']
        del ohlc_data_frame['CandleSize']
        
        # Convert your list of dictionaries into a DataFrame
        trades_data_frame = pd.DataFrame(asset['Trades'])

        # Create a new column 'Entry' in trades_data_frame, set to True
        trades_data_frame['Entry'] = True

        # Create a new column 'Exits' in trades_data_frame, set to True
        trades_data_frame['Exits'] = True

        # Merge the two DataFrames on the 'Timestamp'/'Open' columns
        merged_df = pd.merge(ohlc_data_frame, trades_data_frame[['Entered', 'Entry']], left_on='Timestamp', right_on='Entered', how='left')

        # Drop the 'Entered' column
        merged_df.drop('Entered', axis=1, inplace=True)

        # Replace NaN values in 'Entry' column with False
        merged_df['Entry'].fillna(False, inplace=True)

        # Merge the 'Exits' column into the existing DataFrame
        merged_df = pd.merge(merged_df, trades_data_frame[['Exit', 'Exits']], left_on='Timestamp', right_on='Exit', how='left')

        # Drop the 'Exit' column
        merged_df.drop('Exit', axis=1, inplace=True)

        # Replace NaN values in 'Exits' column with False
        merged_df['Exits'].fillna(False, inplace=True)

        # Drop duplicate rows based on 'Timestamp'
        merged_df.drop_duplicates(subset='Timestamp', keep='first', inplace=True)

        merged_df.set_index("Timestamp", inplace = True)

        print(merged_df)

        return merged_df
