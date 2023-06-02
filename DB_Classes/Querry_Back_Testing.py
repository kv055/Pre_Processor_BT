
from DB_Classes.sqalchemy_connect import SQL_Server

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Index(Base):
    __tablename__ = 'index'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(255))
    data_provider = Column(String(255))
    strategy = Column(String(255))
    parameter = Column(String(255))
    pnl = Column(Float)

class Trades(Base):
    __tablename__ = 'trades'

    Ticker = Column(String(15), primary_key=True)
    Data_Provider = Column(String(10), primary_key=True)
    Open = Column(DateTime, primary_key=True)
    Direction = Column(String(10))
    Asset_Price = Column(Float)
    Position_Size = Column(Float)
    Leverage = Column(Integer)
    Signal = Column(String(255))
    Current_Asset_Balance = Column(Float)
    Current_Cash_Balance = Column(Float)
    Prev_Asset_Balance = Column(Float)
    Prev_Cash_Balance = Column(Float)
    Trade_From = Column(Float)
    Trade_To = Column(Float)
    Closed = Column(String(255))

db_name = 'Back_testing'
connection_instance = SQL_Server(db_name)
# engine = connection_instance.get_engine()
session = connection_instance.get_session()


class QuerryTradesDummyData:
    # def return_all_trades(self):
    #     index_records = session.query(Index).all()

    #     trades_list = []

    #     for index in index_records:
    #         ticker = index.ticker
    #         data_provider = index.data_provider

    #         # Fetch the trades with matching ticker and data_provider
    #         trades = session.query(Trades).filter_by(Ticker=ticker, Data_Provider=data_provider).all()
    #         trades_tuples = [(trade.Ticker, trade.Data_Provider, trade.Open, trade.Direction, trade.Asset_Price, trade.Position_Size, trade.Leverage, trade.Signal, trade.Current_Asset_Balance, trade.Current_Cash_Balance, trade.Prev_Asset_Balance, trade.Prev_Cash_Balance, trade.Trade_From, trade.Trade_To, trade.Closed) for trade in trades]  # Convert trades to tuples manually

    #         trades_list.append({
    #             'data_provider': data_provider,
    #             'ticker': ticker,
    #             'trades': trades_tuples
    #         })

    #     return trades_list
    def return_all_trades(self):
        index_records = session.query(Index).all()

        trades_list = []

        for index in index_records:
            ticker = index.ticker
            data_provider = index.data_provider

            # Fetch the trades with matching ticker and data_provider
            trades = session.query(Trades).filter_by(Ticker=ticker, Data_Provider=data_provider).all()
            trades_dicts = [trade.__dict__ for trade in trades]  # Convert trades to dictionaries

            trades_list.append({
                'data_provider': data_provider,
                'ticker': ticker,
                'trades': trades_dicts
            })

        return trades_list



