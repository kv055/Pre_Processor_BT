from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm.attributes import instance_dict
from sqlalchemy.types import DateTime

from DB_Classes.sqalchemy_connect import SQL_Server

db_name = 'Live_Trading_Logs'
connection_instance = SQL_Server(db_name)
Base = connection_instance.get_base()
session = connection_instance.get_session()


class LogStrategyOutput(Base):
    __tablename__ = 'LOG_STRATEGY_OUTPUT'

    Asset_Price = Column(String(255), primary_key=True)
    Portfolio_Ballances = Column(String(255), nullable=False)
    Trade_Signal = Column(String(255), nullable=False)
    Order_Sent = Column(String(255), nullable=False)
    Order_Confirmation_Rejection_msg = Column(String(255), nullable=False)

class QuerryLogStrategyOutput:
    def __init__(self) -> None:
        db_name = 'Financial_Data'

    def return_all_log_strategy_output(self):
        logs = session.query(LogStrategyOutput).all()
        log_dicts = [instance_dict(log) for log in logs]
        return log_dicts

    def return_log_strategy_output_by_asset_price(self, asset_price):
        logs = session.query(LogStrategyOutput).filter(LogStrategyOutput.Asset_Price == asset_price).all()
        log_dicts = [instance_dict(log) for log in logs]
        return log_dicts
