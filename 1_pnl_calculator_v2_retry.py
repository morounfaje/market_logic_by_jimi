# P p ('') '' : $  {} _ ""

while True:
    print("\n---Profit/Loss Calculator---")
    # take data from trader

    entry = float(input("Entry Price: $"))
    exitPrice = float(input("Exit Price: $"))
    size = int(input("Shares: "))
    commission = float(input("Commission per Share: $"))
    stop_loss = float(input("StopLoss: $"))
    direction = input("Direction (long/short): ") .lower()


    # profit and loss
    if direction == "long":
        gross_pnl = (exitPrice - entry)*size
        risk = entry - stop_loss
        reward = exitPrice - entry
        valid_stop = stop_loss < entry

    elif direction == "short":
        gross_pnl = (entry - exitPrice)*size
        risk = stop_loss - entry
        reward = entry - exitPrice
        valid_stop = stop_loss > entry

    else: 
        print("Invalid direction. Enter 'long' or 'short'.")
        continue #skip to next loop iteration

    net_pnl = gross_pnl - (commission * size)
    pct = net_pnl / (entry * size) if entry * size != 0 else 0

    # Classify Result

    rr = reward/risk  if (valid_stop and risk > 0 and reward != 0) else None
    if net_pnl > 0:
        verdict = "WIN"

    elif net_pnl < 0:
        verdict = "LOSS"
    else:
        verdict = "BREAKEVEN"


    print(f"\n ---RESULT ({direction.upper()})---")
    print(f"Gross P&L: ${gross_pnl:,.2f}")
    print(f"Net P&L: ${net_pnl:,.2f}")
    print(f"Return: ${pct:.1%}")
    print(f"R:R Ratio: {rr:.2f}" if rr else "R:R Ratio: N/A(Invalid stop)")




    if input ("\n Another trade (y/n): ") .lower() !="y": 
        break