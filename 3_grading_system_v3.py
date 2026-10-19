# P p ('') '' : $  {} _ "" ("")

trades = [
    {"symbol": "EURUSD", "pnl": 120},
    {"symbol": "GBPUSD", "pnl": -80},
    {"symbol": "XAUUSD", "pnl": 250},
    {"symbol": "USDJPY", "pnl": -50}
]


# args, calculate total p&l

def total_pnl(*pnls):
    return sum(pnls)


#default argument, risk 1% unless changed

def position_size(balance, risk_pct = 1):
    return balance * risk_pct / 100


# filter() + lambda, keep winning trades

winners = list(
    filter(lambda trade: trade["pnl"] > 0, trades)
)


# sorted() + lambda, rank trades by p&l

ranked = sorted(
    trades,
    key = lambda trade: trade["pnl"],
    reverse = True
)


# total p&l

total = total_pnl(
    120,
    -80,
    250,
    -50
)

print("Total P&L:", total)


# calculate position size

risk = position_size(10000)

print("Risk per trade:", risk)


# show winners

print("\nWinning trades:")

for trade in winners:
    print(trade["symbol"], trade["pnl"])


# show ranking

print("\nTrade ranking:")

for trade in ranked:
    print(trade["symbol"], trade["pnl"])