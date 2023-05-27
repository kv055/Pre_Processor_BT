from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm.attributes import instance_dict
from sqlalchemy.types import DateTime

from sqalchemy_connect import SQL_Server
db_name = 'Financial_Data'
connection_instance = SQL_Server(db_name)
Base = connection_instance.get_base()
session = connection_instance.get_session()

class OHLC(Base):
    __tablename__ = 'OHLC'

    Date = Column(DateTime, primary_key=True)
    Open = Column(Float, nullable=False)
    High = Column(Float, nullable=False)
    Low = Column(Float, nullable=False)
    Close = Column(Float, nullable=False)
    Average = Column(Float, nullable=False)
    Data_Provider = Column(String(45), primary_key=True)
    Ticker = Column(String(45), primary_key=True)
    Time_Frame = Column(String(45), nullable=False)



class Asset(Base):
    __tablename__ = 'Assets'

    data_provider = Column(String(255), primary_key=True)
    ticker = Column(String(45), primary_key=True)
    historical_data_url = Column(String(255))
    historical_data_req_body = Column(String(255))
    live_data_url = Column(String(255))
    live_data_req_body = Column(String(255))
    id = Column(Integer, autoincrement=True, primary_key=True)
    first_available_datapoint = Column(DateTime)
    last_available_datapoint = Column(DateTime)


class Querry_Assets_OHLC_from_DB:
    def __init__(self) -> None:
        db_name = 'Financial_Data'

    def return_all_assets(self):
        assets = session.query(Asset).all()
        asset_dicts = [instance_dict(asset) for asset in assets]
        return asset_dicts

    def return_historical_ohlc_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        ohlc_results = session.query(OHLC).filter(
            # OHLC.Data_Provider == data_provider
            OHLC.Ticker == ticker
        ).all()
        return ohlc_results

    # def return_historical_average_price_from_db(self, asset_dict):
    #     ticker = asset_dict['ticker']
    #     data_provider = asset_dict['data_provider']
    #     ohlc_results = session.query(OHLC).filter(
    #         OHLC.data_provider == data_provider,
    #         OHLC.ticker == ticker
    #     ).all()

    #     result_list = []
    #     for row in ohlc_results:
    #         average = (row.open + row.high + row.low + row.close) / 4
    #         del row.open
    #         del row.high
    #         del row.low
    #         del row.close
    #         row.average_price = average
    #         result_list.append(row)

    #     return result_list
