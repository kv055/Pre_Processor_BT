from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm.attributes import instance_dict
from sqlalchemy.types import DateTime

from DB_Classes.sqalchemy_connect import SQL_Server

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
        pass

    def return_all_assets(self):
        assets = session.query(Asset).all()
        asset_dicts = [instance_dict(asset) for asset in assets]
        return asset_dicts

    def return_historical_ohlc_dict_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        ohlc_results = session.query(OHLC).filter(
            OHLC.Ticker == ticker,
            OHLC.Data_Provider == data_provider
        ).all()
        ohlc_dicts = [instance_dict(ohlc) for ohlc in ohlc_results]
        return ohlc_dicts
    
    def return_historical_ohlc_list_from_db(self, asset_dict):
        ticker = asset_dict['ticker']
        data_provider = asset_dict['data_provider']
        ohlc_results = session.query(OHLC).filter(
            OHLC.Ticker == ticker,
            OHLC.Data_Provider == data_provider
        ).all()
        ohlc_lists = [[
            ohlc.Date,
            ohlc.Open,
            ohlc.High,
            ohlc.Low,
            ohlc.Close,
            ohlc.Average,
            ohlc.Data_Provider,
            ohlc.Ticker,
            ohlc.Time_Frame
        ] for ohlc in ohlc_results]
        return ohlc_lists

