# P p ('') '' : $  {} "" _

# Blacklist

blacklist = {"MEME", "SCAM", "FAKE"}


# Log a trade
def log_trade(trades, ticker, direction, entry, exit_price, size):
    ticker = ticker.upper()

    # Reject blacklisted tickers
    if ticker in blacklist:
        print(f"\n{ticker} is blacklisted. Trade rejected")
        return None

    # Calculate PnL
    if direction == "long":
        pnl = (exit_price - entry) * size
    else:
        pnl = (entry - exit_price) * size

    # Trade dictionary
    trade = {
        "ticker": ticker,
        "direction": direction,
        "entry": entry,
        "exit": exit_price,
        "size": size,
        "pnl": pnl
    }

    # Add trade to list
    trades.append(trade)
    print(f"Trade logged: {ticker}, PnL: ${pnl:+,.2f}")
    return trade


# Show all trades
def show_trades(trades):

    if not trades:
        print("\nNo Trades")
        return

    print("\nALL TRADES")

    for i, trade in enumerate(trades, start=1):
        print(
            f"{i}. {trade['ticker']},"
            f"{trade['direction']},"
            f"PnL: ${trade['pnl']:+,.2f}"
        )

# Rank trades by pnl

def ranked_trades(trades):
    if not trades:
        print("No Trades")
        return

    # Sort highest pnl to the lowest
    ranked = sorted(
        trades,
        key = lambda trade: trade["pnl"],
        reverse = True
    )

    print("\nPnL Ranking")
    for rank, trade in enumerate(ranked, start=1):
        print(
            f"{rank}.{trade['ticker']}"
            f"${trade['pnl']:+,.2f}"
        )

# Filter by ticker

def filter_by_ticker(trades, ticker):
    ticker = ticker.upper()

    filtered = [
        trade
        for trade in trades
        if trade["ticker"] == ticker
    ]

    if not filtered:
        print(f"No trades found for {ticker}")
        return

    print(f"\n{ticker} Trades")

    for trade in filtered:
        print(
            f"{trade['direction']},"
            f"Entry: {trade['entry']},"
            f"Exit: {trade['exit']},"
            f"PnL: ${trade['pnl']:+,.2f}"
        )

# Session Summary

def session_summary(trades):

    if not trades:
        print("No trades in this session")
        return

    pnls = [trade["pnl"] for trade in trades]
    winners = [p for p in pnls if p > 0]
    tickers = {trade["ticker"] for trade in trades}
    win_rate = len(winners) / len(pnls)

    print("\nSESSION SUMMARY")
    print(f"Trades: {len(trades)}")
    print(f"Win rate: {win_rate:.1%}")
    print(f"Total PnL: ${sum(pnls):+,.2f}")
    print(f"Best Trade: ${max(pnls):+,.2f}")
    print(f"Worst Trade: ${min(pnls):+,.2f}")
    print(f"Tickers traded: {tickers}")

# Main Program

trade_log =[]
while True:
    print("\nTRADE LOGGER")
    print("1. Log Trade")
    print("2. View Summary")
    print("3. Rank Trades by PnL")
    print("4. Filter by Ticker")
    print("5. View all trades")
    print("6. Quit")

    choice = input("Enter your choice: ")

    # Log trade

    if choice == "1":

        ticker = input("Ticker: ")
        direction = input("Direction (long/short): ").lower()
        entry = float(input("Entry Price: "))
        exit_price = float(input("Exit Price: "))
        size = int(input("Size: "))

        log_trade(trade_log, 
                  ticker, 
                  direction, 
                  entry, 
                  exit_price, 
                  size
            )

    # Summary

    elif choice == "2":
        session_summary(trade_log)
    
    # Rank by PnL
    elif choice == "3":
        ranked_trades(trade_log)

    # Filter by Ticker
    elif choice == "4":
        ticker = input("Enter ticker: ")
        filter_by_ticker(
            trade_log, 
            ticker
        )

    # View all trades
    elif choice == "5":
        show_trades(trade_log)

    # Quit
    elif choice == "6":
        print("Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")