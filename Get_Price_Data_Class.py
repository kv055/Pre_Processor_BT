"""
This is the object oriented version of the "Price data" folder
One benefit of using these class calls can be seen in app.py
wherein the bin_url can be inserted later on
This allows for any data source to be used at runtime.
"""
import numpy
import pandas as pd
import csv
from io import StringIO

from DB_Classes.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB

class ImportData:
    """Class"""
    def __init__(self):
        self.querry = Querry_Assets_OHLC_from_DB()

    def Querry_ohlc_dict_from_DB(self, asset_dict):
        # self.querry.db_connection.cursor = self.querry.db_connection.connection.cursor(dictionary=True)
        self.ohlc_dict = self.querry.return_historical_ohlc_dict_from_db(asset_dict)

    def Querry_ohlc_list_from_DB(self, asset_dict):
        # self.querry.db_connection.cursor = self.querry.db_connection.connection.cursor(named_tuple=True)
        self.ohlc_list = self.querry.return_historical_ohlc_list_from_db(asset_dict)
        # self.ohlc_list = [list(tup) for tup in ohlc_tuple]

    def Querry_average_price_dict_from_DB(self, asset_dict):
        self.querry.db_connection.cursor = self.querry.db_connection.connection.cursor(dictionary=True)
        self.average_price_dict = self.querry.return_historical_average_price_from_db(asset_dict)
        

    def Querry_average_price_list_from_DB(self, asset_dict):
        self.querry.db_connection.cursor = self.querry.db_connection.connection.cursor(named_tuple=True)
        ohlc_tuple = self.querry.return_historical_ohlc_from_db(asset_dict)
        self.average_price_list = [list(tup) for tup in ohlc_tuple]
        for row in self.average_price_list:
            average = (row[1] + row[2] + row[3] + row[4])/4
            row.pop(1)
            row.pop(1)
            row.pop(1)
            row.pop(1)
            row.append(average)

    def Create_seperate_ohlc_traces(self, asset_dict):
        self.separated_ohlc_traces_dict = {
            'Date': [],
            'Open': [],
            'High': [],
            'Low': [],
            'Close': []
        }

        self.Querry_ohlc_list_from_DB(asset_dict)
        
        for row in self.ohlc_list:
            self._dict['Date'].append(row)
            self.separated_ohlc_traces_dict['Open'].append(row)
            self.separated_ohlc_traces_dict['high'].append(row)
            self.separated_ohlc_traces_dict['low'].append(row)
            self.separated_ohlc_traces_dict['close'].append(row)

    def Create_seperate_average_price_traces(self, asset_dict):
        self.separated_average_price_traces_dict = {
            'Date': [],
            'Average_Price': []
        }

        self.Querry_average_price_list_from_DB(self, asset_dict)
                
        for row in self.average_price_list:
            self.separated_ohlc_traces_dict['Date'].append(row[0])
            self.separated_ohlc_traces_dict['Open'].append(row[1])
    
    def Create_ohlc_CSV(self,asset_dict):
        # self.Querry_ohlc_dict_from_DB(asset_dict)
        self.Querry_ohlc_list_from_DB(asset_dict)
        # Create a StringIO object to hold the CSV data
        csv_data = StringIO()
        # Create a CSV writer
        writer = csv.writer(csv_data)
        # Write the rows to the CSV writer
        # writer.writerows(self.ohlc_dict,self.average_price_list)
        writer.writerows(self.ohlc_list)
        # Seek to the beginning of the StringIO object
        csv_data.seek(0)
        return csv_data.getvalue()

    def Create_average_price_CSV(self, asset_dict):
        self.Querry_average_price_list_from_DB(asset_dict)
        # Create a StringIO object to hold the CSV data
        csv_data = StringIO()
        # Create a CSV writer
        writer = csv.writer(csv_data)
        # Write the rows to the CSV writer
        # writer.writerows(self.ohlc_dict,self.average_price_list)
        writer.writerows(self.average_price_list)
        # Seek to the beginning of the StringIO object
        csv_data.seek(0)
        return csv_data.getvalue()

    def Create_ohlc_numpy_array(self,asset_dict):
        """Method"""
        self.Create_seperate_ohlc_traces(asset_dict)

        open = numpy.array(self.separated_ohlc_traces_dict['Open'])
        high = numpy.array(self.separated_ohlc_traces_dict['High'])
        low = numpy.array(self.separated_ohlc_traces_dict['Low'])
        close = numpy.array(self.separated_ohlc_traces_dict['Close'])

        self.ohlc_numpy_array = {
            'np_Open': open,
            'np_High': high,
            'np_Low': low,
            'np_Close': close
        }

    def Create_average_price_numpy_array(self,asset_dict):
        """Method"""
        self.Create_seperate_average_price_traces(asset_dict)

        average = numpy.array(self.separated_ohlc_traces_dict['Average_Price'])

        self.average_price_numpy_array = {
            'np_Average': average,
        }

    def Create_ohlc_dataframe(self,asset_dict):
        self.Querry_ohlc_list_from_DB(asset_dict)
        self.ohlc_data_frame = pd.DataFrame(
            [row[:5] for row in self.ohlc_list],  # Select the first 5 elements of each row
            columns=('TimeStamp', 'Open', 'High', 'Low', 'Close')
        )

        # self.ohlc_data_frame = pd.DataFrame(
        #     self.ohlc_list,
        #     columns=(
        #         'TimeStamp','Open','High','Low','Close'
        #     )
        # )
        
        self.ohlc_data_frame.set_index("TimeStamp", inplace = True)
        self.ohlc_data_frame['Open'] = pd.to_numeric(self.ohlc_data_frame['Open'])
        self.ohlc_data_frame['High'] = pd.to_numeric(self.ohlc_data_frame['High'])
        self.ohlc_data_frame['Low'] = pd.to_numeric(self.ohlc_data_frame['Low'])
        self.ohlc_data_frame['Close'] = pd.to_numeric(self.ohlc_data_frame["Close"])

    def Create_average_price_data_frame(self, asset_dict):
        pass
        # self.Querry_average_price_list_from_DB(asset_dict)
        # ticker = asset_dict['ticker']
        # self.average_price_data_frame = pd.DataFrame(
        #     self.average_price_list,
        #     columns=(
        #         'TimeStamp',f'Price_{ticker}'
        #     )
        # )
        # self.average_price_data_frame.set_index("TimeStamp", inplace = True) 
        # print(self.average_price_data_frame)

    # def Merge_ohlc_data_frames(self, list_of_asset_dicts):
    #     list_of_ohlc_data_frames = []
    #     for asset_dict in list_of_asset_dicts:
    #         pass
    #     self.merged_ohlc_data_frames = pd.concat(list_of_ohlc_data_frames, axis=1, sjoin='inner')
    #     pass

    def Merge_average_price_data_frames(self, list_of_asset_dicts):
        list_of_average_price_data_frames = []
        for asset_dict in list_of_asset_dicts:
            self.Create_average_price_data_frame(asset_dict)
            list_of_average_price_data_frames.append(self.average_price_data_frame)
        
        self.merged_average_price_data_frames = pd.concat(list_of_average_price_data_frames, axis=1, join='inner')
        print(self.merged_average_price_data_frames)

    def return_ohlc_dict(self,asset_dict):
        self.Querry_ohlc_dict_from_DB(asset_dict)
        return self.ohlc_dict

    def return_ohlc_list(self,asset_dict):
        self.Querry_ohlc_list_from_DB(asset_dict)
        return self.ohlc_list

    def return_average_price_dict(self,asset_dict):
        self.Querry_average_price_dict_from_DB(asset_dict)
        return self.average_price_dict

    def return_average_price_list(self,asset_dict):
        self.Querry_average_price_list_from_DB(asset_dict)
        return self.average_price_list

    def return_seperate_ohlc_traces(self,asset_dict):
        self.Create_seperate_ohlc_traces(asset_dict)
        return self.separated_ohlc_traces_dict

    def return_seperate_average_price_traces(self,asset_dict):
        self.Create_seperate_average_price_traces(asset_dict)
        return self.separated_average_price_traces_dict

    def return_ohlc_CSV(self,asset_dict):
        pass

    def return_average_price_CSV(self, asset_dict):
        pass

    def return_ohlc_numpy_array(self,asset_dict):
        self.Create_ohlc_numpy_array(asset_dict)
        return self.ohlc_numpy_array

    def return_average_price_numpy_array(self,asset_dict):
        self.Create_average_price_numpy_array(asset_dict)
        return self.average_price_numpy_array

    def return_ohlc_dataframe(self,asset_dict):
        self.Create_ohlc_dataframe(asset_dict)
        return self.ohlc_data_frame

    def return_average_price_data_frame(self,asset_dict):
        self.Create_average_price_data_frame(asset_dict)
        return self.average_price_data_frame

    def return_merge_average_price_data_frames(self,list_of_asset_dicts):
        self.Merge_average_price_data_frames(list_of_asset_dicts)
        return self.merged_average_price_data_frames

    # def return_merge_ohlc_data_frames(self,list_of_asset_dicts):
    #     self.Merge_ohlc_data_frames(list_of_asset_dicts)
        # return self.merged_ohlc_data_frames
