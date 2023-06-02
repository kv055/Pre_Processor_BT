import backtrader as bt

class SmaCross(bt.Strategy):
    params = dict(
        pfast=10,
        pslow=30
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)
        sma2 = bt.ind.SMA(period=self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
                print(f'Buy executed at {self.data.close[0]:.2f}')

        elif self.crossover < 0:
            self.close()
            print(f'Sell executed at {self.data.close[0]:.2f}')

