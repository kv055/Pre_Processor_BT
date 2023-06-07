import sys

# Add the folder path containing the library to the sys.path list
sys.path.append('/workspaces/Pre_Procesor_BT/vectorbt-master')

# Now you can import the library as usual
import vectorbt as vbt

price = 

pf = vbt.Portfolio.from_holding(price, init_cash=100)
pf.total_profit()