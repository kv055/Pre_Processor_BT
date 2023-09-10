import pandas as pd

class PreProcessor:
    def __init__(self):
        pass
        
    def datastructure_VectorBT(self,asset_dicts):
        asset_dicts_formated = []
        for asset in asset_dicts:
            asset_dicts_formated.append(self.price_and_trades_frame(asset))

        return asset_dicts_formated
    
    def price_and_trades_frame(self, asset):
        # Prepare Pricedataframe
        ohlc_data_frame = pd.DataFrame(asset['OHLC']) 

        # ohlc_data_frame.set_index("TimeStamp", inplace = True)
        ohlc_data_frame['Open'] = pd.to_numeric(ohlc_data_frame['Open'])
        ohlc_data_frame['High'] = pd.to_numeric(ohlc_data_frame['High'])
        ohlc_data_frame['Low'] = pd.to_numeric(ohlc_data_frame['Low'])
        ohlc_data_frame['Close'] = pd.to_numeric(ohlc_data_frame["Close"])

        del ohlc_data_frame['Open']
        del ohlc_data_frame['High']
        del ohlc_data_frame['Low']
        del ohlc_data_frame['Average']
        del ohlc_data_frame['DataProvider']
        del ohlc_data_frame['CandleSize']
        
        # Convert your list of dictionaries into a DataFrame
        data_frame = pd.DataFrame(asset['Trades'])

        # Create a new column 'Entry' in data_frame, set to True
        data_frame['Entry'] = True

        # Merge the two DataFrames on the 'Timestamp'/'Open' columns
        merged_df = pd.merge(ohlc_data_frame, data_frame[['Open', 'Entry']], left_on='Timestamp', right_on='Open', how='left')

        # Drop the 'Open' column
        merged_df.drop('Open', axis=1, inplace=True)

        # Replace NaN values in 'Entry' column with False
        merged_df['Entry'].fillna(False, inplace=True)

        # Create a new column 'Exits' in data_frame, set to True
        data_frame['Exits'] = True

        # Merge the 'Exits' column into the existing DataFrame
        merged_df = pd.merge(merged_df, data_frame[['Closed', 'Exits']], left_on='Timestamp', right_on='Closed', how='left')

        # Drop the 'Closed' column
        merged_df.drop('Closed', axis=1, inplace=True)

        # Replace NaN values in 'Exits' column with False
        merged_df['Exits'].fillna(False, inplace=True)

        print(merged_df)


        return ohlc_data_frame
